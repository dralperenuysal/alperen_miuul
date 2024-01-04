def nukleotidleri_say(dizi):
    sayac = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nukleotid in dizi:
        if nukleotid in dizi:
            sayac(nukleotid) += 1
    return sayac
