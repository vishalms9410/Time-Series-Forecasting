# 📈 Stock Price Forecasting Using LSTM and ARIMA

## 📌 Project Overview

This project is an interactive **Stock Price Forecasting web application** developed using **Python and Streamlit**. The application fetches historical stock market data from Yahoo Finance and uses time-series forecasting techniques to analyze stock price behavior and predict future prices.

The project combines **LSTM (Long Short-Term Memory)** and **ARIMA (AutoRegressive Integrated Moving Average)** models to provide both deep-learning-based and statistical approaches to time-series forecasting.

The application also provides interactive stock analysis using **Plotly**, along with technical indicators such as **RSI, MACD, candlestick charts, and line charts**.

> ⚠️ **Disclaimer:** This project is developed for educational and analytical purposes. Stock market predictions are uncertain and should not be considered guaranteed investment advice.

---

## 🎯 Objectives

* Analyze historical stock market data.
* Preprocess time-series data for machine learning.
* Forecast future stock prices using LSTM.
* Analyze trends and time-series behavior using ARIMA.
* Evaluate forecasting performance using RMSE.
* Provide technical indicators such as RSI and MACD.
* Create interactive stock visualizations using Plotly.
* Build an easy-to-use web application using Streamlit.

---

## ✨ Features

### 📊 Stock Analysis

The Stock Analysis section provides:

* Historical stock price visualization
* Closing price analysis
* Line charts
* Candlestick charts
* RSI (Relative Strength Index)
* MACD (Moving Average Convergence Divergence)
* Historical trading signals
* Interactive Plotly visualizations

### 🔮 Stock Prediction

The Stock Prediction section includes:

* Historical stock data retrieval
* Data preprocessing
* Min-Max scaling
* Time-series sequence generation
* LSTM-based forecasting
* ARIMA-based analysis
* Future stock price prediction
* RMSE-based model evaluation
* Actual vs predicted price visualization

---

## 🧠 Models Used

### 1. LSTM

**Long Short-Term Memory (LSTM)** is a type of recurrent neural network designed for sequential and time-series data.

LSTM was selected because stock prices are sequential observations and the model can learn relationships between previous observations and future values.

The LSTM architecture uses:

* Forget Gate
* Input Gate
* Output Gate
* Cell State

These mechanisms help the model retain relevant information over multiple time steps.

### 2. ARIMA

**ARIMA** stands for:

**AutoRegressive Integrated Moving Average**

It is a statistical time-series forecasting model that combines:

* **AR** – AutoRegressive
* **I** – Integrated
* **MA** – Moving Average

ARIMA was used to analyze the statistical behavior and trends of the time series and to provide a comparison with the LSTM approach.

### Why use both LSTM and ARIMA?

LSTM and ARIMA approach forecasting differently.

* **ARIMA** is a statistical model that works well for analyzing time-series structure.
* **LSTM** is a deep-learning model capable of learning complex sequential relationships.

Using both approaches provides a broader understanding of stock-price behavior and allows their forecasting performance to be compared.

---

## 🔄 Data Preprocessing

The following preprocessing steps are performed before training the LSTM model:

1. Fetch historical stock data from Yahoo Finance.
2. Select the required stock-price feature.
3. Check for missing values.
4. Handle missing observations when required.
5. Scale the data using `MinMaxScaler`.
6. Split the data into training and testing sets.
7. Generate time-series input sequences.
8. Reshape the data into the format required by LSTM.

### LSTM Input Shape

LSTM expects a 3-dimensional input:

```text
(samples, timesteps, features)
```

In this project:

* **Samples** → Number of training examples
* **Timesteps** → Number of previous observations used as input
* **Features** → Number of variables used at each time step

---

## 📏 Model Evaluation

### RMSE

The primary evaluation metric used in the project is **Root Mean Squared Error (RMSE)**.

RMSE measures the difference between actual and predicted values and gives greater importance to larger errors.

A lower RMSE indicates that the predictions are closer to the actual values.

The advantage of RMSE is that it is expressed in the **same unit as the target variable**, making the error easier to interpret.

---

## 📈 Technical Indicators

### RSI

**Relative Strength Index (RSI)** is a momentum indicator used to identify potential overbought and oversold conditions.

Generally:

* RSI above 70 → Potentially overbought
* RSI below 30 → Potentially oversold

RSI is used as an analytical indicator and does not guarantee future price movements.

### MACD

**Moving Average Convergence Divergence (MACD)** is a technical indicator used to analyze trend direction and momentum.

It can also provide potential bullish and bearish signals through MACD and signal-line crossovers.

---

## 📊 Visualizations

The project uses **Plotly** to create interactive visualizations.

### Line Chart

Used to visualize the stock's closing price and identify overall price trends.

### Candlestick Chart

Displays:

* Open price
* High price
* Low price
* Close price

This provides a more detailed view of price movement during a trading period.

### Why Plotly?

Plotly was selected because it provides interactive features such as:

* Hovering
* Zooming
* Panning
* Interactive data exploration

These features are particularly useful in a Streamlit dashboard.

---

## 🖥️ Application Structure

The Streamlit application contains two main sections:

```text
Stock Price Forecasting Application
│
├── 📊 Stock Analysis
│   ├── Historical Data
│   ├── Line Chart
│   ├── Candlestick Chart
│   ├── RSI
│   ├── MACD
│   └── Historical Signals
│
└── 🔮 Stock Prediction
    ├── Data Preprocessing
    ├── LSTM Forecasting
    ├── ARIMA Analysis
    ├── RMSE Evaluation
    └── Future Price Prediction
```

---

## 🛠️ Technologies Used

| Technology             | Purpose                             |
| ---------------------- | ----------------------------------- |
| **Python**             | Programming language                |
| **Pandas**             | Data manipulation and analysis      |
| **NumPy**              | Numerical computations              |
| **yfinance**           | Fetching Yahoo Finance stock data   |
| **Scikit-learn**       | Data preprocessing and evaluation   |
| **TensorFlow / Keras** | LSTM model development              |
| **Statsmodels**        | ARIMA time-series modeling          |
| **Plotly**             | Interactive visualizations          |
| **Streamlit**          | Web application development         |
| **Git & GitHub**       | Version control and project hosting |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the project directory

```bash
cd stock-price-forecasting
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
Stock-Price-Forecasting/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── ...
│
├── notebooks/
│   └── ...
│
└── images/
    └── ...
```

> Adjust the file and folder names above to match your actual GitHub repository structure.

---

## 🔮 Future Improvements

The project can be improved in several ways:

* Include additional features such as Open, High, Low, and Volume.
* Compare LSTM with GRU, Prophet, XGBoost, and other forecasting approaches.
* Perform systematic hyperparameter tuning.
* Add additional technical indicators.
* Integrate financial-news sentiment analysis.
* Improve the Streamlit user interface.
* Add support for comparing multiple stocks.
* Add model-performance comparison dashboards.
* Improve forecasting and validation strategies.

---

## ⚠️ Limitations

The project has some limitations:

1. The prediction primarily relies on historical stock-price information.
2. External factors such as news, market sentiment, economic conditions, and unexpected events are not fully incorporated.
3. Using a limited set of input features may restrict the model's ability to capture all factors affecting stock prices.
4. Stock prices are highly volatile and difficult to predict accurately.
5. Predictions should be considered analytical estimates rather than guaranteed future prices.

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Time-series data analysis
* Data preprocessing
* LSTM-based forecasting
* ARIMA modeling
* Model evaluation
* Technical stock indicators
* Interactive data visualization
* Streamlit application development
* Python programming
* Git and GitHub

---

## 👩‍💻 Author

**Veena Gupta**

B.Tech – Electrical Engineering
National Institute of Technology, Raipur

---

## ⭐ Acknowledgements

* Yahoo Finance for providing historical market data.
* Python open-source libraries used for data analysis, forecasting, visualization, and application development.

---

## 📜 Disclaimer

This project is intended **only for educational and analytical purposes**. Stock market predictions are inherently uncertain. The application does not provide financial advice, and users should not make investment decisions solely based on its predictions.
