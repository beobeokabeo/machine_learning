# Index, motivation, algos, models

## Goals

---

- Combine
- K random nearest trees for clustering, classifying and looking up of similar historical matches/data
- with random forest decision trees making decisions based on outputs of LSTM, neural networks, classification
- automating data acquisition, continuous labeling, and regression
- auto generation of trading strategy and risk management
- and hyper parameter tuning via genetic algo
- To build an automated algo trading bot to build up capital for future business ventures
- add extra NLP driven model looking at news stories and trading sites to extract sentiment (alpha signal)
- Alexandria, Stock tweets, morning star/t

### 1. Basic strategy

---
> Task, Experience, Performance

- a. Combine price + volume
  - normalize price percentage movement by ATR - average true range gives more relative movement to each currency
  - volume is really important

- b. Ex hypothesis:
  - What is the ATR change in price in the first 5 minutes,
     multiplied by the volume in the first 5 mins, divided by the average volume?

- c. Measure money flow in system. Total bid vs ask
  - how many trades are happening on the bid?
  - how many trades are happening on the ask?

## I. Process and Steps

>*How to approach a ML problem*

### 1. Create a **hypothesis**

- What does the model need to **achieve**?

### 2. Create test for hypothesis with goal of model

- Is the model achieving its *goals*?
- Decide on *measurement of success*

### 3. Gather and process data applicable to hypothesis

  1. Feature engineering
    - build features to automate the process of the next steps
  2. Normalize, clean up, de-noise, curate data
  3. Label data 
  4. decide on ML algo to use 
  5. split data into training, testing, validation sets

### 4. Algorithms to use

  > Supervised learning: *classification and regression algos*
  > vs unsupervised adversarial generative // hyperGANN 255bit

1. Classification:
   - classify data/results into different sets then look up relevant sets/function calculation
   - easier problem to solve
   - bucket trades into different groups and label each one as a CLASS
   - e.g. 2 classes:
     - 1 is positive trades that have returned > $0 which have returned money
     - vs negative trades that have lost money... < $0
2. Regression
   - make predictions
   - regression is more difficult for machine to estimate accurately with market data because it's noisy
   - Stick to classification rather than regression most of the time
     - guessing is hard
     - grouping / clustering is easy

3. Neural nets
   - Give price movements or the volume changes
   - It'll combine them in ways it sees most fit

4. Decision trees
   - gradient boosted trees
   - careful not to overfit data

5. Random forrest = groups of thousands of decision trees

- maximize entropy/knowledge gained
  - math equation of how to measure performance
  - up to certain max depth

### 5. Label all your data

---
> *"useless metadata is the most useful of all data"*

- Use continuous labels, not discrete
- you're asking machine to predict what the return is going to be by the end of the day
- chooses any number within a test

### 6. Train your models

---

1. Train it
2. Test it
3. Tune it
4. goto step 1
   - train model on walk-forward basis to make predictions seeing goal
   - evaluate predictions and goals
   - research trade expression (how u execute your trade after receiving signal)
   - store result, classify, reuse
   - try training using multiple different labes or number of dimensions
  
5. Finish algorithm to manage position, risk control, etc
   - Optimize ENTRY AND EXIT SIGNALS
   - measure on shorter term basis rather than total percentage by end of day
      - dont put all of them in the same bucket
      - the more dimensions - the more data

6. Use genetic algo for hyper-parameter tuning
   - evaluate % of good vs bad trades in each node of decision tree

### 7. Plan, Do, Check, Act, Loop

---

## Feature Selection

> What relevant data and in how many dimensions to keep track of it?
---

1. Features are important both for
   - Input data
   - “Predicted” response (outputs)
     - Too many features -> overfitting… *Be careful!*

2. Feature selection
- Input feature
  - Technical indicators
  - Changes in Prices, Volumes, Ratios
  - External series
  - News feeds
  - Time of day

- Output features
  - Discrete moves
  - up/down/flat etc.
  - True/false
  - Probabilities

## Case Studies, Research and examples

---

### 1. **Example_1**: Analysis of Hidden Markov Models and Support Vector Machines in Financial Applications

---
> Rao and Hong 2010

1. Rao and Hong try to predict future prices of 10 stocks and 1 index
   - 0.51 to 0.7 accuracy
2. They used:
   - K-means clustering
   - Hidden Markov model
   - Support vector machine

3. Inputs were:
   - EMA7, EMA50, EMA200
   - MACD, RSI, ADX,
   - High, Low, Close,Close>EMA200, lagged profits

- They used both a supervised and unsupervised methodology.

---

#### Methodology 1 – unsupervised (HMM)

1. Use the K-means to identify 5 hidden states (clusters)
   - big price up, small price up, no change, small price down, big price down]
2. Use HMM and daily lag profits to determine:
   - “What is the probability of seeing a big price drop tomorrow given today’s state and observations.”

#### Methodology 2 – supervised (SVM)

- Classify each training day as a buy/sell signal, and use the 10  inputs described above to train the SVM
- Use a RBF Kernel to produce nonlinear decision boundary
- Experimented with adding a new input – # of news stories

| ticker | accuracy |
| :----: | :------: |
|  pot   |  0.5172  |
|  msft  |  0.7586  |
|   gg   |  0.5862  |

---

### **Example_2/Methodology_3**: Random Forrests

- Two examples:
  1. Lauretto, Silva, Andrade 2013
       - “Evaluation of a Supervised Learning Approach for Stock Market Operations - Theofilatos
  2. Likothanassis and Karathanasopoulos 2012
       - “Modeling and Trading the EUR/USD Exchange Rate Using Machine Learning Techniques”

- Both teams use Random Forests (classification trees) to build classifiers

#### **Example_2**: Lauretto et al

---

1. Methodology
   - Daily equities data (OHLCV)

2. Inputs:
   - SMAs, EMAs, ROC, Stoch, MACD, RSI

3. Classes are:
   - {Buy-Sell,
   - Sell-Buy,
   - Do-nothing}

4. *Results*:
   - 80% “successful devised operations”
   - 70% “seized opportunities”
   - Average return per operation: 4%

#### **Example_3**: Theofilatos et al

---

1. Methodology
   - Predicting one day ahead EUR/USD
   - Only use autoregressive inputs, i.e. up to 10 days lagged data used as inputs
   - Compared a bunch of ML algos, including SVM (with RBF kernel), RFs, NN, Naïve Bayes
