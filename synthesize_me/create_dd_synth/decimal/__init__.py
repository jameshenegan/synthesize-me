def handle_decimal(row, blanket_default_params):
    """
    Handle the synthesis parameters for decimal data types.

    Parameters:
    - row: pd.Series
        The row from dd_obs.
    - blanket_default_params: dict
        Default parameters for dispersion and winsorization.

    Returns:
    - dict
        The synthesized row dictionary.
    """
    iqr = row['obs_p_75'] - row['obs_p_25']
    dispersion_amount = blanket_default_params['dispersion_factor'] * iqr
    winsorize_lower_limit = blanket_default_params['winsorize_lower_limit']
    winsorize_upper_limit = blanket_default_params['winsorize_upper_limit']

    return {
        'table_name': row['table_name'],
        'var_name': row['var_name'],
        'datatype': 'Decimal',
        'dispersion_amount': dispersion_amount,
        'winsorize_lower_limit': winsorize_lower_limit,
        'winsorize_upper_limit': winsorize_upper_limit
    }