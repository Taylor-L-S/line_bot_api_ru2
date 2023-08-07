from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

#必須放上自己的Channel access token
line_bot_api = LineBotApi('DX8K+3OThP2vbtYoebijLy7gosZVVSDxZAVVfvNilq6+t4yZ10g1HK74dMF3lglMlOXdSO7e9uFH4306LoYVEDQ+SW0web3KggvUFS94ciyQIX4aGgSBi8UicNe2Nr6p9KVMAlIvKGRPj1BB1YF+agdB04t89/1O/w1cDnyilFU=')
#必須放上自己的Channel secret
handler = WebhookHandler('880545b3fef970a1460a69447feee723')

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

if __name__ == "__main__":
    app.run()

