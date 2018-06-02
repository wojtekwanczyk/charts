import csv, sys
import matplotlib.pyplot as plt


class Data:
    def __init__(self, name):
        with open(name) as data_file:
            r = csv.reader(data_file)
            self.data = list(r)

    def get_list(self):
        return self.data

    def show(self):
        for row in self.data:
            print(', '.join(row))


class Chart:
    def __init__(self):
        self.country = []
        self.rank = []
        self.score = []
        self.economy = []
        self.family = []
        self.health = []
        self.generosity = []
        self.trust = []
        self.freedom = []
        self.dystopia = []


        self.data_qtty = len(sys.argv) - 1
        data = Data(sys.argv[1])
        whole_data = data.get_list()
        self.parameters = whole_data[0]
        self.para_len = 10

        # initialize lists [arg nr][para nr]
        self.countries = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
        self.regions = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
        self.happiness_rank = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]
        self.life_exp = [[0 for x in range(len(whole_data))] for y in range(self.data_qtty)]

        for i in range(0, len(sys.argv) - 1):
            data = Data(sys.argv[i + 1])
            whole_data = data.get_list()

            for j in range(0, len(whole_data[0])):
                if ('Country' in whole_data[0][j]):
                    self.country.append(j)
                if ('Rank' in whole_data[0][j]):
                    self.rank.append(j)
                if ('Score' in whole_data[0][j]):
                    self.score.append(j)
                if ('Economy' in whole_data[0][j]):
                    self.economy.append(j)
                if ('Family' in whole_data[0][j]):
                    self.family.append(j)
                if ('Health' in whole_data[0][j]):
                    self.health.append(j)
                if ('Generosity' in whole_data[0][j]):
                    self.generosity.append(j)
                if ('Trust' in whole_data[0][j]):
                    self.trust.append(j)
                if ('Freedom' in whole_data[0][j]):
                    self.freedom.append(j)
                if ('Dystopia' in whole_data[0][j]):
                    self.dystopia.append(j)

            # to skip firste element of the list start from 1 (name of parameters)
            for j in range(1, len(whole_data)):
                self.countries[i][j] = whole_data[j][self.country[i]]
                self.happiness_rank[i][j] = whole_data[j][self.rank[i]]
                self.life_exp[i][j] = float(whole_data[j][self.health[i]])
                #print(whole_data[j-1])

            #print(whole_data[0])

    def rank_plot(self, nr, qtty):
        plt.plot(self.happiness_rank[nr][:qtty], self.countries[nr][:qtty], "yo")
        plt.ylabel("Countries")
        plt.xlabel("Rank")
        #plt.yticks(range(nr), self.countries)
        #plt.xticks(rotation = "vertical")
        #plt.margins(0.1)
        plt.subplots_adjust(left=0.2)
        plt.show()

    def life_expectancy(self, nr, qtty):
        plt.barh(range(qtty), self.life_exp[nr][:qtty])
        plt.yticks(range(qtty), self.countries[nr])
        plt.subplots_adjust(left=0.20)
        plt.show()

    def more(self, nr, qtty):
        plt.figure(1, figsize=(9, 3))

        plt.subplot(131)
        plt.bar(self.countries[nr][:qtty], self.happiness_rank[nr][:qtty])
        plt.subplot(132)
        plt.plot(self.countries[nr][:qtty], self.happiness_rank[nr][:qtty])
        #plt.subplot(133)
        #plt.scatter(self.countries[nr][:qtty], self.life_exp[nr][:qtty])
        plt.suptitle('Pare wykresow')
        plt.show()


file_count = len(sys.argv) - 1



wykres = Chart()
# wykres.rank_plot(10)
wykres.life_expectancy(1, 10)
#wykres.more(1,3)

