import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = """請在網址列上選擇要看的公司名單：<br/>
    /nasdaq ==> nasdaq 的公司名單<br/>
    /nyse ==> nyse 的公司名單<br/>
    /amex ==> amex 的公司名單<br/>
    """
    return message

@app.route('/nyse')
def nyse():
    url='https://drive.google.com/uc?export=download&id=1htM3zRwKJ31tvlIGl0J3C0cPak8jdeeX'
    NYSE=pd.read_csv(url)
    return NYSE.to_html()


@app.route('/nyse/<symbol>')
def nyse_company(symbol):
    url='https://drive.google.com/uc?export=download&id=1htM3zRwKJ31tvlIGl0J3C0cPak8jdeeX'
    NYSE_SYMBOL=pd.read_csv(url)
    NYSE_SYMBOL=NYSE_SYMBOL.loc[NYSE_SYMBOL['Symbol']==symbol]
    return NYSE_SYMBOL.to_html()

@app.route('/nasdaq')
def nasdaq():
    url='https://drive.google.com/uc?export=download&id=1IvgzQwu1KpF7tcb3dOYwj7rzu9z7RF8Y'
    NASDAQ=pd.read_csv(url)
    return NASDAQ.to_html()

@app.route('/nasdaq/<symbol>')
def nasdaq_company(symbol):
    url='https://drive.google.com/uc?export=download&id=1IvgzQwu1KpF7tcb3dOYwj7rzu9z7RF8Y'
    NASDAQ_SYMBOL=pd.read_csv(url)
    NASDAQ_SYMBOL=NASDAQ_SYMBOL.loc[NASDAQ_SYMBOL['Symbol']==symbol]
    return NASDAQ_SYMBOL.to_html()

@app.route('/amex')
def amex():
    url='https://drive.google.com/uc?export=download&id=1puJOnwS4jTiZVcdDHEYPFsHvu0H8ngzk'
    AMEX=pd.read_csv(url)
    return AMEX.to_html()

@app.route('/amex/<symbol>')
def amex_company(symbol):
    url='https://drive.google.com/uc?export=download&id=1puJOnwS4jTiZVcdDHEYPFsHvu0H8ngzk'
    AMEX_SYMBOL=pd.read_csv(url)
    AMEX_SYMBOL=AMEX_SYMBOL.loc[AMEX_SYMBOL['Symbol']==symbol]
    return AMEX_SYMBOL.to_html()

if __name__=="__main__":
    app.run()
