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
    def __init__(self, filename):
        data = Data(filename)
        self.whole_data = data.get_list()
        self.parameters = self.whole_data[0]
        self.countries = []
        self.regions = []
        self.happiness_rank = []
        self.life_exp = []


        # to skip firste element of the list
        iter_data = iter(self.whole_data)
        next(iter_data)
        for elem in iter_data:
            self.countries.append(elem[0])
            self.regions.append(elem[1])
            self.happiness_rank.append(int(elem[2]))
            self.life_exp.append(float(elem[7]))

        print(self.whole_data)

    def rank_plot(self, nr):
        plt.plot(self.happiness_rank[:nr], self.countries[:nr], "yo")
        plt.ylabel("Countries")
        plt.xlabel("Rank")
        #plt.yticks(range(nr), self.countries)
        #plt.xticks(rotation = "vertical")
        #plt.margins(0.1)
        plt.subplots_adjust(left=0.2)
        plt.show()

    def life_expectancy(self, nr):
        plt.barh(range(nr), self.life_exp[:nr])
        plt.yticks(range(nr), self.countries)
        plt.show()

    def more(self, nr):
        plt.figure(1, figsize=(9, 3))

        plt.subplot(131)
        plt.bar(self.countries[:3], self.happiness_rank[:3])
        plt.subplot(132)
        plt.plot(self.countries[:3], self.happiness_rank[:3])
        plt.subplot(133)
        plt.scatter(self.countries[:5], self.life_exp[:5])
        plt.suptitle('Pare wykresow')
        plt.show()



file_count = len(sys.argv) - 1

for i in range(0, file_count):
    print(i)


wykres = Chart("2015.csv")
# wykres.rank_plot(10)
# wykres.life_expectancy(10)
wykres.more(3)

