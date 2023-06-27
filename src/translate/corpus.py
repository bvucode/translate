
def translate(chlang):
    llist = []
    rlist = []

    if chlang == "eng-ru":
        with open("./data/eng-ru.txt", "r") as file:
            for line in file:
                if not line:
                    continue
                else:
                    left, right, *res = line.split(":")
                    llist.append(left)
                    rlist.append(right.replace("\n", ""))
        return llist, rlist

    elif chlang == "ru-eng":
        with open("./data/ru-eng.txt", "r") as file:
            for line in file:
                if not line:
                    continue
                else:
                    left, right, *res = line.split(":")
                    llist.append(left)
                    rlist.append(right.replace("\n", ""))
        return llist, rlist
