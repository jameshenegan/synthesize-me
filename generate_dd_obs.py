from synthesize_me.generate_dd_obs import generate_dd_obs

dd_obs = generate_dd_obs("./example-data/input")

dd_obs.to_csv("./example-data/metadata/dd_obs.csv", index=False)