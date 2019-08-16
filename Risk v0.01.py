
# ██████╗ ██╗███████╗██╗  ██╗ 
# ██╔══██╗██║██╔════╝██║ ██╔╝
# ██████╔╝██║███████╗█████╔╝
# ██╔══██╗██║╚════██║██╔═██╗ 
# ██║  ██║██║███████║██║  ██╗
# ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝

# Ascii Letters from http://patorjk.com/software/taag
# ANSI Shadow font

# Summary here
#
#
#


# ██╗███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗███████╗
# ██║████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
# ██║██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║   ███████╗
# ██║██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
# ██║██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║   ███████║
# ╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝

from risk_constants import MAP_DICT

class Map():
    """ """
    def __init__(self):
        self.name = "RISK"
        self.continents = []
        self.create_continents()

    def create_continents(self):
        for continent_name, regions_dict in MAP_DICT.items():
            continent = Continent(continent_name, regions_dict)
            self.continents.append(continent)

class Continent():
    """ """
    def __init__(self, name, regions_dict):
        self.name = name
        self.regions = list()
        self.create_regions(regions_dict)

    def create_regions(self, regions_dict):
        for region_name, MAP_DICT in regions_dict.items():
            region = Region(region_name, MAP_DICT)
            self.regions.append(region)
        
class Region():
    """ """
    def __init__(self, name, MAP_DICT):
        self.name = name
        self.MAP_DICT = MAP_DICT


def gameLoop():

    # startwaarden
    """ Het aantal spelers en het niveau van de AI, mits aanwezig
        worden bepaalt."""

    print(15*'\n')
    print(GAMETITLE)
    print('version 0.idk')
    print(35*'-')
    
    print(7*'\n')
    
    player_amt = 3
    players = []
    
    for player in range(player_amt):
        print("GAME NOT IMPLEMENTED")







#████████╗███████╗███████╗████████╗    ███████╗████████╗██╗   ██╗███████╗███████╗
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔════╝╚══██╔══╝██║   ██║██╔════╝██╔════╝
#   ██║   █████╗  ███████╗   ██║       ███████╗   ██║   ██║   ██║█████╗  █████╗  
#   ██║   ██╔══╝  ╚════██║   ██║       ╚════██║   ██║   ██║   ██║██╔══╝  ██╔══╝  
#   ██║   ███████╗███████║   ██║       ███████║   ██║   ╚██████╔╝██║     ██║     
#   ╚═╝   ╚══════╝╚══════╝   ╚═╝       ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝     
                                                                                
# test the classes
def printMap():
    
    mapobj = Map()
    for continent in mapobj.continents:
        print(continent.name)
        for region in continent.regions:
            print("   ",region.name)
            for neighbour in region.MAP_DICT:
                print("      ",neighbour)
                
        print('\n',continent.name,'done')
        print(30*'-')



def Test_Stuff():
    # Test Map
    printMap()

#  =--

GAMETITLE="""
        ///////////////////////////\\
       /                            \\
      /  ██████╗ ██╗███████╗██╗  ██╗ \\
     /   ██╔══██╗██║██╔════╝██║ ██╔╝  \\
    /    ██████╔╝██║███████╗█████╔╝    \\
   /     ██╔══██╗██║╚════██║██╔═██╗     \\
  /      ██║  ██║██║███████║██║  ██╗     \\
 /       ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝      \\
/                                          \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  """
gameLoop()
