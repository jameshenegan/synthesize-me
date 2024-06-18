# Synthesize-ME

## Introduction

The `synthesize_me` Python package generates synthetic versions of CSV files, allowing researchers and developers to create realistic data for testing and development without exposing sensitive information.

Given:

- a path to an input folder of CSV files, and
- a path to an empty output folder,

`synthesize_me` will generate synthetic versions of the CSV files in the input folder and write them to disk in the output folder. Optionally, users can fine-tune aspects of the synthetic data generation process to suit their specific needs.

## Fine-Tuning with `dd_synth`

The `dd_synth` DataFrame allows users to fine-tune aspects of the synthetic data generation process. It serves as both

- a data dictionary for the tables and variables in the input folder and
- a set of synthesis instructions for creating the tables and variables in the output folder.

### Structure of `dd_synth`

Here's an example of what a `dd_synth` might look like:

| table_name | var_name                | should_be_synthesized | datatype   | method                     | dispersion_amount | winsorize_lower_limit | winsorize_upper_limit | p_modify_number_list_val |
| ---------- | ----------------------- | --------------------- | ---------- | -------------------------- | ----------------- | --------------------- | --------------------- | ------------------------ |
| sample1    | id_number               | 0                     | Integer    | add_normal_noise_and_round | 12.475            | 0.05                  | 0.95                  |                          |
| sample1    | Standard_Normal         | 1                     | Decimal    | add_normal_noise           | 0.068             | 0.05                  | 0.95                  |                          |
| sample1    | Normal_Mean5_SD2        | 1                     | Decimal    | add_normal_noise           | 0.134             | 0.05                  | 0.95                  |                          |
| sample1    | Exponential_Lambda1     | 1                     | Decimal    | add_normal_noise           | 0.063             | 0.05                  | 0.95                  |                          |
| sample1    | Gamma_Shape2_Scale2     | 1                     | Decimal    | add_normal_noise           | 0.182             | 0.05                  | 0.95                  |                          |
| sample1    | Normal_Like_Int         | 1                     | Integer    | add_normal_noise_and_round | 1.163             | 0.05                  | 0.95                  |                          |
| sample1    | Left_Heavy_Int          | 1                     | Integer    | add_normal_noise_and_round | 0.800             | 0.05                  | 0.95                  |                          |
| sample2    | id_number               | 0                     | Integer    | add_normal_noise_and_round | 12.475            | 0.05                  | 0.95                  |                          |
| sample2    | Multi_Modal             | 1                     | Decimal    | add_normal_noise           | 0.250             | 0.05                  | 0.95                  |                          |
| sample2    | With_Missing_Data       | 1                     | Decimal    | add_normal_noise           | 0.068             | 0.05                  | 0.95                  |                          |
| sample2    | Uniform_0_10            | 1                     | Decimal    | add_normal_noise           | 0.252             | 0.05                  | 0.95                  |                          |
| sample2    | Beta_Alpha2_Beta5       | 1                     | Decimal    | add_normal_noise           | 0.012             | 0.05                  | 0.95                  |                          |
| sample2    | Log_Normal_Mean0_Sigma1 | 1                     | Decimal    | add_normal_noise           | 0.066             | 0.05                  | 0.95                  |                          |
| sample2    | Right_Heavy_Int         | 1                     | Integer    | add_normal_noise_and_round | 0.725             | 0.05                  | 0.95                  |                          |
| sample2    | Multi_Modal_Int         | 1                     | Integer    | add_normal_noise_and_round | 3.200             | 0.05                  | 0.95                  |                          |
| sample3    | id_number               | 0                     | Integer    | add_normal_noise_and_round | 12.475            | 0.05                  | 0.95                  |                          |
| sample3    | Binomial_n10_p_one_half | 1                     | NumberList | random_shuffle             |                   |                       |                       | 0.15                     |
| sample3    | Poisson_Lambda3         | 1                     | NumberList | random_shuffle             |                   |                       |                       | 0.15                     |
| sample3    | Uniform_Int             | 1                     | Integer    | add_normal_noise_and_round | 2.600             | 0.05                  | 0.95                  |                          |

- **table_name**: The name of the table containing the variable. This corresponds to the CSV file name without the `.csv` extension.
- **var_name**: The name of the variable.
- **should_be_synthesized**: A flag indicating whether the variable should be synthesized (1) or not (0).
- **datatype**: The type of data for the variable. Options include:
  - String: a column of strings
  - Decimal: a column of floating point numbers
  - Integer: a column of integers
  - NumberList: a column of integers with a few unique values
  - StringList: a column of strings with a few unique values
  - DateTime: a column of DateTime-like values
- **method**: The method used for synthesizing the variable. Examples include:
  - `add_normal_noise`: Add normal noise to the data.
  - `add_normal_noise_and_round`: Add normal noise and round to the nearest integer.
  - `random_shuffle`: Shuffle the values randomly.
- **dispersion_amount**: The standard deviation of the normal distribution used to generate the noise added to the real data to create the synthetic data. This is relevant for `Decimal` and `Integer` datatypes.
- **winsorize_lower_limit** and **winsorize_upper_limit**: These parameters define the limits for Winsorization during the creation of synthetic data. The lowest values are adjusted to the value at the `winsorize_lower_limit` percentile, and the highest values are adjusted to the value at the `winsorize_upper_limit` percentile. Masked values are ignored during this process. This is relevant for `Decimal` and `Integer` datatypes.
- **p_modify_number_list_val**: The probability of modifying a value in a `NumberList` column. This is relevant for `NumberList` datatypes.

## Kick-starting the `dd_synth` with `dd_obs` and `blanket_default_params`

Creating a `dd_synth` manually can be time-consuming. To simplify this process, the package provides an option to generate the `dd_synth` automatically. This involves two main steps:

### Step One: Construct the `dd_obs`

### Step One: Construct the `dd_obs`

First, the package generates a DataFrame called `dd_obs`. This DataFrame contains the following columns:

- **table_name**: The name of the table containing the variable (corresponding to the CSV file name without the `.csv` extension).
- **var_name**: The name of the variable.
- **obs_numobs**: The number of observations for the variable.
- **obs_distinct**: The number of distinct values for the variable.
- **obs_missing**: The number and percentage of missing values for the variable.
- **obs_datatype**: The inferred data type of the variable (e.g., String, Decimal, Integer, NumberList, etc.).

Additionally, `dd_obs` includes various summary statistics for each variable, which depend on the `obs_datatype`. For example, for decimal variables, the summary statistics include:

- **obs_mean**: The mean value.
- **obs_std**: The standard deviation of the values.
- **obs_min**: The minimum observed value.
- **obs_p_25**: The 25th percentile.
- **obs_median**: The median value.
- **obs_p_75**: The 75th percentile.
- **obs_max**: The maximum observed value.
- **obs_permissible_values**: The permissible values for categorical or discrete variables (only applicable for certain data types like `NumberList`).

These summary statistics help determine the parameters that will be used in the `dd_synth`.

#### Example of `dd_obs`

Here's an example of what a `dd_obs` might look like:

| table_name | var_name                | obs_numobs | obs_distinct | obs_missing | obs_datatype | obs_mean | obs_std | obs_min | obs_p_25 | obs_median | obs_p_75 | obs_max | obs_permissible_values         |
| ---------- | ----------------------- | ---------- | ------------ | ----------- | ------------ | -------- | ------- | ------- | -------- | ---------- | -------- | ------- | ------------------------------ |
| sample1    | id_number               | 500        | 500          | 0 (0.0%)    | Integer      | 249.5    | 144.48  | 0.0     | 124.75   | 249.5      | 374.25   | 499.0   |                                |
| sample1    | Standard_Normal         | 500        | 500          | 0 (0.0%)    | Decimal      | -0.0386  | 1.0042  | -3.2311 | -0.6904  | -0.0365    | 0.6696   | 2.9586  |                                |
| sample1    | Normal_Mean5_SD2        | 500        | 500          | 0 (0.0%)    | Decimal      | 4.9190   | 1.9987  | -1.3341 | 3.6389   | 4.9089     | 6.3105   | 12.1432 |                                |
| sample1    | Exponential_Lambda1     | 500        | 500          | 0 (0.0%)    | Decimal      | 1.0286   | 1.0060  | 0.0001  | 0.2737   | 0.7554     | 1.5301   | 7.9413  |                                |
| sample1    | Gamma_Shape2_Scale2     | 500        | 500          | 0 (0.0%)    | Decimal      | 4.1359   | 2.7129  | 0.0300  | 2.0137   | 3.6054     | 5.6619   | 13.9704 |                                |
| sample1    | Normal_Like_Int         | 500        | 87           | 0 (0.0%)    | Integer      | 48.4940  | 18.0666 | 0.0     | 37.0     | 49.0       | 60.25    | 100.0   |                                |
| sample1    | Left_Heavy_Int          | 500        | 57           | 0 (0.0%)    | Integer      | 13.4620  | 13.7512 | 0.0     | 3.0      | 10.0       | 19.0     | 100.0   |                                |
| sample2    | id_number               | 500        | 500          | 0 (0.0%)    | Integer      | 249.5    | 144.48  | 0.0     | 124.75   | 249.5      | 374.25   | 499.0   |                                |
| sample2    | Multi_Modal             | 500        | 500          | 0 (0.0%)    | Decimal      | 0.5203   | 2.5423  | -3.1131 | -1.9861  | 0.5444     | 3.0079   | 4.5254  |                                |
| sample2    | With_Missing_Data       | 450        | 450          | 50 (10.0%)  | Decimal      | 0.0810   | 1.0233  | -2.6434 | -0.5752  | 0.0115     | 0.7830   | 2.7995  |                                |
| sample2    | Uniform_0_10            | 500        | 500          | 0 (0.0%)    | Decimal      | 5.0535   | 2.9332  | 0.0594  | 2.5513   | 4.9989     | 7.5868   | 9.9685  |                                |
| sample2    | Beta_Alpha2_Beta5       | 500        | 500          | 0 (0.0%)    | Decimal      | 0.2806   | 0.1565  | 0.0108  | 0.1562   | 0.2634     | 0.3934   | 0.8048  |                                |
| sample2    | Log_Normal_Mean0_Sigma1 | 500        | 500          | 0 (0.0%)    | Decimal      | 1.5100   | 1.7465  | 0.0348  | 0.4902   | 0.9833     | 1.8173   | 12.8518 |                                |
| sample2    | Right_Heavy_Int         | 500        | 59           | 0 (0.0%)    | Integer      | 85.7380  | 14.3213 | 0.0     | 80.75    | 90.0       | 95.25    | 100.0   |                                |
| sample2    | Multi_Modal_Int         | 500        | 65           | 0 (0.0%)    | Integer      | 49.0080  | 32.8204 | 0.0     | 17.0     | 52.0       | 81.0     | 100.0   |                                |
| sample3    | id_number               | 500        | 500          | 0 (0.0%)    | Integer      | 249.5    | 144.48  | 0.0     | 124.75   | 249.5      | 374.25   | 499.0   |                                |
| sample3    | Binomial_n10_p_one_half | 500        | 10           | 0 (0.0%)    | NumberList   |          |         |         |          |            |          |         | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| sample3    | Poisson_Lambda3         | 500        | 9            | 0 (0.0%)    | NumberList   |          |         |         |          |            |          |         | [0, 1, 2, 3, 4, 5, 6, 7, 8]    |
| sample3    | Uniform_Int             | 500        | 98           | 0 (0.0%)    | Integer      | 49.2740  | 29.6560 | 0.0     | 23.0     | 48.5       | 75.0     | 99.0    |                                |

### Step Two: Combine the `dd_obs` with the `blanket_default_params` to Obtain Parameters for the `dd_synth`

Next, the package uses `blanket_default_params` to automatically create the `dd_synth` by making sensible default decisions based on the `dd_obs`. Here are some example `blanket_default_params`:

- **dispersion_factor**: For example, 0.05. This value is multiplied by the `obs_iqr` of a decimal variable to determine the `dispersion_amount` for that variable in the `dd_synth`.
- **winsorize_lower_limit**: For example, 0.05. This value is set as the `winsorize_lower_limit` for all decimal variables.
- **winsorize_upper_limit**: For example, 0.95. This value is set as the `winsorize_upper_limit` for all decimal variables.

The main idea is that the package uses the information derived from the `dd_obs` and combines it with the `blanket_default_params` to automatically create a `dd_synth`, making the process of generating synthetic data more efficient and user-friendly.

## Example Usage

This section demonstrates how to create sample data and metadata that can be used to develop and test the `synthesize_me` package. The example involves generating synthetic data, creating metadata, and using this metadata to generate new synthetic data.

### Create Sample Data and Metadata to be used by the package

#### Generate Sample Data

First, we will generate some sample data "out of thin air" using the `generate_sample_data.py` script. This script creates CSV files with various distributions to simulate real-world data.

Run the following command to generate sample data:

```bash
python generate_sample_data.py example-data/input --n 500 --seed 123
```

or

```bash
python3 generate_sample_data.py example-data/input --n 500 --seed 123
```

This should create some CSV files in the `./example-data/input` directory. The generated files will contain synthetic data based on different statistical distributions, which can be used for developing and testing the `synthesize_me` package.

#### Generate Sample Metadata

Next, we will generate metadata for the sample data. This metadata will include summary statistics and synthesis instructions.

##### A Sample `dd_obs.csv` file

First, we generate the `dd_obs.csv` file, which contains summary statistics for the sample data. The `generate_dd_obs.py` script reads the sample data and creates this metadata file.

Run the following command to generate the `dd_obs.csv` file:

```bash
python generate_dd_obs.py example-data/input example-data/metadata/dd_obs.csv
```

or

```bash
python3 generate_dd_obs.py example-data/input example-data/metadata/dd_obs.csv
```

This should create the following CSV file: `./example-data/metadata/dd_obs.csv`. This file contains information about the distributions of the variables in the sample data, which is essential for generating synthesis instructions.

##### A Sample `dd_synth.csv` file

Next, we generate the `dd_synth.csv` file, which contains synthesis instructions based on the `dd_obs.csv` metadata. The `generate_dd_synth.py` script reads the `dd_obs.csv` file and creates the `dd_synth.csv` file with default parameters.

Run the following command to generate the `dd_synth.csv` file:

```bash
python generate_dd_synth.py example-data/metadata/dd_obs.csv example-data/metadata/dd_synth.csv
```

or

```bash
python3 generate_dd_synth.py example-data/metadata/dd_obs.csv example-data/metadata/dd_synth.csv
```

This should create the following CSV file: `./example-data/metadata/dd_synth.csv`. This file contains instructions on how to generate new synthetic data based on the distributions and parameters specified in the metadata.

### Creating Synthetic Data from the Sample Data

Finally, we use the `synthesize_me` package to generate synthetic data based on the sample data and the metadata we created. The `synthesize_folder_of_csv_files` function reads the input data and metadata, and produces synthetic versions of the CSV files.

#### General Usage

Use the following code to synthesize the data:

```python
from synthesize_me import synthesize_folder_of_csv_files

input_path = 'example-data/input'
output_path = 'example-data/output'

dd_obs, dd_synth = synthesize_folder_of_csv_files(input_path, output_path)
```

The synthetic data should be saved in the `example-data/output` directory. This synthetic data can be used for further testing and development, ensuring that the `synthesize_me` package works correctly with various types of data.

#### Example Script

There is a sample script that can be executed here:

```bash
python generate_synthetic_data.py
```

or

```bash
python3 generate_synthetic_data.py
```

## Next Steps

### Improve the `synthesize_data` sub-module

In general, this work will go in `synthesize_me/synthesize_data`.

For more details, see the [Next Steps for the synthesize_data module](./synthesize_me/synthesize_data/next_steps.md).

### Update the `dd_synth`

In general, this work will go in `synthesize_me/create_dd_synth`.

For more details, see the [Next Steps for the create_dd_synth module](./synthesize_me/create_dd_synth/next_steps.md).

### Update the `dd_obs`

In general, this work will go in `synthesize_me/generate_dd_obs`.

For more details, see the [Next Steps for the generate_dd_obs module](./synthesize_me/generate_dd_obs/next_steps.md).

### Improve the `compare` sub-module

In general, this work will go in `synthesize_me/compare`

For more details, see the [Next Steps for the compare module](./synthesize_me/compare/next_steps.md).
