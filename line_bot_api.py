from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

#必須放上自己的Channel access token
line_bot_api = LineBotApi('DX8K+3OThP2vbtYoebijLy7gosZVVSDxZAVVfvNilq6+t4yZ10g1HK74dMF3lglMlOXdSO7e9uFH4306LoYVEDQ+SW0web3KggvUFS94ciyQIX4aGgSBi8UicNe2Nr6p9KVMAlIvKGRPj1BB1YF+agdB04t89/1O/w1cDnyilFU=')
#必須放上自己的Channel secret
handler = WebhookHandler('880545b3fef970a1460a69447feee723')
