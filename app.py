from line_bot_api import *
from events.basic import *
from events.oil import *
from events.EXRate import *
from events.Msg_Template import *
from model.mongodb import *
import re #爬蟲模組
import twstock #要pip
import datetime


app = Flask(__name__)

@app.route("/callback", methods = ['POST'])
def callback():
    ##
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)


    try:
        handler.handle(body, signature)
    except IndentationError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)#抓取使用者ID
    uid = profile.user_id #指定變數存取 使用者ID
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip()#使用者輸入的內容
    emsg = event.message.text
    user_name = profile.display_name
    

    ###################### 匯率區 #####################################
    if re.match('匯率查詢', emsg):
        message = show_Button()
        line_bot_api.reply_message(event.reply_token, message)

    if re.match('查詢匯率[A-Z{3}]',msg):
        msg = msg[4:]
        content = showCurrency(msg)
        line_bot_api.push_message(uid,TextSendMessage(content))

    if re.match("換匯[A-Z]{3}/[A-Z{}]", msg):
        line_bot_api.push_message(uid, TextSendMessage("將為您做換匯計算..."))
        content = getExchangeRate(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))


    ##################### 說明選單 選單 ################################

    if message_text == "@使用說明":
        about_us_event(event)
        Usage(event)

    ##################### 油價查詢 ####################################
    if event.message.text == "油價查詢" or event.message.text == "@油價查詢" :
        content = oil_price()
        line_bot_api.reply_message(
            
            event.reply_token, 
            TextSendMessage(text = content)
        )


    ###################### 股票區 #####################################
    if event.message.text == '@股價查詢':
        line_bot_api.push_message(uid, TextSendMessage("請輸入#加股票代碼......"))

    ##股價查詢
    if re.match("@股價查詢", msg):
        stockNumber = msg[5:]
        btn_msg = stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    
    ##新增使用者關注的股票 (存到mongoDB)
    if re.match('關注[0-9]{4}[<>][0-9]', msg):
        stockNumber = msg[2:6]
        line_bot_api.push_message(uid, TextSendMessage("加入股票代號"+stockNumber))
        content = write_my_stock(uid, user_name, stockNumber,msg[6:7], msg[7:])
        line_bot_api.push_message(uid, TextSendMessage(content))
    # else:
    #     content = write_my_stock(uid, user_name, stockNumber, "未設定", "未設定")
    #     line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    
    if re.match('股票清單',msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下，股票查詢中...'))
        content = show_stock_setting(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0


    if (emsg.startswith('#')):
        text = emsg[1:]
        content =''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content +='%s (%s) %s\n' % (
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)
        
        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        
        content += '最高: %s / 最低:%s\n'%(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])
        
        content += '量: %s\n'%(stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' % (date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text=content)
        )


@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = '''$ stock block_oil $
您好! 歡迎成為 stock block_oil的好友!
我是您的股市小幫手

這裡有股票油價等生活經濟資訊唷!
請直接點選下方連結選單'''
    line_bot_api.reply_message(
        event.reply_token, 
        TextSendMessage(text = welcome_msg)
    )

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)


    # if event.message.text == "@小幫手":
    #     buttons_template = TemplateSendMessage(
    #         alt_text = '小幫手template', 
    #         template=ButtonsTemplate(
    #             title="選擇服務", 
    #             text="請選擇",
    #             thumbnail_image_url = 'https://i.imgur.com/vtOU7MO.jpg', 
    #             actions=[
    #                 MessageTemplateAction(
    #                     label='油價查詢', 
    #                     text='油價查詢'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='匯率查詢', 
    #                     text='匯率查詢'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='股價查詢', 
    #                     text='股價查詢'
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token, buttons_template)
    # 以上移動至basic.py

if __name__ == "__main__":
    app.run()

