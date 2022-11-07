liste_en_bazar = [14, 2.21, ["docstring", 74, "cactus",
                             {"chien": "berger allemand"}], 74, (12, [47, 7.3])]


def compterProfondeur(bazar):
    nombreNombre = 0
    for chose in bazar:
        print(chose)
        print(type(chose))
        if type(chose) == int or type(chose) == float:
            nombreNombre += 1
        elif type(chose) == list or type(chose) == dict:
            for trucs in chose:
                print(trucs)
                print(type(trucs))
                if type(trucs) == int or type(trucs) == float:
                    nombreNombre += 1
                if type(trucs) == list:
                    for machin in chose:
                        print(machin)
                        print(type(machin))
                        if type(machin) == int or type(machin) == float:
                            nombreNombre += 1
    return nombreNombre


print(compterProfondeur(liste_en_bazar))
