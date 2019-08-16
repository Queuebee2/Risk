# Hello
#
#

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


from random import randint
from warnings import warn

# local
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




def assertNotGhostArmy(amount):
    """ funny named function to warn user an illegal number of dice is
        being used for the battle rolls"""
    if amount <= 0:
        warn("someone tries to fight with a nonexisting army!")
    else:
        pass
    
def battle(attacker_dice_amount, defender_dice_amount):
    """ takes two amounts for the amount of dice to use and
        returns the victor
        arguments"""

    
    amount_of_checks = min(attacker_dice_amount, defender_dice_amount)
    assertNotGhostArmy(amount_of_checks)
    
    attacks = [randint(1,6) for i in range(attacker_dice_amount)]
    defences = [randint(1,6) for i in range(defender_dice_amount)]

    print(35*"-")
    print("attacker rolls:",attacks)
    print("defender rolls:",defences)

    lost_attacker_soldiers = 0
    lost_defender_soldiers = 0

    for i in range(amount_of_checks):
        
        best_attack = popMax(attacks)
        best_defence = popMax(defences)
        
        attacker_wins = decide_result(best_attack, best_defence)

        
        if attacker_wins:
            print("attacker wins with", best_attack, 'vs', best_defence)
            lost_defender_soldiers += 1
        else:
            print("attacker loses with", best_attack, 'vs', best_defence)
            lost_attacker_soldiers += 1

    print("BATTLE RESULT")
    print('attacker lost:',lost_attacker_soldiers,
          '| defender lost:',lost_defender_soldiers)
    
    return lost_attacker_soldiers, lost_defender_soldiers

def decide_result(attack, defence):
    if defence >= attack:
        return False
    else:
        return True
        
    
def popMax(l):
    """
        arguments
        l = a list of integers

        returns
        the maximum number from a list and removes it from that list"""

    
    max_num = max(l)
    index_max_num = l.index(max_num)
    return l.pop(index_max_num)



#  ██████╗  █████╗ ███╗   ███╗███████╗    ██╗      ██████╗  ██████╗ ██████╗ 
# ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
# ██║  ███╗███████║██╔████╔██║█████╗      ██║     ██║   ██║██║   ██║██████╔╝
# ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝ 
# ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗╚██████╔╝╚██████╔╝██║     
#  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  

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

    # game 'opstellen'
    """ De onderdelen van de kaart worden geïnitialiseerd,
        - [x] continenten laden
        - [x] landen laden
        De land-kaarten worden verdeeld over de spelers en er word
        alvast automatisch op ieder land een bataljon bijhorend tot
        de eigenaar geplaatst.

        [!] De beginnende speler wordt random bepaalt"""

    # versterken
    """ Het aantal bataljons van de speler die aan zet is wordt als volgt
        bepaald:
        - regio_bataljons = player.owned_regions.count() / 3 = N bataljons (minimaal 3)
        - contintent_bataljons = sum([c[bataljonwaarde] for c in player.owned_continents])
    """
    # aanvalbeurt
    """ Hoe word gecheckt welke speler door welke speler 
        
    """
    # verzetten


#





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



def Test_Battle():
    battle(1, 1)
    battle(0, 0)
    battle(0, 10)
    battle(10, 0)
    battle(3, 2)
    battle(2, 3)
    
def Test_Stuff():
    # Test Map
    printMap()

    # Test Battle
    Test_Battle()



# ██╗  ██╗
# ██║  ██║
# ███████║
# ██╔══██║
# ██║  ██║
# ╚═╝  ╚═╝



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
