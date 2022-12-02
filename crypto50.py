import webbrowser
import time

symbolsList = [
   "BTC-USD","ETH-USD","USDT-USD","BNB-USD","USDC-USD","BUSD-USD","XRP-USD","DOGE-USD","ADA-USD","MATIC-USD","DOT-USD","DAI-USD","HEX-USD","WTRX-USD","LTC-USD","SHIB-USD","TRX-USD","SOL-USD","UNI7083-USD","STETH-USD","AVAX-USD","LINK-USD","WBTC-USD","LEO-USD","ATOM-USD","ETC-USD","XMR-USD","XLM-USD","TON11419-USD","BCH-USD","ALGO-USD","CRO-USD","QNT-USD","FIL-USD","NEAR-USD","APE18876-USD","VET-USD","OKB-USD","ICP-USD","FLOW-USD","HBAR-USD","LUNC-USD","WBNB-USD","HT-USD","EGLD-USD","TWT-USD","FRAX-USD","EOS-USD","CHZ-USD","USDP-USD"
]

for cryptoSymbol in symbolsList:
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{cryptoSymbol}?period1=1512172800&period2=1669939200&interval=1d&events=history&includeAdjustedClose=true"
    webbrowser.open(url)
    time.sleep(1)