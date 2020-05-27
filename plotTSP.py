import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from eHandler import PrintException as EH


def plot_learning(fitness_list):
    """
    Plot the fitness function through iterations.
    :param fitness_list: list[float]
    :return: plot
    """
    fig = plt.figure(figsize=(8, 5), constrained_layout=True)
    plt.title("Learning Rate", color='b')
    plt.plot([i for i in range(len(fitness_list))], fitness_list)
    plt.ylabel("Fitness - Distance", c='r')
    plt.xlabel("Iteration", c='r')
    plt.show()


def plotSA(cityName, latitude, longitude, country):
    """"""

    try:
        fig = plt.figure(figsize=(10, 5), constrained_layout=True)

        fig.suptitle(country + ' Journey')

        if country == "Qatar":
            map = Basemap(width=250000
                      , height=350000
                      , resolution='i'
                      , projection='tmerc'
                      , lat_0=25.286106
                      , lon_0=51.534817
                      )
        else:
            map = Basemap(width=350000
                          , height=400000
                          , resolution='i'
                          , projection='tmerc'
                          , lat_0=11.572076
                          , lon_0=43.145645
                          )

        map.drawmapboundary(fill_color = 'aqua')
        map.fillcontinents(color = '#FFE4B5', lake_color = 'aqua')
        map.drawcoastlines()
        map.drawcountries()

        x, y = map(longitude, latitude)
        map.plot(x, y, 'bo', markersize=10)

        #for city, xpt, ypt in zip(cityName, x, y):
            #plt.text(xpt + 1000, ypt + 15000, city)

        map.plot(x, y, '*-'
                 , markersize=3
                 , linewidth=1
                 , color='r'
                 , markerfacecolor='b')

        plt.show()

    except:
        EH()
