# Synthesize-ME

We want to develop a Python package that will perform the following task:

Given

- a path to an input folder of CSV files and
- a path to an empty output folder,

generate synthetic versions of the CSV files in the input folder and write them to disk in the output folder.

We want to give the user of the package the option of fine-tuning certain aspects of the synthetic data generation process.

We will call the package `synthesize_me`.

## Example Usage

First generate some sample data:

```bash
python generate_sample_data.py
```

Then, generate the `dd_obs.csv` file:

```bash
python generate_dd_obs.py
```

Finally, generate the `dd_synth.csv` file:

```bash
python generate_dd_synth.py
```

Once we develop the package, use the following code to synthesize the data:

```
from synthesize_me import synthesize_folder_of_csv_files

input_path = 'example-data/input'
output_path = 'example-data/output'

dd_obs, dd_synth = synthesize_folder_of_csv_files(input_path, output_path)
```

The synthetic data will be saved in the example-data/output directory.

# Next Steps

- Write a first draft of a function called something like `synthesize_continuous_series`
- Right now, there is a script in the examples folder called `generate_dd_synth.py`. We want this to exist inside of the `synthesize_me` package. So I'm thinking we need to move that code into the `synthesize_me` package.
