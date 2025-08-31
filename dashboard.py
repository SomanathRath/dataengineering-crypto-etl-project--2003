import streamlit as st
import mysql.connector
import pandas as pd

def get_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='soma',
        password='Soma@1234',
        database='etl_db'
    )
    query = "SELECT * FROM crypto_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("Crypto Prices Dashboard")
df = get_data()
st.dataframe(df)

st.line_chart(df.set_index('last_updated')['current_price'])
