from .series.decimal import synthesize_decimal_column
from .series.integer import synthesize_integer_column
from .series.numberlist import synthesize_numberlist_column


def synthesize_table_data(df, dd_synth_table):
    # Synthesize data based on the dd_synth_table
    synth_df = df.copy()
    for _, row in dd_synth_table.iterrows():
        var_name = row['var_name']
        if row['datatype'] == 'Decimal':
            synth_df[var_name] = synthesize_decimal_column(
                df[var_name],
                row['dispersion_amount'],
                row['winsorize_lower_limit'],
                row['winsorize_upper_limit'],
                method=row.get('synthesis_method', 'default')
            )
        elif row['datatype'] == 'Integer':
            synth_df[var_name] = synthesize_integer_column(
                df[var_name],
                row['dispersion_amount'],
                row['winsorize_lower_limit'],
                row['winsorize_upper_limit'],
                method=row.get('synthesis_method', 'default')
            )
        elif row['datatype'] == 'NumberList':
            synth_df[var_name] = synthesize_numberlist_column(
                df[var_name],
                row['p_modify_number_list_val'],
                method=row.get('synthesis_method', 'default')
            )
        # Add other data types synthesis as needed

    return synth_df
