from line_bot_api import *
from events.basic import *
from events.oil import *


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
    
    
    #####################說明選單 選單 油價查詢########################

    if message_text == "@使用說明":
        about_us_event(event)
        Usage(event)

    if event.message.text == "想知道油價":
        content = oil_price()
        line_bot_api.reply_message(
            
            event.reply_token, 
            TextSendMessage(text = content)
        )
    ###################### 股票區 #####################################
    if event.message.text == '股價查詢':
        line_bot_api.push_message(uid, TextSendMessage("請輸入#加股票代碼......"))



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

