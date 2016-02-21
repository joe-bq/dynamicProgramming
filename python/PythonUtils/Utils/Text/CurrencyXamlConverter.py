'''
Created on Nov 5, 2013

@author: wangboqi
'''

currencies = ["USD",
        "JPY",
        "AUD",
        "CAD",
        "CHF",
        "CNY",
        "CZK",
        "DEM",
        "EUR",
        "FIM",
        "GBP",
        "GRD",
        "HKD",
        "IDR",
        "INR",
        "ISK",
        "KRW",
        "MXP",
        "MYR",
        "NZD",
        "PHP",
        "PLN",
        "SEK",
        "SGD",
        "THB",
        "TRY",
        "TWD",
        "VND",
        "ZAR"]

currencies2 = list(["USD",
        "JPY",
        "AUD",
        "CAD",
        "CHF",
        "CNY",
        "CZK",
        "DEM",
        "EUR",
        "FIM",
        "GBP",
        "GRD",
        "HKD",
        "IDR",
        "INR",
        "ISK",
        "KRW",
        "MXP",
        "MYR",
        "NZD",
        "PHP",
        "PLN",
        "SEK",
        "SGD",
        "THB",
        "TRY",
        "TWD",
        "VND",
        "ZAR"])

if __name__ == '__main__':
    for c in currencies:
        print "<sys:String>{0}</sys:String>".format(c)
    for c in currencies2:
        print "<sys:String>{0}</sys:String>".format(c)