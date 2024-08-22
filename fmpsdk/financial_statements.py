import typing
import os
import requests
import logging
from .settings import (
    FINANCIAL_STATEMENT_FILENAME,
    INCOME_STATEMENT_FILENAME,
    BALANCE_SHEET_STATEMENT_FILENAME,
    CASH_FLOW_STATEMENT_FILENAME,
    INCOME_STATEMENT_AS_REPORTED_FILENAME,
    BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
    DEFAULT_LIMIT,
    BASE_URL_v3,
)
from .url_methods import __return_json_v3, __validate_period
from .data_compression import compress_json_to_tuples

API_KEY = os.getenv('FMP_API_KEY')


def income_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Retrieve income statement data for a company.

    Provides real-time access to a company's revenue, expenses, and net income.
    Useful for tracking profitability, comparing with competitors, and
    identifying business trends. 

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of statements to retrieve. Default is 10.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is INCOME_STATEMENT_FILENAME.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with income statement data, or None if download is True.
    :example: income_statement('AAPL', period='quarter', limit=5, download=True)
    """
    path = f"income-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def balance_sheet_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Retrieve balance sheet data for a company.

    Provides real-time access to a company's assets, liabilities, and equity.
    Useful for assessing financial health, identifying risks, and analyzing
    debt levels, cash flow, and equity position. 

    :param symbol: Company ticker (e.g., 'AAPL') or CIK (e.g., '0000320193').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of statements to retrieve. Default is 10.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is BALANCE_SHEET_STATEMENT_FILENAME.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with balance sheet data, or None if download is True.
    :example: balance_sheet_statement('AAPL', period='quarter', limit=5, download=True)
    """
    path = f"balance-sheet-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} balance sheet statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def cash_flow_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Retrieve cash flow statement data for a company.

    Provides real-time access to a company's cash inflows and outflows,
    categorized into operating, investing, and financing activities.
    Useful for assessing cash management, liquidity, and financial health.

    :param symbol: Company ticker (e.g., 'AAPL') or CIK (e.g., '0000320193').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of statements to retrieve. Default is 10.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is CASH_FLOW_STATEMENT_FILENAME.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with cash flow data, or None if download is True.
    :example: cash_flow_statement('AAPL', period='quarter', limit=5, download=True)
    """
    path = f"cash-flow-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def income_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_AS_REPORTED_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /income-statement-as-reported/ API for company's as-reported income statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is INCOME_STATEMENT_AS_REPORTED_FILENAME.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with as-reported income statement data, or None if download is True.
    :example: income_statement_as_reported('AAPL', period='quarter', limit=5, download=True)
    """
    path = f"income-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def balance_sheet_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /balance-sheet-statement-as-reported/ API for company's as-reported balance sheet.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with as-reported balance sheet data, or None if download is True.
    :example: balance_sheet_statement_as_reported('AAPL', period='quarter', limit=5, download=True)
    """
    path = f"balance-sheet-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def cash_flow_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /cash-flow-statement-as-reported/ API for company's as-reported cash flow statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with as-reported cash flow data, or None if download is True.
    :example: cash_flow_statement_as_reported('AAPL', period='quarter', limit=5, download=True)
    """
    path = f"cash-flow-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def financial_statement_full_as_reported(
    symbol: str,
    period: str = "annual",
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /financial-statement-full-as-reported/ API for company's full as-reported financial statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with full as-reported financial statement data.
    :example: financial_statement_full_as_reported('AAPL', period='quarter')
    """
    path = f"financial-statement-full-as-reported/{symbol}"
    query_vars = {"apikey": API_KEY, "period": __validate_period(value=period)}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)