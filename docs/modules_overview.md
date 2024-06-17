# Modules Overview

This document provides an overview of the various modules in the `synthesize_me` package and links to their specific documentation.

## `generate_dd_obs`

The `generate_dd_obs` module is responsible for creating the `dd_obs` DataFrame, which contains inferred data types and summary statistics for the variables in the input CSV files.

For more details, see the [generate_dd_obs README](../synthesize_me/generate_dd_obs/readme.md).

## `create_dd_synth`

The `create_dd_synth` module generates the `dd_synth` DataFrame, which includes synthesis instructions for generating synthetic data.

For more details, see the [create_dd_synth README](../synthesize_me/create_dd_synth/readme.md).

## `synthesize_data`

The `synthesize_data` module is responsible for applying synthesis instructions to generate synthetic CSV files. This module processes the synthesis instructions from `dd_synth` and applies them to the input CSV files to create synthetic versions.

For more details, see the [synthesize_data README](../synthesize_me/synthesize_data/readme.md).

## `compare`

The `compare` module is responsible for comparing synthesized data with original data.

For more details, see the [compare README](../synthesize_me/compare/readme.md).

## Other Modules

- `synthesize_me/__init__.py`: Initializes the package.
- Additional modules and their functionalities will be documented here as they are developed.
