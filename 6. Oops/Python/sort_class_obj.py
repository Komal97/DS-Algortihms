class Movie:
    def __init__(self, book, year):
        self.book = book
        self.year = year
    
    def printObj(self):
        print(self.book, self.year)

def sort_year(obj):
    return obj.year

if __name__ == '__main__':
    l = []
    l.append(Movie('a', 1996))
    l.append(Movie('b', 2000))
    l.append(Movie('c', 1980))
    l.append(Movie('d', 1990))

    for m in l:
        m.printObj()
    
    # method - 1
    a = sorted(l, key = sort_year)
    for m in a:
        m.printObj()

    # method - 2
    b = sorted(l, key = lambda x: x.year)
    for m in b:
        m.printObj()
    