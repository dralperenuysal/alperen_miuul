import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import os


print(os.getcwd())
ipr_concat = "../data/ipr_concat.csv"
out_file = "../data/ipr_heatmap.png"

def plot_heatmap(df):
    sns.set_style("whitegrid", {"axes.grid": False})
    plt.figure(figsize=(20, 10))

    # Create the heatmap
    ax = sns.heatmap(df,
                     cmap = sns.color_palette("ch:start = .2, rot = -.3", as_cmap = True),
                     square = True,
                     # fat = 'g',
                     linewidths=4,
                     annot = True,
                     cbar_kws = {"shrink": .5},
                     annot_kws = {'size': 5}) # Adjust font size of annotations here

    plt.savefig(out_file, format = "png", bbox_inches = "tight", dpi = 800)
    return plt.show()


def plot_heatmap_illustrative1(df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(20, 15))

    ax = sns.heatmap(df,
                     cmap="YlGnBu",  # Sıcaklık renk paleti
                     annot=True,
                     fmt=".1f",  # Sayısal değerleri bir ondalık basamakla göster
                     linewidths=.5,
                     cbar_kws={"shrink": .5, "label": "Veri Yoğunluğu"})  # Renk ölçeği etiketi

    plt.title("Heatmap - SP and IPR Relationship")
    plt.xlabel("SP")
    plt.ylabel("IPR")
    plt.savefig(out_file, format="png", bbox_inches="tight", dpi=800)
    return plt.show()
def plot_heatmap_illustrative2(df):
    sns.set_style("darkgrid")
    plt.figure(figsize=(20, 15))

    ax = sns.heatmap(df,
                     cmap="viridis",  # Sıcak ve soğuk renkler
                     annot=True,
                     annot_kws= {'size': 5},
                     fmt=".1f",  # Tam sayı formatı
                     linewidths=1,
                     linecolor='black',  # Hücre arası çizgiler
                     cbar_kws={"shrink": .5, "label": "Frekans"})

    plt.title("Detailed Heatmap - SP and IPR Relationship", fontsize=16)
    plt.xlabel("SP", fontsize=12)
    plt.ylabel("IPR", fontsize=12)
    plt.xticks(rotation=45)  # X eksenindeki etiketleri döndür
    plt.yticks(rotation=45)  # Y eksenindeki etiketleri döndür
    plt.savefig(out_file, format="png", bbox_inches="tight", dpi=800)
    return plt.show()


df = pd.read_csv(ipr_concat, header = "infer", sep = "\t")
df = df.groupby(["ipr", "sp"]).size().reset_index().sort_values(by = [0], ascending = False)
df = df.rename(columns = {0: "cou

plot_heatmap(df)

plot_heatmap_illustrative1(df)
plot_heatmap_illustrative2(df)
