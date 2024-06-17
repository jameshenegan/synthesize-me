# `create_dd_synth` Module

The `create_dd_synth` module is responsible for creating the `dd_synth` DataFrame. This DataFrame includes synthesis instructions for generating synthetic data based on the inferred data types and summary statistics provided by the `dd_obs` DataFrame. The synthesis parameters can be fine-tuned using blanket default parameters.

## Functions

### `create_dd_synth`

This function generates the `dd_synth` DataFrame by combining information from the `dd_obs` DataFrame and applying the blanket default parameters to determine synthesis instructions.

**Parameters:**

- `dd_obs` (pd.DataFrame): The DataFrame containing inferred data types and summary statistics for each variable.
- `blanket_default_params` (dict): A dictionary containing default parameters for data synthesis.

**Returns:**

- `dd_synth_df` (pd.DataFrame): A DataFrame containing synthesis instructions for each variable.

**Example:**

```python
from synthesize_me.create_dd_synth import create_dd_synth

# Assume dd_obs is already created and blanket_default_params is defined
dd_obs = pd.read_csv('path/to/dd_obs.csv')
blanket_default_params = {
    'dispersion_factor': 0.05,
    'winsorize_lower_limit': 0.05,
    'winsorize_upper_limit': 0.95
}

dd_synth_df = create_dd_synth(dd_obs, blanket_default_params)
print(dd_synth_df)
```

## Parameters in `dd_synth`

The `dd_synth` DataFrame includes the following columns for each variable:

- **table_name**: The name of the table containing the variable (derived from the CSV file name).
- **var_name**: The name of the variable.
- **datatype**: The inferred data type of the variable (e.g., String, Decimal, Integer, NumberList, etc.).
- **dispersion_amount**: The amount of dispersion (noise) to add to the variable, calculated based on the interquartile range (IQR) and the `dispersion_factor` from the `blanket_default_params`.
- **winsorize_lower_limit**: The lower limit for Winsorization, set using the `winsorize_lower_limit` from the `blanket_default_params`.
- **winsorize_upper_limit**: The upper limit for Winsorization, set using the `winsorize_upper_limit` from the `blanket_default_params`.

## How It Works

1. **Initialization**: The `create_dd_synth` function initializes an empty list to hold the `dd_synth` data.

2. **Parameter Calculation**: For each variable in the `dd_obs` DataFrame, the function calculates the `dispersion_amount` based on the IQR and `dispersion_factor`, and sets the Winsorization limits using the `blanket_default_params`.

3. **Data Aggregation**: The calculated parameters and other relevant information for each variable are collected in a list of dictionaries.

4. **DataFrame Creation**: The collected data is then converted into a DataFrame (`dd_synth_df`), which is returned by the `create_dd_synth` function.

## Dependencies

- `pandas`

Ensure you have this package installed in your environment.

## Example Usage

Here is an example of how to use the `create_dd_synth` function to create a `dd_synth` DataFrame:

```python
from synthesize_me.create_dd_synth import create_dd_synth

# Load the dd_obs DataFrame
dd_obs = pd.read_csv('path/to/dd_obs.csv')

# Define blanket default parameters
blanket_default_params = {
    'dispersion_factor': 0.05,
    'winsorize_lower_limit': 0.05,
    'winsorize_upper_limit': 0.95
}

# Generate the dd_synth DataFrame
dd_synth_df = create_dd_synth(dd_obs, blanket_default_params)

# Display the resulting DataFrame
print(dd_synth_df)
```

---

## Next Steps

### Add a `method` parameter

Add something like a "method" to the DDsynth so that the user can control the method that is used to generate the synthetic data.

Different methods will be available for different data types.

For example, one method for NumberLists is to treat the number list like an ordered numberlist. Another is to treat it as unordered.

### Add a parameter for NumberList synthesization.

Right now, there isn't a parameter that's being passed in to the synthesize_number_list function.

### Add a `should_be_synthesized` parameter

We want to give the user the ability to avoid synthesizing certain columns (for example id columns). By default, all of the columns will be synthesized. So, by default, the `should_be_synthesized` value will be 1. However, the user can set the `should_be_synthesized` value to 0 for variables that they don't want to synthesize.
