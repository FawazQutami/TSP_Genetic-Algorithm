import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from eHandler import PrintException as EH


def plot_learning(fitness_list):
    """
    Plot the fitness function through iterations.
    :param fitness_list: list[float]
    :return: plot
    """
    plt.plot([i for i in range(len(fitness_list))], fitness_list)
    plt.ylabel("Fitness - Distance")
    plt.xlabel("Iteration")
    plt.show()


def plotSA(cityName, latitude, longitude, country, fitness_list):
    """"""

    try:
        fig = plt.figure(figsize=(10, 5), constrained_layout=True)

        ax1, ax2 = fig.subplots(1,2)
        fig.suptitle(country + ' Journey')

        # use width and height instead of
        # (llcrnrlon=50.5, llcrnrlat=24.5, urcrnrlon=52.5, urcrnrlat=26.5,)

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
        #map.drawparallels(np.arange(-40, 61., 2.))
        #map.drawmeridians(np.arange(-20., 21., 2.))

        x, y = map(longitude, latitude)
        map.plot(x, y, 'bo', markersize=10)

        #for city, xpt, ypt in zip(cityName, x, y):
            #plt.text(xpt + 1000, ypt + 15000, city)

        map.plot(x, y, '*-'
                 , markersize=3
                 , linewidth=1
                 , color='r'
                 , markerfacecolor='b')

        #ax1.set_title("Learning Rate")
        plt.setp(ax1.set_title("Distance"), color='b')
        ax1.plot([i for i in range(len(fitness_list))], fitness_list)
        ax1.set_ylabel("Fitness - Distance")
        ax1.yaxis.label.set_color('red')
        ax1.set_xlabel("Iteration")
        ax1.xaxis.label.set_color('red')

        plt.show()
    except:
        EH()
