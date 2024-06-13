# Synthesize-ME

## Introduction

The `synthesize_me` Python package generates synthetic versions of CSV files, allowing researchers and developers to create realistic data for testing and development without exposing sensitive information.

Given:

- a path to an input folder of CSV files, and
- a path to an empty output folder,

`synthesize_me` will generate synthetic versions of the CSV files in the input folder and write them to disk in the output folder. Optionally, users can fine-tune aspects of the synthetic data generation process to suit their specific needs.

## Installation

(TODO: Add installation instructions once the package is finished)

## Usage

(TODO: Add usage instructions once the package is finished)

## Fine-Tuning with `dd_synth`

The `dd_synth` DataFrame allows users to fine-tune aspects of the synthetic data generation process. It serves as both a data dictionary and a set of synthesis instructions.

### Structure of `dd_synth`

| table_name   | var_name | datatype   | dispersion_amount | winsorize_lower_limit | winsorize_upper_limit |
| ------------ | -------- | ---------- | ----------------- | --------------------- | --------------------- |
| demographics | age      | Integer    |                   |                       |                       |
| demographics | gender   | Stringlist |                   |                       |                       |
| sales        | amount   | Decimal    | 12.5              | 0.05                  | 0.95                  |

- **table_name**: The name of the table containing the variable. This corresponds to the CSV file name without the `.csv` extension.
- **var_name**: The name of the variable.
- **datatype**: The type of data for the variable. Options include:
  - String: a column of strings
  - Decimal: a column of floating point numbers
  - Integer: a column of integers
  - Numberlist: a column of integers with a few unique values
  - Stringlist: a column of strings with a few unique values
  - DateTime: a column of DateTime-like values

The datatype influences the manner in which the synthetic data is generated.

The other columns of the `dd_synth` are relevant for only specific data types.

- **dispersion_amount**: The standard deviation of the normal distribution used to generate the noise added to the real data to create the synthetic data. This is relevant for Decimals.
- **winsorize_lower_limit** and **winsorize_upper_limit**: These parameters define the limits for Winsorization during the creation of synthetic data. The lowest values are adjusted to the value at the `winsorize_lower_limit` percentile, and the highest values are adjusted to the value at the `winsorize_upper_limit` percentile. Masked values are ignored during this process. This is relevant for Decimals.

## Kick-starting the `dd_synth` with `dd_obs` and `blanket_default_params`

Creating a `dd_synth` manually can be time-consuming. To simplify this process, the package provides an option to generate the `dd_synth` automatically. This involves two main steps:

### Step One: Construct the `dd_obs`

First, the package generates a DataFrame called `dd_obs`. This DataFrame contains the following columns:

- **table_name**: The name of the table containing the variable (corresponding to the CSV file name without the `.csv` extension).
- **var_name**: The name of the variable.
- **obs_datatype**: The inferred data type of the variable (e.g., String, Decimal, Integer, Numberlist, etc.).

Additionally, `dd_obs` includes various summary statistics for each variable, which depend on the `obs_datatype`. For example, for decimal variables, the summary statistics include:

- **obs_min**: The minimum observed value.
- **obs_max**: The maximum observed value.
- **obs_mean**: The mean value.
- **obs_std**: The standard deviation of the values.
- **obs_p_25**: The 25th percentile.
- **obs_p_75**: The 75th percentile.
- **obs_iqr**: The interquartile range (75th percentile minus the 25th percentile).

These summary statistics help determine the parameters that will be used in the `dd_synth`.

### Step Two: Combine the `dd_obs` with the `blanket_default_params` to Obtain Parameters for the `dd_synth`

Next, the package uses `blanket_default_params` to automatically create the `dd_synth` by making sensible default decisions based on the `dd_obs`. Here are some example `blanket_default_params`:

- **dispersion_factor**: For example, 0.05. This value is multiplied by the `obs_iqr` of a decimal variable to determine the `dispersion_amount` for that variable in the `dd_synth`.
- **winsorize_lower_limit**: For example, 0.05. This value is set as the `winsorize_lower_limit` for all decimal variables.
- **winsorize_upper_limit**: For example, 0.95. This value is set as the `winsorize_upper_limit` for all decimal variables.

The main idea is that the package uses the information derived from the `dd_obs` and combines it with the `blanket_default_params` to automatically create a `dd_synth`, making the process of generating synthetic data more efficient and user-friendly.

## Example Usage

### Create Sample Data and Metadata to be used by the package

#### Generate Sample Data

First, generate some sample data:

```bash
python generate_sample_data.py
```

This should create some CSV files in `./example-data/input`.

#### Generate Sample Metadata

##### A Sample `dd_obs.csv` file

Then, generate the `dd_obs.csv` file:

```bash
python generate_dd_obs.py
```

This should create the following CSV file: `./example-data/metadata/dd_obs.csv`.

##### A Sample `dd_synth.csv` file

Finally, generate the `dd_synth.csv` file:

```bash
python generate_dd_synth.py
```

### Creating Synthetic Data from the Sample Data

Once the package is developed, use the following code to synthesize the data:

```python
from synthesize_me import synthesize_folder_of_csv_files

input_path = 'example-data/input'
output_path = 'example-data/output'

dd_obs, dd_synth = synthesize_folder_of_csv_files(input_path, output_path)
```

The synthetic data should be saved in the `example-data/output` directory.
