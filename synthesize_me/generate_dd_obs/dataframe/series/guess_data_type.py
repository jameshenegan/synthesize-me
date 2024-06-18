import pandas as pd
import re

def guess_data_type(curr_col, cat_col_cut=15):
    """
    Guess the data type of a column in a DataFrame.

    Parameters:
    curr_col (pd.Series): The column to analyze.
    cat_col_cut (int): Threshold for unique values to classify as categorical.

    Returns:
    str: The inferred data type.
    """
    dt = pd_dt(curr_col)
    if dt == "object":
        return handle_object(curr_col, cat_col_cut)
    elif dt == "datetime64[ns]":
        return "DateTime"
    else:
        return handle_numeric(curr_col, cat_col_cut)

def pd_dt(curr_col):
    """
    Determine the data type of a column as classified by pandas.

    Parameters:
    curr_col (pd.Series): The column to analyze.

    Returns:
    str: The pandas data type of the column.
    """
    return str(curr_col.dtype)

def handle_object(curr_col, cat_col_cut):
    """
    Handle object-type columns by checking if they are date-like or categorical.

    Parameters:
    curr_col (pd.Series): The column to analyze.
    cat_col_cut (int): Threshold for unique values to classify as categorical.

    Returns:
    str: The inferred data type.
    """
    if is_date_like(curr_col):
        return "DateTime"
    return handle_non_date_object(curr_col, cat_col_cut)

def is_date_like(curr_col):
    """
    Check if a column is date-like by evaluating various date formats.

    Parameters:
    curr_col (pd.Series): The column to analyze.

    Returns:
    bool: True if the column is date-like, False otherwise.
    """
    if curr_col.dtype == "datetime64[ns]":
        return True
    if string_series_is_series_of_blsa_dates(curr_col):
        return True
    if string_series_is_series_of_td_dates(curr_col):
        return True
    if string_series_is_series_of_extended_blsa_dates(curr_col):
        return True
    return False

def handle_non_date_object(curr_col, cat_col_cut):
    """
    Handle non-date object-type columns by determining if they are categorical.

    Parameters:
    curr_col (pd.Series): The column to analyze.
    cat_col_cut (int): Threshold for unique values to classify as categorical.

    Returns:
    str: The inferred data type.
    """
    nunique = curr_col.nunique()
    if nunique <= cat_col_cut:
        return "StringList"
    return "String"

def handle_numeric(curr_col, cat_col_cut):
    """
    Handle numeric-type columns by determining if they are categorical or continuous.

    Parameters:
    curr_col (pd.Series): The column to analyze.
    cat_col_cut (int): Threshold for unique values to classify as categorical.

    Returns:
    str: The inferred data type.
    """
    nunique = curr_col.nunique()
    if nunique <= cat_col_cut:
        return check_number_list(curr_col)
    return handle_non_number_list(curr_col)

def check_number_list(curr_col):
    """
    Check if a numeric column represents a list of numbers.

    Parameters:
    curr_col (pd.Series): The column to analyze.

    Returns:
    str: The inferred data type.
    """
    if all_integers(curr_col):
        return "NumberList"
    return "DecimalList"

def handle_non_number_list(curr_col):
    """
    Handle non-number list numeric-type columns by determining if they are integer or decimal.

    Parameters:
    curr_col (pd.Series): The column to analyze.

    Returns:
    str: The inferred data type.
    """
    if all_integers(curr_col):
        return "Integer"
    return "Decimal"

def all_integers(curr_col):
    """
    Check if all entries of a numeric column are integers.

    Parameters:
    curr_col (pd.Series): The column to analyze.

    Returns:
    bool: True if all values are integers, False otherwise.
    """
    return curr_col.dropna().apply(lambda x: float(x).is_integer()).all()

def num_expected_obs(curr_col):
    """
    Calculate the number of expected observations in the column.

    Parameters:
    curr_col (pd.Series): The column to analyze.

    Returns:
    int: The number of observations.
    """
    return len(curr_col)

def num_missing_obs(curr_col):
    """
    Calculate the number of missing observations in the column.

    Parameters:
    curr_col (pd.Series): The column to analyze.

    Returns:
    int: The number of missing observations.
    """
    return curr_col.isna().sum()

def string_series_is_series_of_blsa_dates(series):
    """
    Check if a series consists entirely of BLSA date strings (YYYY-MM-DD).

    Parameters:
    series (pd.Series): The series to analyze.

    Returns:
    bool: True if all values match the BLSA date pattern, False otherwise.
    """
    no_missing = series.dropna()
    num_in_series = no_missing.shape[0]
    num_matching_blsa_date_pattern = no_missing.apply(lambda x: string_is_blsa_date(x)).sum()
    return num_matching_blsa_date_pattern == num_in_series

def string_series_is_series_of_extended_blsa_dates(series):
    """
    Check if a series consists entirely of extended BLSA date strings (YYYY-MM-DD HH:MM:SS).

    Parameters:
    series (pd.Series): The series to analyze.

    Returns:
    bool: True if all values match the extended BLSA date pattern, False otherwise.
    """
    no_missing = series.dropna()
    num_in_series = no_missing.shape[0]
    num_matching_blsa_date_pattern = no_missing.apply(lambda x: string_is_extended_blsa_date(x)).sum()
    return num_matching_blsa_date_pattern == num_in_series

def string_series_is_series_of_td_dates(series):
    """
    Check if a series consists entirely of Stata TD date strings (e.g., 01mar2020).

    Parameters:
    series (pd.Series): The series to analyze.

    Returns:
    bool: True if all values match the TD date pattern, False otherwise.
    """
    no_missing = series.dropna()
    num_in_series = no_missing.shape[0]
    num_matching_td_date_pattern = no_missing.apply(lambda x: string_is_stata_td_date(x)).sum()
    return num_matching_td_date_pattern == num_in_series

def string_is_blsa_date(string):
    """
    Check if a string matches the BLSA date pattern (YYYY-MM-DD).

    Parameters:
    string (str): The string to check.

    Returns:
    bool: True if the string matches the BLSA date pattern, False otherwise.
    """
    blsa_date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(blsa_date_pattern.match(str(string)))

def string_is_extended_blsa_date(string):
    """
    Check if a string matches the extended BLSA date pattern (YYYY-MM-DD HH:MM:SS).

    Parameters:
    string (str): The string to check.

    Returns:
    bool: True if the string matches the extended BLSA date pattern, False otherwise.
    """
    extended_blsa_date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')
    return bool(extended_blsa_date_pattern.match(str(string)))

def string_is_stata_td_date(string):
    """
    Check if a string matches the Stata TD date pattern (e.g., 01mar2020).

    Parameters:
    string (str): The string to check.

    Returns:
    bool: True if the string matches the Stata TD date pattern, False otherwise.
    """
    string = str(string)
    list_of_months = ['mar', 'jan', 'may', 'nov', 'dec', 'aug', 'oct', 'sep', 'jun', 'jul', 'feb', 'apr']
    
    if len(string) != 9:
        return False
    if not re.compile(r'^\d{2}').match(string[:2]):
        return False
    if not string[2:5] in list_of_months:
        return False
    if not re.compile(r'\d{4}$').match(string[-4:]):
        return False
    
    return True

