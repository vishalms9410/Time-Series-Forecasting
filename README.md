
# 📈 Stock Price Forecasting Using LSTM & ARIMA

An interactive stock market analysis and forecasting application built with **Python, Streamlit, LSTM, ARIMA, and Plotly**. The application combines time-series forecasting techniques with interactive financial visualizations to explore historical stock price movements and estimate potential future trends.

> **Disclaimer:** This project is intended for educational and analytical purposes only. Forecasts are estimates, not guarantees of future performance or investment advice.

## ✨ Key Features

### 📊 Stock Market Analysis

- Analyze historical stock market data retrieved from Yahoo Finance.
- Visualize closing prices and historical price trends.
- Explore interactive line and candlestick charts.
- Analyze market momentum using RSI and MACD indicators.
- Examine historical trading signals.

### 🔮 Stock Price Forecasting

- Retrieve and preprocess historical stock data.
- Scale numerical data using Min-Max normalization.
- Generate sequential input data for time-series modeling.
- Apply **LSTM** for sequence-based price forecasting.
- Use **ARIMA** for statistical time-series analysis.
- Evaluate forecasting performance using Root Mean Squared Error (RMSE).
- Visualize actual and predicted stock prices.

### 📈 Interactive Visualization

- Explore financial data using interactive Plotly charts.
- Zoom, pan, and inspect historical price movements.
- Analyze market behavior through technical indicators.

## 🧠 Forecasting Models

### 1. Long Short-Term Memory (LSTM)

LSTM is a type of recurrent neural network designed to learn patterns in sequential data. It uses memory cells and gating mechanisms to control the information retained across time steps.

In this project, LSTM is used to learn patterns from historical stock price sequences and generate forecasts.

### 2. AutoRegressive Integrated Moving Average (ARIMA)

ARIMA is a statistical forecasting model that combines autoregression, differencing, and moving averages.

- **AR — Autoregression:** Models relationships between current observations and previous observations.
- **I — Integration:** Uses differencing to help achieve stationarity.
- **MA — Moving Average:** Models relationships between observations and past forecast errors.

ARIMA provides a statistical approach to analyzing and forecasting time-series data.

### Why LSTM and ARIMA?

LSTM can learn nonlinear sequential patterns, while ARIMA models statistical relationships in time-series data under its assumptions.

Using both provides an opportunity to compare different forecasting approaches. However, neither model guarantees accurate predictions in volatile financial markets.

## 🔄 Data Processing Workflow

1. **Data Collection:** Retrieve historical market data from Yahoo Finance.
2. **Data Preparation:** Select the required price series and inspect missing observations.
3. **Normalization:** Scale input data using Min-Max scaling.
4. **Sequence Generation:** Construct time-series windows for LSTM.
5. **Modeling:** Apply LSTM and ARIMA forecasting techniques.
6. **Evaluation:** Measure prediction errors using RMSE.
7. **Visualization:** Present historical data and forecasting results through interactive charts.

### LSTM Input Representation

LSTM models generally expect sequential input in the following format:

`(samples, timesteps, features)`

- **Samples:** Number of training sequences.
- **Timesteps:** Number of observations in each sequence.
- **Features:** Number of variables supplied at each time step.

## 📏 Model Evaluation

### Root Mean Squared Error (RMSE)

RMSE measures the magnitude of prediction errors by calculating the square root of the mean of squared differences between actual and predicted values.

\[
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
\]

Where:

- \(y_i\) represents an actual value.
- \(\hat{y}_i\) represents a predicted value.
- \(n\) represents the number of evaluated observations.

A lower RMSE generally indicates smaller prediction errors on the evaluated dataset. Comparisons should use the same target variable, scale, and evaluation period.

## 📉 Technical Indicators

| Indicator | Purpose |
|---|---|
| RSI (Relative Strength Index) | Evaluates price momentum and potential overbought or oversold conditions. |
| MACD (Moving Average Convergence Divergence) | Helps analyze trend direction and momentum. |
| Candlestick Chart | Displays open, high, low, and close prices. |
| Line Chart | Illustrates historical price movements and trends. |

Technical indicators provide analytical signals, not certain predictions of future market behavior.

## 🛠️ Technology Stack

| Technology | Role |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computation |
| yfinance | Historical stock market data retrieval |
| Scikit-learn | Data preprocessing and evaluation utilities |
| TensorFlow / Keras | LSTM model development |
| Statsmodels | ARIMA time-series modeling |
| Plotly | Interactive financial visualizations |
| Git & GitHub | Version control and source-code hosting |

## 📁 Project Structure

```text
Time-Series-Forecasting/
│
├── .vscode/
│   └── settings.json
│
├── pages/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── model_train.py
│   │   └── plotly_figure.py
│   │
│   ├── Stock_Analysis.py
│   └── Stock_Prediction.py
│
├── app.png
├── Trading_App.py
├── README.md
└── SOURCES.txt
```

### Main Components

- **`Trading_App.py`** — Main application entry point.
- **`pages/Stock_Analysis.py`** — Stock analysis page.
- **`pages/Stock_Prediction.py`** — Stock forecasting page.
- **`pages/utils/model_train.py`** — Model training and forecasting utilities.
- **`pages/utils/plotly_figure.py`** — Plotting utilities for interactive visualizations.
- **`app.png`** — Application image asset.

## 🚀 Getting Started

### Prerequisites

- Python installed on your system.
- Git installed on your system.
- An internet connection to retrieve stock market data.

### 1. Clone the Repository

```bash
git clone https://github.com/vishalms9410/Time-Series-Forecasting.git
cd Time-Series-Forecasting
```

Replace `vishalms9410` with the GitHub username hosting your repository.

### 2. Create a Virtual Environment

**Windows CMD:**

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

If a `requirements.txt` file is available:

```cmd
pip install -r requirements.txt
```

Otherwise, install the likely dependencies based on the project implementation:

```cmd
pip install streamlit pandas numpy yfinance scikit-learn tensorflow statsmodels plotly
```

Package versions may need adjustment to match your Python version and the project's implementation.

### 4. Run the Application

```cmd
streamlit run Trading_App.py
```

Streamlit should display a local URL in the terminal, typically:

`http://localhost:8501`

Open that URL in your browser to access the application.

## 🔮 Potential Improvements

- Compare LSTM and ARIMA forecasts using consistent out-of-sample evaluation.
- Experiment with additional models such as GRU, Prophet, and XGBoost.
- Incorporate volume, market indices, and other relevant features.
- Add systematic hyperparameter tuning.
- Improve time-series validation and prevent data leakage.
- Support comparisons across multiple stocks.
- Add forecasting-performance dashboards and prediction intervals.
- Explore financial-news sentiment analysis.

## ⚠️ Limitations

- Historical prices alone cannot capture every factor affecting financial markets.
- Market news, macroeconomic events, and investor sentiment may influence prices unexpectedly.
- Model performance can vary across stocks and time periods.
- Random train-test splitting can cause data leakage in time-series problems; chronological validation is generally more appropriate.
- Good historical performance does not guarantee future forecasting accuracy.

## 🎯 Learning Outcomes

This project provides practical exposure to:

- Time-series analysis and forecasting.
- LSTM-based deep learning and statistical ARIMA modeling.
- Financial data collection and preprocessing.
- Technical indicators and exploratory data analysis.
- Forecast evaluation using RMSE.
- Interactive dashboard development with Streamlit and Plotly.
- Python project organization and Git-based version control.

## 👨‍💻 Author

**Vishal Chaudhary**  
B.Tech
National Institute of Technology, Raipur

## 🙏 Acknowledgements

- [Yahoo Finance](https://finance.yahoo.com/) for historical market data access through available data interfaces.
- The Python open-source ecosystem for data analysis, forecasting, and visualization tools.

---

**Disclaimer:** This application is for educational and analytical purposes only. It does not provide financial advice. Always conduct independent research before making investment decisions.
