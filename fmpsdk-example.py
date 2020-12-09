#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = os.environ.get("apikey")
symbol = "AAPL"

# Access the FMPSDK methods.  Most return a List of Dictionaries.

# Company Valuation Methods
print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)}")
# print(f"Company Quote: {fmpsdk.quote(apikey=apikey, symbol=symbol)}")
# print(f"Multiple Company Quotes: {fmpsdk.quote(apikey=apikey, symbol=['AAPL', 'CSCO', 'QQQQ'])}")
# print(f"Key Executives: {fmpsdk.key_executives(apikey=apikey, symbol=symbol)}")
# print(f"Search: {fmpsdk.search(apikey=apikey, query='AA', exchange='NYSE', limit=10)}")
# print(f"Ticker Search: {fmpsdk.search_ticker(apikey=apikey, query='AA', exchange='NYSE', limit=5)}")
# fmpsdk.financial_statement(apikey=apikey, symbol=symbol)
# print(f"Annual Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol)}")
# print(f"Quarterly Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol, period='quarter')}")
# fmpsdk.income_statement(apikey=apikey, symbol=symbol, download=True)
# print(f"Annual Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol)}")
# print(f"Quarterly Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, period='quarter')}")
# fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, download=True)
# print(f"Annual Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, )}")
# print(f"Quarterly Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, period='quarter')}")
# fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, download=True)
# print(f"Financial Statement Symbols List: {fmpsdk.financial_statement_symbol_lists(apikey=apikey)}")
# print(f"Income Statement Growth: {fmpsdk.income_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
# print(f"Balance Sheet Statement Growth: {fmpsdk.balance_sheet_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
# print(f"Cash Flow Statement Growth: {fmpsdk.cash_flow_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
# print(f"Annual Income Statement as Reported : {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol)}")
# print(f"Quarterly Income Statement as Reported: {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
# fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
# print(f"Annual Balance Sheet Statement as Reported : {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol)}")
# print(f"Quarterly Balance Sheet Statement as Reported: {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
# fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
# print(f"Annual Cash Flow Statement as Reported : {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol)}")
# print(f"Quarterly Cash Flow Statement as Reported: {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
# fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
# print(f"Annual Full Financial Statement as Reported : {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol)}")
# print(f"Quarterly Full Financial Statement as Reported: {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
# print(f"Financial Ratios (TTM): {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period='ttm')}")
# print(f"Annual Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period='annual')}")
# print(f"Quarterly Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period='quarter')}")
# print(f"Annual Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol)}")
# print(f"Quarterly Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol, period='quarter')}")
# print(f"Key Metrics (TTM): {fmpsdk.key_metrics(apikey=apikey, symbol=symbol, period='ttm')}")
# print(f"Annual Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol, period='annual')}")
# print(f"Quarterly Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol, period='quarter')}")
# print(f"Annual Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol, period='annual')}")
# print(f"Quarterly Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol, period='quarter')}")
# print(f"Company Rating: {fmpsdk.rating(apikey=apikey, symbol=symbol)}")
# print(f"Historical Company Rating: {fmpsdk.historical_rating(apikey=apikey, symbol=symbol, limit=10)}")
# print(f"Discounted Cash Flow: {fmpsdk.discounted_cash_flow(apikey=apikey, symbol=symbol)}")
# print(f"Annual Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol, period='annual')}")
# print(f"Quarterly Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol, period='quarter')}")
# print(f"Daily Historical Discounted Cash Flow: {fmpsdk.historical_daily_discounted_cash_flow(apikey=apikey, symbol=symbol)}")
# print(f"Market Capitalization: {fmpsdk.market_capitalization(apikey=apikey, symbol=symbol)}")
# print(f"Historical Market Capitalization: {fmpsdk.historical_market_capitalization(apikey=apikey, symbol=symbol, limit=10)}")
# print(f"Symbols List: {fmpsdk.symbols_list(apikey=apikey)}")
# print(f"Stock Screener: {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=1000000000, beta_more_than=1, volume_more_than=10000, sector='Technology', exchange='NASDAQ', dividend_more_than=0, limit=100)}")
# print(f"Stock Screener: {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=1000000000, beta_more_than=1, volume_more_than=10000, sector='Technology', industry='Software', exchange='NASDAQ', dividend_more_than=0, limit=100)}")
# print(f"Stock Screener: {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=10000000000, beta_more_than=1, volume_more_than=100, exchange=['NYSE', 'NASDAQ'])}")
# print(f"Delisted Companies: {fmpsdk.delisted_companies(apikey=apikey, limit=10)}")
# print(f"Stock News (Single): {fmpsdk.stock_news(apikey=apikey, tickers=symbol)}")
# print(f"Stock News (Multiple): {fmpsdk.stock_news(apikey=apikey, tickers=['AAPL', 'CSCO', 'QQQQ'])}")
# print(f"Stock News (Latest): {fmpsdk.stock_news(apikey=apikey, limit=10)}")
# print(f"Earnings Surprises: {fmpsdk.earnings_surprises(apikey=apikey, symbol=symbol)}")
# print(f"SEC Filings: {fmpsdk.sec_filings(apikey=apikey, symbol=symbol, filing_type='10-K')}")
# print(f"Press Releases: {fmpsdk.press_releases(apikey=apikey, symbol=symbol)}")

# Calendars
# print(f"Earning Calendar: {fmpsdk.earning_calendar(apikey=apikey)}")
# print(f"Earning Calendar: {fmpsdk.earning_calendar(apikey=apikey, from_date='2000-06-23', to_date='2010-12-12')}")

# Stock Time Series Methods
# print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)}")
# print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)}")
