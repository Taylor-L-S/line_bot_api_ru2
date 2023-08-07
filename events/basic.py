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