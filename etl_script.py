import requests
import mysql.connector
from datetime import datetime

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 10, 'page': 1, 'sparkline': 'false'}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def load_data_to_mysql(data):
    connection = mysql.connector.connect(
        host='localhost',
        user='soma',
        password='Soma@1234',
        database='etl_db'
    )
    cursor = connection.cursor()

    for coin in data:
        cursor.execute("""
            INSERT INTO crypto_data (id, symbol, name, current_price, market_cap, total_volume, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                current_price=VALUES(current_price),
                market_cap=VALUES(market_cap),
                total_volume=VALUES(total_volume),
                last_updated=VALUES(last_updated)
        """, (
            coin['id'], coin['symbol'], coin['name'], coin['current_price'],
            coin['market_cap'], coin['total_volume'],
            datetime.strptime(coin['last_updated'], "%Y-%m-%dT%H:%M:%S.%fZ")
        ))

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    crypto_data = fetch_crypto_data()
    load_data_to_mysql(crypto_data)
    print("ETL job completed successfully.")
