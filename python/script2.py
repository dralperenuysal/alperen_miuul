def sozluk_yap(dizi):
    sozluk = {}
    for nukleotid in set(dizi):
        sozluk(nukleotid) = dizi.count(nukleotid)
    return sozluk