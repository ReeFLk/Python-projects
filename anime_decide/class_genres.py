import scrap


def classingDict():
    with open('anime_decide/genres.txt') as f:
        lines = f.readlines()
        list_temp = [line.rstrip().rstrip(")").split(" (") for line in lines]
        dict_genres = {list_temp[i][0]: int("".join(list_temp[i][1].split(",")))
                    for i in range(0, len(list_temp), 2)}
        print(dict_genres)
        


classingDict()
