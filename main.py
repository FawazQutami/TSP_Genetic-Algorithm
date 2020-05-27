import argparse
import numpy as np
import datetime as dt

from GAAlgorithm import GeneticAlgorithm as GA \
    , Population \
    , TripManager \
    , Node

from eHandler import PrintException as EH
from plotTSP import plotSA, plot_learning
from setup import install_required_Packages


def coordinatesFile(fileName):
    """
    Coordinates File
    :param fileName: string
    :return: Journey object
    """
    try:
        _journey = TripManager()

        with open(fileName, "r") as f:
            for line in f.readlines():
                line = [float(x.strip()) for x in line.split(" ")]
                cty = Node(int(line[0])
                           , float(line[1])
                           , float(line[2]))
                _journey.addNode(cty)

        return _journey
    except:
        EH()


def runGenetic(Nodes):
    try:
        print("Starting Genetic Algorithm ...")
        start = dt.datetime.now()

        # initiate with population size 50
        initialPopulation = Population(Nodes, 100, True)
        print("Initial Distance: " + str(initialPopulation.getFittest().getDistance()))

        ga = GA(Nodes
                , mutationRate=0.05
                , tournamentSize=15
                , eliteSize=True)

        fitnessResults = []
        nextGeneration = ga.matingPool(initialPopulation)
        for i in range(0, 1000):
            nextGeneration = ga.matingPool(nextGeneration)
            fitnessResults.append(nextGeneration.getFittest().getDistance())

        print("Final Distance: " + str(nextGeneration.getFittest().getDistance()))
        print("Final Fitness: " + str(nextGeneration.getFittest().getFitness()))

        end = dt.datetime.now()
        print('Genetic Algorithm Execution Time in seconds: {%.2f}' % (end - start).seconds)

        # Extract the best population trip
        bestPopulation = nextGeneration.getFittest()
        # print(bestPopulation)
        fitness = fitnessResults
        # print(fitness)

        return bestPopulation, fitness

    except:
        EH()


def main():
    """ """
    try:
        print()
        print("1. Djibouti - 38 Cities.")
        print("2. Qatar - 194 Cities.\n")
        choice = int(input("Your choice? "))

        """
        Traveling salesman problem: is, given a set of cities, to find the shortest 
        path to visit all of the cities exactly once.
        """
        parser = argparse.ArgumentParser(description="Metaheuristics")

        fileList = ["data/dj38_tsp.txt", "data/qa194_tsp.txt"]
        parser.add_argument("--filename",  # name or flags - Either a name or a
                            # list of option strings
                            choices=fileList,  # choices - A container of the allowable
                            # values for the argument.
                            default=fileList[choice - 1],  # default - The value produced if the
                            # argument is absent from the command line.
                            help='A string represents a dataset'  # help - A brief
                            # description of what the argument does.
                            )

        args = parser.parse_args()

        # load and read data ----------------------------------------------------
        print("..." * 15)
        _Nodes = coordinatesFile(args.filename)
        cityName = []
        latitude = []
        longitude = []

        solutionObj, fitnessObj = runGenetic(_Nodes)

        # Prepare the data for plotting the trip
        for city in solutionObj.trip:
            # print(city.latitude)
            cityName.append(city.cityName)
            latitude.append(city.latitude / 1000)
            longitude.append(city.longitude / 1000)
        cityName.append(cityName[0])
        latitude.append(latitude[0])
        longitude.append(longitude[0])
        # print(longitude)

        # Visualize
        if choice == 1:
            plotSA(cityName, latitude, longitude, "Djibouti")
        else:
            plotSA(cityName, latitude, longitude, "Qatar")

        plot_learning(fitnessObj)
    except:
        EH()


if __name__ == "__main__":
    try:
        # Install Required packages
        install_required_Packages()
        main()

    except:
        EH()
