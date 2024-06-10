# Synthesize-ME

We want to develop a Python package that will perform the following task:

Given

- a path to an input folder of CSV files and
- a path to an empty output folder,

generate synthetic versions of the CSV files in the input folder and write them to disk in the output folder.

We want to give the user of the package the option of fine-tuning certain aspects of the synthetic data generation process.

We will call the package `synthesize_me`.

## Example Usage

First generate the sample data:

```bash
cd examples
python generate_sample_data.py
```

Then, generate the `dd_obs.csv` file:

```bash
python generate_dd_obs.py
```

Once we develop the package, use the following code to synthesize the data:

```
from synthesize_me import synthesize_folder_of_csv_files

input_path = 'examples/input'
output_path = 'examples/output'

dd_obs, dd_synth = synthesize_folder_of_csv_files(input_path, output_path)
```

The synthetic data will be saved in the examples/output directory.

# Next Steps

- Create a sub-folder called `metadata` inside of the `examples` folder
- Add an example `dd_obs` to the `metadata` folder
- Add an example `dd_synth` to the `metadata` folder
