def getExchangeRate(msg):#不圖貨幣直接換算(非只限於台幣)
    """
    sample
    code = "換匯USD/TWD/100;
    code = '換匯USD/JPY/100'
    """
    currency_list = msg[2:].split('/')
    currency = currency_list[0] # 輸入想查詢的匯率
    currency1 = currency_list[1] #輸入想兌換的匯率
    money_value = currency_list[2] #輸入金額數值
    url_coinbase = 'https://api.coinbase.com/v2/exchange-rates?currency=' + currency
    res = requests.get(url_coinbase)
    jData = res.json()
    pd_currency = jData['data']['rates']
    content = f'目前的兌換率為:{pd_currency[currency1]}{currency1} \n查詢的金額'
    amount = float(pd_currency[currency1])
    content += str('%.2f' % (amount * float(money_value))) + "" + currency1
    return content