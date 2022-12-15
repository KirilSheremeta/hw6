cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
translation = ("a", "b", "v", "g", "d", "e", "e",
               "j", "z", "i", "j", "k", "l", "m",
               "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch",
               "", "y", "", "e", "ju", "ja", "je",
               "i", "ji", "g")
translations = {}

for i, j in zip(cyrillic_symbols, translation):
    translations[ord(i)] = j
    translations[ord(i.upper())] = j.upper()


def normalize_names(name):
    """ This function normalizing from Cyrillic to Latin"""

    result = ""
    try:
        for symbol in name.split(".")[0]:
            if symbol.lower() not in cyrillic_symbols and symbol.lower() not in translation and symbol not in "1234567890cxwXCW":
                result += "_"
            elif symbol.lower() not in cyrillic_symbols:
                result += symbol
            else:
                result += translations[ord(symbol)]
    except:
        return name
    result += "." + name.split(".")[1]
    return result
