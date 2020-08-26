Get stock, fx, or crypto OHLCV data from kaggle, alpha vantage, or yahoo; pick one API provider which has high low open.

1. Get stock data with node; can use it from cli or js

```bash
npm i -g alpha-vantage-cli
alpha-vantage-cli --type=daily --symbol=MSFT --api-key=demo --out=MSFT_daily.csv
```

2. Or with python 

```bash
cd 10\stock-trading-ml-master
python save_data_to_csv.py MSFT daily
```

- add creds.json containing { av_api_key: 'your_alpha_vantage_key'}


3. Integrate with exchange because you're gonna need it anyway

4. Try binary and ternary classification - buy/sell or buy/do-nothing/sell

5. Try regression to predict future price with LSTM/RNNs/CNNs on ohlcv & indicators like MACD/RSI; find a way to classify good trades better than if predicted_price>current_price

6. Try anomaly detection on volume/price for early signals

7. Try Random Forest and Gradient Boosted trees / ensemble methods for 

8. Try GANNs for encoding good trades to make a model that generalizes well across markets given indicators regardless of market and noise