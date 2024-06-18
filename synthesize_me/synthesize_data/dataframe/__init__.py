from .series import synthesize_series

def synthesize_table_data(df, dd_synth_table):
    # Synthesize data based on the dd_synth_table
    synth_df = df.copy()

    for _, row in dd_synth_table.iterrows():
        var_name = row['var_name']
        should_be_synthesized = row['should_be_synthesized']

        if should_be_synthesized == 0:
            pass
        else:            
            synth_df[var_name] = synthesize_series(df[var_name], row)       
        

    return synth_df
