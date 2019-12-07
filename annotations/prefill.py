import pandas as pd

df = pd.read_csv("annotations/annotation_02")

keep = ["cveid", "description", "spans"] + [col for col in df.columns if col.endswith("-tag")]

df = df[keep]

#  df = df.fillna(-1)

df = df.rename(columns= lambda x: x.replace("tag", "fill"))

df.to_csv("annotations/annotation_02_prefilled", index=None)
