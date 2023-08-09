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
    return text_message


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