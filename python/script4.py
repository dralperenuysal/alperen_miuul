def pozisyon_belirle(dizi):
    pozisyon = {'A': [], 'C': [], 'G': [], 'T': []}
    for index, nukleotid in enumerate(dizi):
        if nukleotid in pozisyon:
            pozisyon[nukleotid].append(index)
    return pozisyon