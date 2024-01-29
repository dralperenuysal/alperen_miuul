import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_of_Gmuris.columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
df_of_Ssalmonicida.columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

data_list = [df_of_Gmuris, df_of_Ssalmonicida]

num_hits_blastn_Gmuris = len(df_of_Gmuris)
num_hits_Ssalmonicida = len(df_of_Ssalmonicida)

print("The number of hits between G.intestinalis and G.muris:", num_hits_blastn_Gmuris)
print("The number of hits between G.intestinalis and S.salmonicida:", num_hits_Ssalmonicida)

sns.histplot(data= df_of_Gmuris, x = "pident")
plt.show()

pivot_table_Gmuris = pd.pivot_table(df_of_Gmuris, values='length', index= 'qseqid', columns= 'sseqid')
plt.show()

sns.scatterplot(data = df_of_Gmuris.reset_index(), x = 'index', y = 'bitscore', hue = 'pident')
plt.show()

sns.scatterplot(data = df_of_Gmuris.reset_index(), x = 'index', y = 'length', hue = 'pident')
plt.show()