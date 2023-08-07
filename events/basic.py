from line_bot_api import *

def about_us_event(event):
    emoji = [
        {
            "index":0,
            "productId":"5ac2213e040ab15980c9b447",
            "emojiId":"035"

        },
        {
            "index":18,
            "productId":"5ac2213e040ab15980c9b447",
            "emojiId":"035"

        }
    ]

    text_message = TextSendMessage(text='''$ stock block_oil $
您好! 歡迎成為 stock block_oil的好友!
我是您的股市小幫手

這裡有股票油價等生活經濟資訊唷!
請直接點選下方連結選單''', emojis = emoji)
    sticker_message = StickerMessage(
        package_id = '8522',
        sticker_id='16581271'
    )

    line_bot_api.reply_message(
        event.reply_token, 
        [text_message, sticker_message])
    
def push_msg(event,msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id,TextSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id, TextSendMessage(text=msg))

# def Usage(event):
#     push_msg(event, "  ❕查詢方法❕  \
#              \n小幫手可以查詢匯率股價油價 \
#              \n油價請輸入油價")
def Usage(event):
    push_msg(event,'✨✨ 查詢方法 ✨✨ \
             \n\
             \n\小幫手可以查詢油價 匯率 股價\
             \n\
             \n\油價通知 ➡️➡️➡️ 輸入可以查詢油價\
             \n\匯率通知 ➡️➡️➡️ 輸入可以查詢匯率\
             \n\匯率兌換 ➡️➡️➡️ 換匯USD/TWD\
             \n\股價查詢 ➡️➡️➡️ 輸入#股票代號')    