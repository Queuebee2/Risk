
# Risk will be here


Continents = {"Noord-Amerika":["Alaska","Quebec"],
              "Zuid-Amerika":["Brazilië","Peru"]}

class Map():
    """ """
    def __init__(self):
        self.name = "RISK"
        self.continents = list()
        self.create_continents()


    def create_continents(self):
        for continent_name, regions in Continents.items():
            continent = Continent(continent_name, regions)
            self.continents.append(continent)


class Continent():
    """ """
    def __init__(self, name, regions):
        self.name = name
        self.regions = list()
        self.create_regions(regions)

    def create_regions(self, regions):
        for region_name in regions:
            region = Region(region_name)
            self.regions.append(region)


class Region():
    """ """
    def __init__(self, name):
        self.name = name


# test the classes
def printMap():
    mapobj = Map()
    for continent in mapobj.continents:
        print(continent.name)
        for region in continent.regions:
            print("  ",region.name)


printMap()
