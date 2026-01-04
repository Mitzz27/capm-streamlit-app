import streamlit as st

st.set_page_config(
    page_title="Trading App",
    page_icon="heavy_dollar_sign:",
    layout='wide' )

st.title('Trading Guide App:bar_chart:')
st.header('We provide Best platform for you to collect all information prior to investing in stocks. ')
st.image('app.png')
st.markdown("## We provide the following Services:")

st.markdown("#### :one: Stock Information")
st.write('Through this page you can see all information about stock. ')

st.markdown("#### :two: Stock Prediction")
st.write('You can explore Predicted Closing price for next 30 days based on historical stock data and advance Forecasting Models. ')

st.markdown("#### :three: CAPM Return")
st.write('Discover how the Capital Asset Pricing Model (CAPM) calculates the expected returns of different stocks asset based on its risk and market Performance. ')

st.markdown("#### :four: CAPM Beta")
st.write('Calculates Beta and expected returns for individual stocks. ')