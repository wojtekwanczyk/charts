import csv, sys
import unittest
import matplotlib.pyplot as plt
from random import randint
import copy
import numpy as np

class Data:
    def __init__(self, name):
        if name != "":
            self.year = name[:-4]
            with open(name) as data_file:
                r = csv.reader(data_file)
                self.data = list(r)
        else:
            self.year = "2015"
            self.data = []

    def get_list(self):
        return self.data

    def show(self):
        for row in self.data:
            print(', '.join(row))

    def __str__(self):
        ret = ""
        for row in self.data:
           ret += str(row) + "\n"
        return ret

    def __add__(self, other):
        new = copy.copy(self)
        for l in range(1, len(other.data)):
            new.data.append(other.data[l])
        return new


class Chart:

    def map_indexes(self):
        for i in range(0, len(sys.argv) - 1):
            data = Data(sys.argv[i + 1])
            whole_data = data.get_list()

            for j in range(0, len(whole_data[0])):
                if 'Country' in whole_data[0][j]:
                    self.country_i.append(j)
                if 'Rank' in whole_data[0][j]:
                    self.rank_i.append(j)
                if 'Score' in whole_data[0][j]:
                    self.score_i.append(j)
                if 'Economy' in whole_data[0][j]:
                    self.economy_i.append(j)
                if 'Family' in whole_data[0][j]:
                    self.family_i.append(j)
                if 'Health' in whole_data[0][j]:
                    self.health_i.append(j)
                if 'Generosity' in whole_data[0][j]:
                    self.generosity_i.append(j)
                if 'Trust' in whole_data[0][j]:
                    self.trust_i.append(j)
                if 'Freedom' in whole_data[0][j]:
                    self.freedom_i.append(j)
                if 'Dystopia' in whole_data[0][j]:
                    self.dystopia_i.append(j)

    # initialize lists [arg nr][para nr]
    def initialize_lists(self):
        self.data_qtty = len(sys.argv) - 1
        for i in range(0, self.data_qtty):
            data = Data(sys.argv[i])
            whole_data = data.get_list()
            self.country = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.rank = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.health = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.score = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.economy = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.family = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.generosity = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.trust = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.freedom = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
            self.dystopia = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]

    def __init__(self):
        self.country_i = []
        self.rank_i = []
        self.score_i = []
        self.health_i = []
        self.economy_i = []
        self.family_i = []
        self.generosity_i = []
        self.trust_i = []
        self.freedom_i = []
        self.dystopia_i = []

        self.years = []
        for i in range(len(sys.argv)):
            self.years.append(sys.argv[i][:4])
        self.years = self.years[1:]

        self.map_indexes()
        self.initialize_lists()
        self.para_len = 10

        for i in range(0, self.data_qtty):
            data = Data(sys.argv[i + 1])
            whole_data = data.get_list()

            # to skip first element of the list start from 1 (name of parameters)
            for j in range(1, len(whole_data)):
                self.country[i][j - 1] = whole_data[j][self.country_i[i]]
                self.rank[i][j - 1] = whole_data[j][self.rank_i[i]]
                self.health[i][j - 1] = float(whole_data[j][self.health_i[i]])
                self.score[i][j - 1] = float(whole_data[j][self.score_i[i]])
                self.economy[i][j - 1] = float(whole_data[j][self.economy_i[i]])
                self.family[i][j - 1] = float(whole_data[j][self.family_i[i]])
                self.generosity[i][j - 1] = float(whole_data[j][self.generosity_i[i]])
                self.trust[i][j - 1] = float(whole_data[j][self.trust_i[i]])
                self.freedom[i][j - 1] = float(whole_data[j][self.freedom_i[i]])
                self.dystopia[i][j - 1] = float(whole_data[j][self.dystopia_i[i]])
                # print(whole_data[j-1])

    def __str__(self):
        ret = ""
        for data in range(self.data_qtty):
            for i in range(len(self.country[data])):
                if(self.country[data][i] != 0):
                    ret += "In " + str(self.years[data]) + " country " + str(self.country[data][i]) + \
                           " was on " + str(self.rank[data][i]) + " position\n"
        return ret

    # finds position of country in given year as index, returns index (stating form 0)
    def findPosition(self, nr, name):
        if nr >= self.data_qtty:
            return -1
        for j in range(len(self.country[nr])):
            if name == self.country[nr][j]:
                return j
        return -1

    def rank_plot(self, nr, qtty):
        plt.plot(self.rank[nr][:qtty], self.country[nr][:qtty], "yo")
        plt.ylabel("Countries")
        plt.xlabel("Rank")
        plt.title('RANK')
        plt.subplots_adjust(left=0.2)
        plt.show()

    def life_expectancy(self, nr, qtty):
        plt.barh(range(qtty), self.health[nr][:qtty])
        plt.yticks(range(qtty), self.country[nr])
        plt.title('Life Expectancy Rate')
        plt.subplots_adjust(left=0.20)
        plt.show()

    def few_charts(self, nr, qtty):
        plt.figure(1, figsize=(9, 3))

        plt.subplot(131)
        plt.bar(self.country[nr][:qtty], self.family[nr][:qtty], color="g")
        plt.title('Family rate')
        plt.xticks(rotation = "vertical")

        plt.subplot(132)
        plt.bar(self.country[nr][:qtty], self.rank[nr][:qtty], color="y")
        plt.xticks(rotation = "vertical")
        plt.title('Rank')

        plt.subplot(133)
        plt.scatter(self.country[nr][:qtty], self.health[nr][:qtty])
        plt.xticks(rotation = "vertical")
        plt.subplots_adjust(bottom=0.3)
        plt.subplots_adjust(top=0.8)
        plt.title('Health rate')

        plt.suptitle('Pare wykresow')
        plt.show()

    def dystopia_chart(self, nr, qtty, color, *args):
        countries = []
        dystopias = []
        for i in range(len(args)):
            for j in range(len(self.country[nr])):
                if args[i] == self.country[nr][j]:
                    x = j
                    break
            countries.append(args[i])
            dystopias.append(self.dystopia[nr][x])

        for i in range(qtty - len(args)):
            x = randint(0, 158)
            countries.append(self.country[nr][x])
            dystopias.append(self.dystopia[nr][x])

        plt.bar(countries, dystopias, color = color)
        plt.title('Dystopia rate')
        plt.xticks(rotation = "vertical")

        plt.subplots_adjust(bottom=0.3)

        plt.show()

    def freedom_chart(self, nr, qtty, color, *args):
        countries = []
        freedoms = []
        for i in range(len(args)):
            for j in range(len(self.country[nr])):
                if args[i] == self.country[nr][j]:
                    x = j
                    break
            countries.append(args[i])
            freedoms.append(self.freedom[nr][x])

        for i in range(qtty - len(args)):
            x = randint(0, 158)
            countries.append(self.country[nr][x])
            freedoms.append(self.freedom[nr][x])

        plt.bar(countries, freedoms, color = color)
        plt.title('Freedom rate')
        plt.xticks(rotation = "vertical")

        plt.subplots_adjust(bottom=0.3)

        plt.show()

    def trust_chart(self, nr, qtty, color, *args):
        countries = []
        trusts = []
        for i in range(len(args)):
            for j in range(len(self.country[nr])):
                if args[i] == self.country[nr][j]:
                    x = j
                    break
            countries.append(args[i])
            trusts.append(self.trust[nr][x])

        for i in range(qtty - len(args)):
            x = randint(0, 158)
            countries.append(self.country[nr][x])
            trusts.append(self.trust[nr][x])

        plt.bar(countries, trusts, color = color)
        plt.title('Trust rate')
        plt.xticks(rotation = "vertical")

        plt.subplots_adjust(bottom=0.3)

        plt.show()

    def throughYears(self, country, c, *args):
        pos = []
        for i in range(self.data_qtty):
            pos.append(self.findPosition(i, country) + 1)
        plt.plot(self.years, pos, c, self.years, pos, c + "o")
        plt.ylabel("Rank")
        plt.xlabel("Year")
        plt.title(str(country) + " rank")
        #plt.subplots_adjust(left=0.2)
        if len(args) > 0:
            plt.savefig(args[0])
        plt.show()

    def compareTwo(self, filenr, *args):
        pos = []
        ys = []
        rects = []
        N = 6
        ind = np.arange(N)  # the x locations for the groups
        w = 0.8
        width = w/len(args)           # the width of the bars
        fig, ax = plt.subplots()
        colors = ['r', 'y', 'b', 'g', 'c', 'm']


        x = 0
        for i in range(len(args)):
            pos.append(self.findPosition(filenr, args[i]))
            ys.append([self.generosity[filenr][pos[i]], self.trust[filenr][pos[i]],
               self.freedom[filenr][pos[i]], self.health[filenr][pos[i]],
               self.economy[filenr][pos[i]], self.family[filenr][pos[i]]])
            rects.append(ax.bar(ind + x, ys[i], width, color = colors[i]))
            x += width

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Rates')
        ax.set_title('Comparision between countries')
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(('Generosity', 'Trust', 'Freedom', 'Health', 'Economy', 'Family'))


        cs_tuple = tuple(args)
        rec_list = []
        for i in range(len(args)):
            rec_list.append(rects[i][0])
        rec_tuple = tuple(rec_list)



        ax.legend(rec_tuple, cs_tuple)

        plt.show()


wykres = Chart()

'''
wykres.rank_plot(1, 10)
wykres.life_expectancy(1, 15)
wykres.few_charts(1,3)
wykres.dystopia_chart(1, 10, "G", "France", "Belarus", "China", "Togo")
wykres.freedom_chart(1, 10, "C", "France", "Belarus", "China", "Togo")
wykres.trust_chart(1, 10, "R", "France", "Belarus", "China", "Japan", "Poland", "Germany")
wykres.throughYears("Poland", 'g')
wykres.throughYears("Belarus", 'b')
'''

# wykres.throughYears("Switzerland", "g", "swtz.png")

# finding postion of a country
# print(wykres.findPosition(0, "Poland"))
# print(wykres.findPosition(0, "Switzerland"))


# str representation - chart
# print(wykres)

data1 = Data(sys.argv[1])
data2 = Data(sys.argv[2])
data3 = Data(sys.argv[3])

wykres.compareTwo(0, "Egypt", "Niger", 'RPA', 'Sri Lanka')

# str representation - data
# print(data1)

# add override
#data4 = data1 + data2
#print(data4)


class MyTestCase(unittest.TestCase):

    def test_countries(self):
        self.assertEqual(wykres.country[0][0], "Switzerland")
        self.assertEqual(wykres.country[0][1], "Iceland")
        self.assertEqual(wykres.country[0][2], "Denmark")
        self.assertEqual(wykres.country[1][0], "Denmark")
        self.assertEqual(wykres.country[2][0], "Norway")

    def test_findPosition(self):
        self.assertEqual(wykres.findPosition(0,"Switzerland"), 0)
        self.assertEqual(wykres.findPosition(2,"Germany"), 15)
        self.assertEqual(wykres.findPosition(0,"Poland"), 59)
        self.assertEqual(wykres.findPosition(1,"Poland"), 56)
        self.assertEqual(wykres.findPosition(2,"Poland"), 45)
        self.assertEqual(wykres.findPosition(2,"qwerty"), -1)
        self.assertEqual(wykres.findPosition(3,"Poland"), -1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'])



