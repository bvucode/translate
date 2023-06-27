
class Translate:
    """"класс для перевода """
    def __init__(self, llist, rlist):
        self.llist = llist
        self.rlist = rlist

    def binarysearch(self, xlist, item):
        """binary search бинарный поиск"""
        self.xlist = xlist
        self.item = item
        low:int = 0
        high:int = len(self.xlist)-1
        while low <= high:
            mid:int = (low + high) // 2
            if self.xlist[mid] == self.item:
                return mid
            elif self.xlist[mid] < self.item:
                low = mid + 1
            elif self.xlist[mid] > self.item:
                high = mid - 1
        return False

    def load(self, text):
        """ translate перевод"""
        self.text = text
        elist = []
        ngram = 2

        def fngrams(text, ngrams):
            """ function to make n-grams"""
            nlist = []
            for x, i in enumerate(text):
                trlist = []
                tc = ""
                for j in range(ngrams):
                    if j == 0:
                        tc = str(text[j + x])
                    elif j > 0:
                        try:
                            tc += " " + str(text[j + x])
                        except IndexError:
                            break
                    trlist.append(tc)
                nlist.append(trlist)
            return nlist

        ngtext = fngrams(self.text, ngram)
        
        for x, i in enumerate(ngtext):
            c = 0
            for j in i[::-1]:
                binaryr = self.binarysearch(self.llist, j)
                c += 1
                if binaryr != False:
                    firstword, *res = self.rlist[binaryr].split(",")
                    elist.append(((j, firstword), x))
                    break
                if c == len(i):
                    elist.append(((i[0], "out"), x))
        return elist
