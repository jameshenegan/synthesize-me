def compute_obs_missing(series):
    num_missing = series[series.isna()].shape[0]
    prop_missing = num_missing / series.shape[0]
    pct_missing = f'{round(100 * prop_missing, 2)}%'
    obs_missing = f'{num_missing} ({pct_missing})'
    return obs_missing