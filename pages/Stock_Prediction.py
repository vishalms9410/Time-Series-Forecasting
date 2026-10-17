import streamlit as st
from pages.utils.model_train import get_data , get_rolling_mean ,get_differencing_order , get_forecast, scaling ,evaluate_model,inverse_scaling
import pandas as pd
from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

st.set_page_config(

    page_title = "Stock Prediction",
    page_icon= "chart_with_downwards_trend",
    layout="wide",
)

st.title("Stock Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input('Stock Ticker' ,'AAPL')

rmse =0

st.subheader('Predicting Next 30 days Close Price for: '+ticker)

close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)

differencing_order = get_differencing_order(rolling_price)
scaled_data , scaler = scaling(rolling_price)
rmse = evaluate_model(scaled_data, differencing_order)

st.write("**Model RMSE Score:**", rmse)

# 1. First, generate your forecast array/dataframe
forecast = get_forecast(scaled_data, differencing_order)

# 2. Convert forecast to a DataFrame if it isn't one already, and make it look like rolling_price
import pandas as pd
if not isinstance(forecast, pd.DataFrame):
    forecast = pd.DataFrame(forecast, columns=['Close'])

# 3. Clean up the index of rolling_price to fix the MultiIndex issue
if isinstance(rolling_price.columns, pd.MultiIndex):
    rolling_price.columns = rolling_price.columns.get_level_values(0)

# 4. Standardize column names perfectly across both datasets
rolling_price.columns = ['Close']
forecast.columns = ['Close']

# 5. Reverse the scaling process on the forecast values
forecast['Close'] = inverse_scaling(scaler, forecast['Close'])

rolling_price.index = pd.to_datetime(rolling_price.index).strftime('%Y-%m-%d')
forecast.index = pd.to_datetime(forecast.index).strftime('%Y-%m-%d')

rolling_price.columns = ['Close Price']
forecast.columns = ['Future Close Price']
# 6. Now append the forecast data safely to historical data if you need to
# (or just use forecast directly for your table)

st.write('#### Forecast Data(Next 30 days)')
fig_tail = plotly_table(forecast.sort_index(ascending = True).round(3))
st.plotly_chart(fig_tail,use_container_width=True)
fig_tail.update_layout(height =220)


forecast = pd.concat([rolling_price,forecast])


st.plotly_chart(Moving_average_forecast(forecast.iloc[150:]), use_container_width=True)