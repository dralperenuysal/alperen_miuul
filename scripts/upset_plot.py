import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import UpSet
import seaborn as sns

path_OG_count = "output/orthofinder/Results_Jan18/Orthogroups/Orthogroups.GeneCount.tsv"
path_singletone = "output/orthofinder/Results_Jan18/Orthogroups/Orthogroups_UnassignedGenes.tsv"
out_0 = "data/upset_plot.png"

df_count = pd.read_csv(path_OG_count, sep = '\t', header = 'infer')
df_count = df_count.set_index("Orthogroup").sort_values(by="Total", ascending=False)
df_count.loc[df_count["Total"] > 1, "Type"] = "OG"

df_sing = pd.read_csv(path_singletone, sep = '\t', header = 'infer')
df_sing = df_sing.set_index("Orthogroup").fillna(8)
df_sing["Total"] = 1
df_sing = df_sing.applymap(lambda x: 1 if isinstance(x, str) == True else x)

df_count_s = pd.concat([df_count, df_sing], axis =0)
df_count_s.loc[df_count_s["Total"] > 1, "Type"] = "OG"
df_count_s.loc[df_count_s["Total"] == 1, "Type"] = "singleton"

df_count_s = df_count_s.rename(columns = {"S_salmonicida_aa": "S. salmonicida",
                                          "G_intestinalis_aa": "G. intestinalis",
                                          "G_muris_aa": "G. muris"})

df_stack = df_count_s.set_index(df_count_s["S. salmonicida"] >=1). \
    set_index(df_count_s["G. intestinalis"] >=1, append = True). \
    set_index(df_count_s["G. muris"] >= 1, append = True)

upset0 = UpSet(df_stack.sort_values(by = "Total", ascending=True),
               min_subset_size=10,
               intersection_plot_elements=0,
               show_counts=True)

pal = sns.dark_palette("#69d", n_colors=2, reverse=False)
upset0.add_stacked_bars(by = "Type",
                        colors=pal,
                        title="Count by type",
                        elements=5)

upset0.style_subsets(max_degree=1,
                     facecolor="white",
                     edgecolor="black",
                     label="Species-specific")

sns.set_style("whitegrid", {"axes.grid": False})
upset0.plot()
plt.suptitle("OG Upset plot")
plt.savefig(out_0, format="png", dpi=1200, bbox_inches="tight")
plt.show()

