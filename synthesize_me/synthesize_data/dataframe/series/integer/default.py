from synthesize_me.synthesize_data.dataframe.series.decimal.add_normal_noise import add_normal_noise

def synthesize_default_integer(series, dispersion_amount, winsorize_lower_limit, winsorize_upper_limit):
    return add_normal_noise(series, dispersion_amount).round()
    