from synthesize_me.generate_dd_obs.dataframe.series.guess_data_type import guess_data_type
from synthesize_me.generate_dd_obs.dataframe.series.compute_obs_missing import compute_obs_missing

def make_dd_obs_entry_for_series(series, metadata):


    table_name = metadata['table_name']
    var_name = metadata['var_name']        

    obs_numobs = series.dropna().shape[0]
    obs_distinct = series.dropna().nunique()
    obs_datatype = guess_data_type(series)
    obs_missing = compute_obs_missing(series)


    dd_obs_entry = {
        'table_name': table_name,
        'var_name': var_name,
        'obs_numobs' : obs_numobs,
        'obs_distinct' : obs_distinct,
        'obs_missing' : obs_missing,
        'obs_datatype': obs_datatype,       
    }

    if obs_datatype in ['Integer', 'Decimal']:

        obs_mean = series.mean()
        obs_std = series.std()
        obs_min = series.min()
        obs_p_25 = series.quantile(0.25)
        obs_median = series.median()
        obs_p_75 = series.quantile(0.75)
        obs_max = series.max()

        dd_obs_entry['obs_mean'] = obs_mean
        dd_obs_entry['obs_std'] = obs_std
        dd_obs_entry['obs_min'] = obs_min
        dd_obs_entry['obs_p_25'] = obs_p_25
        dd_obs_entry['obs_median'] = obs_median
        dd_obs_entry['obs_p_75'] = obs_p_75
        dd_obs_entry['obs_max'] = obs_max


    elif obs_datatype in ['StringList', 'NumberList']:
        obs_permissible_values = list(series.dropna().unique())
        obs_permissible_values.sort()
        dd_obs_entry['obs_permissible_values'] = obs_permissible_values
             

    return dd_obs_entry