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
