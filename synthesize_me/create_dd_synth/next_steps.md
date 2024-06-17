# `create_dd_synth` Module: Next Steps

## Next Steps

### Add a `method` parameter

Add something like a "method" to the DDsynth so that the user can control the method that is used to generate the synthetic data.

Different methods will be available for different data types.

For example, one method for NumberLists is to treat the number list like an ordered numberlist. Another is to treat it as unordered.

### Add a parameter for NumberList synthesization.

Right now, there isn't a parameter that's being passed in to the synthesize_number_list function.

### Add a `should_be_synthesized` parameter

We want to give the user the ability to avoid synthesizing certain columns (for example id columns). By default, all of the columns will be synthesized. So, by default, the `should_be_synthesized` value will be 1. However, the user can set the `should_be_synthesized` value to 0 for variables that they don't want to synthesize.
