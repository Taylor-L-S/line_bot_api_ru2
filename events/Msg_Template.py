from line_bot_api import *


def stock_reply_other(stockNumber):
    content_text = "即時股價K線圖"
    text_message = TextSendMessage(
                            text = content_text, 
                            quick_reply=QuickReply(
                                items=[
                                    QuickReplyButton(
                                        action=MessageAction(
                                            label="即時股價",
                                            text="#"+stockNumber
                                        )
                                    ),
                                    QuickReplyButton(
                                        action=MessageAction(
                                            label = "K線圖",
                                            text = "@K"+stockNumber
                                        )
                                    ),
                                ]
                            ))
    

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "幣別種類",
                            "weight": "bold",
                            "size": "xl",
                            "color": "#AA2B1D"
                        }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "美金",
                                "text": "USD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "日圓",
                                "text": "JPY"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "港幣",
                                "text": "HKD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "英鎊",
                                "text": "GBP"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "澳幣",
                                "text": "AUD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "加幣",
                                "text": "CAD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "瑞-法郎",
                                "text": "CHF"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "新加坡",
                                "text": "SGD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "南非幣",
                                "text": "ZAR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "瑞典幣",
                                "text": "SEK"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "泰幣",
                                "text": "THB"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "菲比索",
                                "text": "PHP"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "印尼幣",
                                "text": "IDR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "韓元",
                                "text": "KRW"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "馬來幣",
                                "text": "MYR"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "越南盾",
                                "text": "VND"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "人民幣",
                                "text": "CNY"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "紐元",
                                "text": "NZD"
                                },
                                "gravity": "center",
                                "style": "primary",
                                "color": "#92BEF9",
                                "margin": "sm"
                            }
                            ]
                        }
                        ]
                    }
                    }
                    
    )
    return flex_message


# #股價查詢        
#     if re.match('想知道股價',msg):
#         stockNumber = msg[2:6]
#         btn_msg = stock_reply_other(stockNumber)
#         line_bot_api.push_message(uid,btn_msg)
#         return 0
    
#     if (emsg.starkswith('#')):
#         text = emsg[1:]
#         content = ''

#         stock_rt = twstock.realtime.get(text)
#         my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
#         my_time = my_datetime.strftime('%H:%M:%S')

#         content += '%s (%s) %s\n' %(
#             stock_rt['info']['name'],
#             stock_rt['info']['code'],
#             my_time)
#         content += '現價： %s  / 開盤： %s \n' %(
#             stock_rt['realtime']['latest_trade_price'],
#             stock_rt['realtime']['open']
#         )
#         content += '最高： %s  / 最低：  %s \n'%(
#             stock_rt['realtime']['high'],
#             stock_rt['realtime']['low']
#         )
#         content += '量： %s\n' %(stock_rt['realtime']['accumulate_trade_colume'])



#     stock = twstock.stock(text) #twstock.stock('2330')
#         content += '-----\n'
#         content += '最近五日價格： \n'
#         price5 = stock.price[-5:][::-1]
#         date5 = stock.date[-5][::-1]
#         for i in range(len(price5)):
#             #content +='[%s] %s\n' %(date5[i].strftime('%Y-%m-%d %H:%M:%S'),price5[i]) 
#             content +='[%s] %s\n' %(date5[i].strftime('%Y-%m-%d'),price5[i])
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text = content)
#         )