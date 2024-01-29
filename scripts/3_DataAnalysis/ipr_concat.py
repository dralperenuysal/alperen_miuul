import pandas as pd
import glob
import os

# Learn the current directory
current_directory = os.getcwd()

# Print the curent directory
print("Current Working Directory:", current_directory)

path = "resource/interproscan/*.tsv"
out_file = "data/ipr_concat.csv"
list_files = glob.glob(path)

# Get the species names from the list_files
sp_dic = {}
for element in list_files:
    i = element.split(".")[0]
    i = i.split("/")[-1]
    sp_dic[i] = element

dic_ann = {}
for key, values in sp_dic.items():
    dic_ann[key] = pd.read_csv(values, sep = "\t", header = None, names= list(range(0, 15)), engine= 'python', quoting = 3)[[0, 11, 12]][:100]
    dic_ann[key] = dic_ann[key].dropna().drop_duplicates().rename(columns = {0: "id", 11: 'ipr', 12: 'ann_inter'})

    # add column with a species name
    dic_ann[key]['sp'] = key
    dic_ann[key].to_csv(f"data/{key}.csv", sep = '\t', index = False)

# Concat all species
concat = pd.concat(dic_ann, axis=0).dropna().drop_duplicates()
concat.to_csv(out_file, sep = '\t', index = False)