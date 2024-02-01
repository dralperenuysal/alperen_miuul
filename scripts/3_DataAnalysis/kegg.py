import pandas as pd
import os

print(os.getcwd())
os.chdir('/home/alperen/PycharmProjects/alperen_miuul')

# define the paths
eggnog = "resource/kegg/G_intestinalis.csv"
out_file = "output/kegg/kegg_Gintestinalis_wb.csv"

# read the data
df = pd.read_csv(eggnog, header="infer", sep="\t")

# split the columns into multiple columns
df_kegg = df.dropna(subset=["KEGG_KOs"])["KEGG_KOs"].str.split(",", expand=True)

# merge all columns into one
df_kegg_melt = pd.melt(df_kegg, value_name="KEGG_KOs").dropna(subset=["KEGG_KOs"])

# drop duplicates
df_kegg_melt = df_kegg_melt.drop_duplicates(subset=["KEGG_KOs"])

# sort the data
df_kegg_melt_sort = df_kegg_melt.sort_values(by=["variable"], ascending=False)