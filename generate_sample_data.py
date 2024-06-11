import numpy as np
import pandas as pd
import os

def generate_sample_data(output_dir, n=1000, seed=42):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set the seed for reproducibility
    np.random.seed(seed)

    # First CSV File
    # First column: Standard normal distribution
    col1 = np.random.normal(0, 1, n)

    # Second column: Normal distribution with mean 5 and standard deviation 2
    col2 = np.random.normal(5, 2, n)

    # Third column: Exponential distribution with lambda = 1
    col3 = np.random.exponential(1, n)

    # Fourth column: Gamma distribution with shape = 2 and scale = 2
    col4 = np.random.gamma(2, 2, n)

    # Create a DataFrame for the first CSV file
    df1 = pd.DataFrame({
        'Standard_Normal': col1,
        'Normal_Mean5_SD2': col2,
        'Exponential_Lambda1': col3,
        'Gamma_Shape2_Scale2': col4,
    })

    # Save to CSV
    df1.to_csv(os.path.join(output_dir, 'sample1.csv'), index=False)

    # Second CSV File
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

    # Create a DataFrame for the second CSV file
    df2 = pd.DataFrame({
        'Multi_Modal': col5,
        'With_Missing_Data': col6,
        'Uniform_0_10': col7,
        'Beta_Alpha2_Beta5': col10,
        'Log_Normal_Mean0_Sigma1': col11
    })

    # Save to CSV
    df2.to_csv(os.path.join(output_dir, 'sample2.csv'), index=False)

    # Third CSV File
    # Binomial distribution with n = 10 and p = 0.5
    col12 = np.random.binomial(10, 0.5, n)

    # Poisson distribution with lambda = 3
    col13 = np.random.poisson(3, n)    

    # Create a DataFrame for the third CSV file
    df3 = pd.DataFrame({
        'Binomial_n10_p_one_half': col12,
        'Poisson_Lambda3': col13,        
    })

    # Save to CSV
    df3.to_csv(os.path.join(output_dir, 'sample3.csv'), index=False)

    print(f"CSV files 'sample1.csv', 'sample2.csv', and 'sample3.csv' created successfully in {output_dir}.")

if __name__ == '__main__':
    generate_sample_data('example-data/input')
