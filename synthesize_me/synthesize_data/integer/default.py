from synthesize_me.synthesize_data.decimal.default import synthesize_default_decimal

def synthesize_default_integer(series, dispersion_amount, winsorize_lower_limit, winsorize_upper_limit):
    return synthesize_default_decimal(series, dispersion_amount, winsorize_lower_limit, winsorize_upper_limit).round()
    