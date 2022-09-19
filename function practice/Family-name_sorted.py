
def famili(names):
    list_of_tuples = list()
    for name in names:
        name_tuple = tuple(name.split())
        list_of_tuples.append(name_tuple)

    sorted_list = sorted(list_of_tuples,key=lambda x: x[1])

    for name in sorted_list:
        print(name[0],name[1])

names = ['Ali Cheraghi','Maryam Darabi','Hesam Akbari','Romina Bayat']
famili(names)