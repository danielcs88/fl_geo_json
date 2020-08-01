# %% [markdown]
# # Florida JSON

# %%
import json
from urllib.request import urlopen

with urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
) as response:
    counties = json.load(response)

# %%
print(type(counties))

# %%
type(counties.get("features"))

# %%
import pandas as pd

test = counties.get("features")

# %%
florida = []

# %%
for entry in test:
    if entry.get("properties").get("STATE") == '12':
        florida.append(entry)

# %%
fl_json = dict(type="FeatureCollection", features=florida)
