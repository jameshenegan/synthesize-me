import pandas as pd 

from synthesize_me.create_dd_synth import create_dd_synth

path_to_dd_obs = "./example-data/metadata/dd_obs.csv"

dd_obs = pd.read_csv(path_to_dd_obs)

dd_synth = create_dd_synth(dd_obs)

dd_synth.to_csv("./example-data/metadata/dd_synth.csv", index=False)