import numpy as np
import pandas as pd
import os
import argparse
import logging

def generate_normal_like_int(n):
    """Generate a normal-like distribution of integers."""
    data = np.random.normal(0, 1, n)
    data = (data - data.min()) / (data.max() - data.min()) * 100
    return data.astype(int)

def generate_left_heavy_int(n):
    """Generate a left heavy distribution of integers."""
    data = np.random.chisquare(df=2, size=n)
    data = (data - data.min()) / (data.max() - data.min()) * 100
    return data.astype(int)

def generate_right_heavy_int(n):
    """Generate a right heavy distribution of integers."""
    data = -np.random.chisquare(df=2, size=n)
    data = (data - data.min()) / (data.max() - data.min()) * 100
    return data.astype(int)

def generate_multi_modal_int(n):
    """Generate a multi-modal distribution of integers."""
    data1 = np.random.normal(-2, 0.5, n // 2)
    data2 = np.random.normal(3, 0.5, n // 2)
    data = np.concatenate([data1, data2])
    data = (data - data.min()) / (data.max() - data.min()) * 100
    return data.astype(int)

def generate_uniform_int(n):
    """Generate a uniform distribution of integers."""
    data = np.random.uniform(0, 100, n)
    return data.astype(int)

def generate_sample1(n):
    """
    Generate the first sample data set.

    Parameters:
    n (int): Number of samples to generate for each column.

    Returns:
    pd.DataFrame: DataFrame containing the first sample data set.
    """
    # First column: Standard normal distribution
    col1 = np.random.normal(0, 1, n)

    # Second column: Normal distribution with mean 5 and standard deviation 2
    col2 = np.random.normal(5, 2, n)

    # Third column: Exponential distribution with lambda = 1
    col3 = np.random.exponential(1, n)

    # Fourth column: Gamma distribution with shape = 2 and scale = 2
    col4 = np.random.gamma(2, 2, n)

    # New columns
    normal_like_int = generate_normal_like_int(n)
    left_heavy_int = generate_left_heavy_int(n)

    df_sample1 = pd.DataFrame({
        'Standard_Normal': col1,
        'Normal_Mean5_SD2': col2,
        'Exponential_Lambda1': col3,
        'Gamma_Shape2_Scale2': col4,
        'Normal_Like_Int': normal_like_int,
        'Left_Heavy_Int': left_heavy_int,

    })

    df_sample1 = df_sample1.reset_index()    
    df_sample1 = df_sample1.rename(columns={"index" : "id_number"})
    
    return df_sample1

def generate_sample2(n):
    """
    Generate the second sample data set.

    Parameters:
    n (int): Number of samples to generate for each column.

    Returns:
    pd.DataFrame: DataFrame containing the second sample data set.
    """
    # Fifth column: Multi-modal distribution (combination of two normal distributions)
    col5 = np.concatenate([np.random.normal(-2, 0.5, n // 2), np.random.normal(3, 0.5, n // 2)])

    # Sixth column: Contains some missing data (10% missing)
    col6 = np.random.normal(0, 1, n)
    col6[np.random.choice(n, size=n//10, replace=False)] = np.nan

    # Seventh column: Uniform distribution between 0 and 10
    col7 = np.random.uniform(0, 10, n)

    # Tenth column: Beta distribution with alpha = 2 and beta = 5
    col10 = np.random.beta(2, 5, n)

    # Eleventh column: Log-normal distribution with mean 0 and sigma 1
    col11 = np.random.lognormal(0, 1, n)

    # New columns    
    right_heavy_int = generate_right_heavy_int(n)
    multi_modal_int = generate_multi_modal_int(n)    

    df_sample2 = pd.DataFrame({
        'Multi_Modal': col5,
        'With_Missing_Data': col6,
        'Uniform_0_10': col7,
        'Beta_Alpha2_Beta5': col10,
        'Log_Normal_Mean0_Sigma1': col11,      
        'Right_Heavy_Int': right_heavy_int,
        'Multi_Modal_Int': multi_modal_int,
    })

    df_sample2 = df_sample2.reset_index()    
    df_sample2 = df_sample2.rename(columns={"index" : "id_number"})

    return df_sample2

def generate_sample3(n):
    """
    Generate the third sample data set.

    Parameters:
    n (int): Number of samples to generate for each column.

    Returns:
    pd.DataFrame: DataFrame containing the third sample data set.
    """
    # Binomial distribution with n = 10 and p = 0.5
    col12 = np.random.binomial(10, 0.5, n)

    # Poisson distribution with lambda = 3
    col13 = np.random.poisson(3, n)

    # New columns    
    uniform_int = generate_uniform_int(n)

    df_sample3 = pd.DataFrame({
        'Binomial_n10_p_one_half': col12,
        'Poisson_Lambda3': col13,
        'Uniform_Int': uniform_int
    })


    df_sample3 = df_sample3.reset_index()    
    df_sample3 = df_sample3.rename(columns={"index" : "id_number"})

    return df_sample3

def save_csv(df, output_dir, filename):
    """
    Save the DataFrame to a CSV file.

    Parameters:
    df (pd.DataFrame): DataFrame to save.
    output_dir (str): Directory where the CSV file will be saved.
    filename (str): Name of the CSV file.
    """
    filepath = os.path.join(output_dir, filename)
    df.to_csv(filepath, index=False)
    logging.info(f"CSV file '{filename}' created successfully in {output_dir}.")

def generate_sample_data(output_dir, n=1000, seed=42):
    """
    Generate sample CSV files with synthetic data.

    Parameters:
    output_dir (str): Directory where the generated CSV files will be saved.
    n (int): Number of samples to generate for each column. Default is 1000.
    seed (int): Seed for the random number generator. Default is 42.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set the seed for reproducibility
    np.random.seed(seed)

    # Generate and save the sample data sets
    save_csv(generate_sample1(n), output_dir, 'sample1.csv')
    save_csv(generate_sample2(n), output_dir, 'sample2.csv')
    save_csv(generate_sample3(n), output_dir, 'sample3.csv')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate sample CSV files with synthetic data.')
    parser.add_argument('output_dir', type=str, help='Directory where the generated CSV files will be saved.')
    parser.add_argument('--n', type=int, default=1000, help='Number of samples to generate for each column.')
    parser.add_argument('--seed', type=int, default=42, help='Seed for the random number generator.')

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    generate_sample_data(args.output_dir, n=args.n, seed=args.seed)
