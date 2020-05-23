------------
Source: "https://antoinevastel.com/algorithme/python/algorithmes%20g%C3%A9n%C3%A9tiques/2016/04/30/probleme-voyageur-commerce.html"
------------
import math
import random
import numpy as np
from eHandler import PrintException as EH


class Node:
    """
    Node: a city (represented as (x, y) coordinates)"
    """
    def __init__(self, cityName, latitude, longitude):
        """
        TripNode Class Initializer
        :param longitude: float
        :param latitude: float
        :param cityName: float
        """
        try:
            self.longitude = longitude
            self.latitude = latitude
            self.cityName = cityName

        except:
            EH()

    def distanceBetweenCities(self, city):
        """
        Distance between 2 cities
        :param city: list[float, float]
        :return: Distance:float
        """
        try:

            """R = 6371e3
            fphi1 = self.latitude * math.pi/180
            fphi2 = city.latitude * math.pi/180
            deltaph = (city.latitude-self.latitude) * math.pi/180
            deltalm = (city.longitude-self.longitude) * math.pi/180

            a = math.sin(deltaph/2)* math.sin(deltaph/2) + math.cos(fphi1) * math.cos(fphi2) * math.sin(deltalm/2) * math.sin(deltalm/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

            distance = R * c / 1000"""

            xDis = abs(self.latitude - city.latitude)
            yDis = abs(self.longitude - city.longitude)
            distance = np.sqrt((xDis ** 2) + (yDis ** 2))

            return distance

        except:
            EH()


class TripManager:
    """
    Trips Manager Class: add cities to the trip
    """
    def __init__(self):
        """
        TheTrip Manager Class Initializer
        """
        try:
            self.destinationCities = []

        except:
            EH()

    def addNode(self, city):
        """
        Add city to a trip list
        :param city: list[int, float, float]
        :return: None
        """
        try:
            self.destinationCities.append(city)

        except:
            EH()

    def getNode(self, index):
        """
        Get city from a trip list
        :param index: int
        :return: list[int, float, float]
        """
        try:
            return self.destinationCities[index]

        except:
            EH()

    def tripLength(self):
        """
        Length of trip
        :return: float
        """
        try:
            return len(self.destinationCities)

        except:
            EH()


class Trips:
    """
    Individual Trip : a single route satisfying the Node conditions
    """
    def __init__(self, tripManager, trip=None):
        """
        Trips Class Initializer
        :param tripManager: list[int, float, float]
        :param trip: boolean
        """
        try:
            self.tripManager = tripManager
            self.trip = []
            self.distance = 0
            self.fitness = 0.0

            if trip is not None:
                self.trip = trip
            else:
                for i in range(0, self.tripManager.tripLength()):
                    self.trip.append(None)
        except:
            EH()

    def __getitem__(self, index):
        return self.trip[index]

    def __len__(self):
        return len(self.trip)

    def __setitem__(self, index, value):
        self.trip[index] = value

    def generateIndividuals(self):
        """
        Set cities in a trip with a random shuffle
        :return:None
        """
        try:
            for _cityIndices in range(0, self.tripManager.tripLength()):
                self.setTrip(_cityIndices
                             , self.tripManager.getNode(_cityIndices))
            random.shuffle(self.trip)

        except:
            EH()

    def getTrip(self, index):
        """
        Get a city from trip list
        :param position: int
        :return: list[int, float, float]
        """
        try:
            return self.trip[index]

        except:
            EH()

    def setTrip(self, index, city):
        """
        Set a city into trip list
        :param position: int
        :param city: list [int, float, float]
        :return: None
        """
        try:
            self.trip[index] = city
            self.fitness = 0.0
            self.distance = 0


        except:
            EH()

    def getDistance(self):
        """
        Trips distance between two cities
        :return: float
        """
        try:
            if self.distance == 0:
                _tripDistance = 0
                for _cityIndices in range(0, self.tripSize()):
                    _originCity = self.getTrip(_cityIndices)
                    _destinationCity  = None
                    if _cityIndices + 1 < self.tripSize():
                        _destinationCity = self.getTrip(_cityIndices + 1)
                    else:
                        _destinationCity = self.getTrip(0)
                    _tripDistance += _originCity.distanceBetweenCities(_destinationCity)
                self.distance = _tripDistance

            return self.distance

        except:
            EH()

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.getDistance())

        return self.fitness

    def tripSize(self):
        """
        Trips Size
        :return:float
        """
        try:
            return len(self.trip)

        except:
            EH()

    def cityContent(self, city):
        """

        :param city: list
        :return: list
        """
        try:
            return city in self.trip

        except :EH()


class Population:
    """
    A collection of possible routes
    """
    def __init__(self, tripManager, populationSize, flag):
        """
        Population Initializer
        :param tripManager: list[]
        :param populationSize: int
        :param flag: boolean
        """
        try:
            self.trips = []
            for i in range(0, populationSize):
                self.trips.append(None)

            if flag:
                for i in range(0, populationSize):
                    newTrip = Trips(tripManager)
                    newTrip.generateIndividuals()
                    self.setPopulation(i, newTrip)

        except:
            EH()

    def __setitem__(self, key, value):
        self.trips[key] = value

    def __getitem__(self, index):
        return self.trips[index]

    def setPopulation(self, index, trip):
        """

        :param index:
        :param trip:
        :return:
        """
        self.trips[index] = trip

    def getPopulation(self, index):
        """

        :param index:
        :return:
        """
        return self.trips[index]

    def getFittest(self):
        """

        :return:
        """
        try:
            fitnessResults = self.trips[0]
            for i in range(0, self.populationSize()):
                if fitnessResults.getFitness() <= self.getPopulation(i).getFitness():
                    fitnessResults = self.getPopulation(i)
            return fitnessResults

        except:
            EH()

    def populationSize(self):
        """

        :return:
        """
        try:
            return len(self.trips)

        except:
            EH()


class GeneticAlgorithm:
    """

    """
    def __init__(self, tripManager
                 , mutationRate = 0.01
                 , tournamentSize = 5
                 ,eliteSize = True):
        try:
            self.tripManager = tripManager
            self.mutationRate = mutationRate
            self.tournamentSize = tournamentSize
            self.elitism = eliteSize

        except:
            EH()

    def matingPool(self, pop):
        """
        Mating Pool
        :param pop:
        :return:
        """
        try:
            newPopulation = Population(self.tripManager, pop.populationSize(), False)

            # offspring
            elitismOffset = 0
            if self.elitism:
                newPopulation.setPopulation(0, pop.getFittest())
                elitismOffset = 1


            # Parents: two routes that are combined to create a child route
            for i in range(elitismOffset, newPopulation.populationSize()):
                parent1 = self.tournamentSelection(pop)
                parent2 = self.tournamentSelection(pop)
                child = self.crossover(parent1, parent2)
                newPopulation.setPopulation(i, child)

            for i in range(elitismOffset, newPopulation.populationSize()):
                self.mutate(newPopulation.getPopulation(i))

            return newPopulation

        except:
            EH()

    def crossover(self, parent1, parent2):
        """
        Breeding
        :param parent1:list
        :param parent2:list
        :return:list
        """
        try:
            child = Trips(self.tripManager)

            startPos = int(random.random() * parent1.tripSize())
            endPos = int(random.random() * parent1.tripSize())

            for i in range(0, child.tripSize()):
                if startPos < endPos and i > startPos and i < endPos:
                    child.setTrip(i, parent1.getTrip(i))
                elif startPos > endPos:
                    if not (i < startPos and i > endPos):
                        child.setTrip(i, parent1.getTrip(i))

            for i in range(0, parent2.tripSize()):
                if not child.cityContent(parent2.getTrip(i)):
                    for j in range(0, child.tripSize()):
                        if child.getTrip(j) == None:
                            child.setTrip(j, parent2.getTrip(i))
                            break
            return child

        except:
            EH()

    def mutate(self, trip):
        """
        Mutate Class
        :param trip: list
        :return: None
        """
        try:
            # swap mutation
            for tripPos1 in range(0, trip.tripSize()):
                if random.random() < self.mutationRate:
                    tripPos2 = int(trip.tripSize() * random.random())

                    city1 = trip.getTrip(tripPos1)
                    city2 = trip.getTrip(tripPos2)

                    trip.setTrip(tripPos2, city1)
                    trip.setTrip(tripPos1, city2)
        except:
            EH()

    def tournamentSelection(self, pop):
        """
        A set number of individuals are randomly selected from the population
        :param pop: list
        :return: list
        """
        try:
            tournament = Population(self.tripManager, self.tournamentSize, False)
            for i in range(0, self.tournamentSize):
                randomId = int(random.random() * pop.populationSize())
                tournament.setPopulation(i, pop.getPopulation(randomId))
            fittest = tournament.getFittest()

            return fittest

        except:
            EH()
