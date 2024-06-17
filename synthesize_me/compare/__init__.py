import os
import matplotlib.pyplot as plt


def generate_comparison_plots(original_df, synth_df, dd_synth_table, output_folder):
    """
    Generate comparison plots between original and synthesized data.

    Parameters:
    original_df (pd.DataFrame): Original data DataFrame.
    synth_df (pd.DataFrame): Synthesized data DataFrame.
    dd_synth_table (pd.DataFrame): DataFrame with synthesis instructions for the current table.
    output_folder (str): Directory where the comparison plots will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for _, row in dd_synth_table.iterrows():
        var_name = row['var_name']
        datatype = row['datatype']
        
        # Generate comparison plots for Decimal variables
        if datatype in ['Decimal', 'Integer']:
            plt.figure(figsize=(10, 6))
            plt.scatter(original_df[var_name], synth_df[var_name], alpha=0.5)
            plt.title(f'Comparison of Original and Synthesized Data for {var_name}')
            plt.xlabel('Original Data')
            plt.ylabel('Synthesized Data')
            plt.plot([original_df[var_name].min(), original_df[var_name].max()], 
                     [original_df[var_name].min(), original_df[var_name].max()], color='red', linestyle='--')
            plt.grid(True)
            plt.savefig(os.path.join(output_folder, f'comparison_{var_name}.png'))
            plt.close()

        # Generate other plots as needed for different data types
        
        
        

def compare_number_list_vars_for_table(original_df, synth_df, table_name, dd_synth_table):
    
    aggregated_number_list_comparison_metadata = []

    for _, row in dd_synth_table.iterrows():
        var_name = row['var_name']
        datatype = row['datatype']

        if datatype in ['NumberList']:
            original_series = original_df[var_name]
            synth_series = synth_df[var_name]
            num_original_vals = len(original_series.dropna())
            num_synth_vals = len(synth_series.dropna())
            num_matches = (original_series == synth_series).sum()

            number_list_comparison_metadata = {
                "table_name" : table_name,
                "var_name": var_name,
                "datatype" : datatype,
                "num_original_vals" : num_original_vals,
                "num_synth_vals" : num_synth_vals,
                "num_matches" : num_matches,
                "prop_matches" : num_matches / num_original_vals,
            }
            
            aggregated_number_list_comparison_metadata.append(number_list_comparison_metadata)
            
        
    return aggregated_number_list_comparison_metadata