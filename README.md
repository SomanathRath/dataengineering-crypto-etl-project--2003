# dataengineering-crypto-etl-project--2003
# Crypto ETL Project

A project for ETL pipeline development and crypto price analysis. This repository demonstrates extracting, transforming, and loading cryptocurrency price data, with Python scripts and a Streamlit dashboard for visualization.

## Table of Contents

- [Project Overview](#project-overview)
- [Files Included](#files-included)
- [Setup Instructions](#setup-instructions)
- [Usage Guide](#usage-guide)
- [Database Schema](#database-schema)
- [Dashboard Preview](#dashboard-preview)
- [License](#license)

## Project Overview

This project builds a basic ETL pipeline to work with cryptocurrency price data. The included SQLite database stores crypto prices with time stamps, and Python scripts clean, transform, and analyze the data. The dashboard.py script provides an interactive visualization using Streamlit.

## Files Included

- `crypto_data.db`: SQLite database storing price and timestamp per cryptocurrency.
- `dashboard.py`: Streamlit code for displaying/visualizing data.
- `etl_script.py`: Main script for extraction, transformation, and loading.
- `requirements.txt`: List of Python dependencies.
- `test_mysql_connection.py`: Script for verifying database connectivity.

## Setup Instructions

1. Clone this repository.
2. Install requirements:
3. Ensure `crypto_data.db` is in your working directory.

## Usage Guide

- Use `etl_script.py` to process data and update the database.
- Run `dashboard.py` to view results and plots via Streamlit.
- `test_mysql_connection.py` can help confirm database connection settings.

## Database Schema

- **Table Name:** `crypto_prices`
- **Columns:**
- `crypto` (TEXT): Name/symbol of cryptocurrency.
- `price_usd` (REAL): Price in US dollars.
- `timestamp` (TEXT): Timestamp for data record.

## Dashboard Preview

Below is a screenshot of the live dashboard built with Streamlit:

![Dashboard](visualisation.jpg)

## License

This project is licensed under the MIT License—see the LICENSE file for details.
