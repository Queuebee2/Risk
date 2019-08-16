
#Continents, Regions, Neighbours
MAP_DICT = {
    'NOORD-AMERIKA':{
        'ALASKA':{
                'KAMTSJATKA',
                'NOORDWEST-TERRITORIA',
                'ALBERTA',},
        'NOORDWEST-TERRITORIA':{
                'ALASKA',
                'ALBERTA',
                'GROENLAND',
                'ONTARIO',},
        'GROENLAND':{
                'ONTARIO',
                'QUEBEC',
                'IJSLAND',
                'NOORDWEST-TERRITORIA',},
        'ALBERTA':{
                'ALASKA',
                'NOORDWEST-TERRITORIA',
                'ONTARIO',
                'VERENIGDE STATEN(WEST)',},
        'ONTARIO':{
                'NOORDWEST-TERRITORIA',
                'ALBERTA',
                'GROENLAND',
                'QUEBEC',
                'VERENIGDE STATEN(WEST)',
                'VERENIGDE STATEN(OOST)',},
        'QUEBEC':{
                'ONTARIO',
                'GROENLAND',
                'VERENIGDE STATEN(OOST)',},
        'VERENIGDE STATEN(WEST)':{
                'ALBERTA',
                'ONTARIO',
                'VERENIGDE STATEN(OOST)',
                'MIDDEN-AMERIKA',},
        'VERENIGDE STATEN(OOST)':{
                'VERENIGDE STATEN(WEST)',
                'ONTARIO',
                'QUEBEC',
                'MIDDEN-AMERIKA',},
        'MIDDEN-AMERIKA':{
                'VERENIGDE STATEN(WEST)',
                'VERENIGDE STATEN(OOST)',
                'VENEZUELA',}
        },
    'ZUID-AMERIKA':{
        'VENEZUELA':{
                'MIDDEN-AMERIKA',
                'PERU',
                'BRAZILIË',},
        'PERU':{
                'VENEZUELA',
                'BRAZILIË',
                'ARGENTINIË',},
        'BRAZILIË':{
                'VENEZUELA',
                'PERU',
                'NOORD-AFRIKA',
                'ARGENTINIË',},
        'ARGENTINIË':{
                'PERU',
                'BRAZILIË',}
        },
    'AFRIKA':{
        'NOORD-AFRIKA':{
                'BRAZILIË',
                'WEST-EUROPA',
                'ZUID-EUROPA',
                'EGYPTE',
                'OOST-AFRIKA',
                'CENTRAAL-AFRIKA',},
        'EGYPTE':{
                'NOORD-AFRIKA',
                'ZUID-EUROPA',
                'MIDDEN-OOSTEN',
                'OOST-AFRIKA',},
        'OOST-AFRIKA':{
                'NOORD-AFRIKA',
                'EGYPTE',
                'CENTRAAL-AFRIKA',
                'MADAGASCAR',
                'ZUID-AFRIKA',},
        'CENTRAAL-AFRIKA':{
                'NOORD-AFRIKA',
                'OOST-AFRIKA',
                'ZUID-AFRIKA',},
        'ZUID-AFRIKA':{
                'CENTRAAL-AFRIKA',
                'OOST-AFRIKA',
                'MADAGASCAR',},
        'MADAGASCAR':{
                'OOST-AFRIKA',
                'ZUID-AFRIKA',}
        },
    'EUROPA':{
        'IJSLAND':{
                'GROENLAND',
                'SCANDINAVIË',
                'GROOT-BRITTANNIË',},
        'SCANDINAVIË':{
                'IJSLAND',
                'GROOT-BRITTANNIË',
                'NOORD-EUROPA',
                'OOST-EUROPA',},
        'GROOT-BRITTANNIË':{
                'IJSLAND',
                'SCANDINAVIË',
                'NOORD-EUROPA',
                'WEST-EUROPA',},
        'NOORD-EUROPA':{
                'GROOT-BRITTANNIË',
                'SCANDINAVIË',
                'OOST-EUROPA',
                'WEST-EUROPA',
                'ZUID-EUROPA',},
        'OOST-EUROPA':{
                'SCANDINAVIË',
                'NOORD-EUROPA',
                'ZUID-EUROPA',
                'OERAL',
                'KAZACHSTAN',
                'MIDDEN-OOSTEN',},
        'WEST-EUROPA':{
                'GROOT-BRITTANNIË',
                'NOORD-EUROPA',
                'ZUID-EUROPA',
                'NOORD-AFRIKA',},
        'ZUID-EUROPA':{
                'WEST-EUROPA',
                'NOORD-EUROPA',
                'OOST-EUROPA',
                'NOORD-AFRIKA',
                'EGYPTE',
                'MIDDEN-OOSTEN',}
        },
    'AZIË':{
        'OERAL':{
                'OOST-EUROPA',
                'KAZACHSTAN',
                'SIBERIË',
                'CHINA',},
        'SIBERIË':{
                'OERAL',
                'JAKOETSK',
                'TSJITA',
                'CHINA',
                'MONGOLIË',},
        'JAKOETSK':{
                'SIBERIË',
                'TSJITA',
                'KAMTSJATKA',},
        'KAMTSJATKA':{
                'JAKOETSK',
                'TSJITA',
                'MONGOLIË',
                'JAPAN',
                'ALASKA',},
        'TSJITA':{
                'SIBERIË',
                'JAKOETSK',
                'KAMTSJATKA',
                'MONGOLIË',},
        'MONGOLIË':{
                'SIBERIË',
                'TSJITA',
                'KAMTSJATKA',
                'CHINA',
                'JAPAN',},
        'JAPAN':{
                'KAMTSJATKA',
                'MONGOLIË',},
        'KAZACHSTAN':{
                'OOST-EUROPA',
                'OERAL',
                'CHINA',
                'INDIA',
                'MIDDEN-OOSTEN',},
        'MIDDEN-OOSTEN':{
                'EGYPTE',
                'ZUID-EUROPA',
                'OOST-EUROPA',
                'KAZACHSTAN',
                'INDIA',},
        'INDIA':{
                'MIDDEN-OOSTEN',
                'KAZACHSTAN',
                'CHINA',
                'ZUID-OOST-AZIË',},
        'CHINA':{
                'KAZACHSTAN',
                'OERAL',
                'SIBERIË',
                'MONGOLIË',
                'INDIA',
                'ZUID-OOST-AZIË',},
        'ZUID-OOST-AZIË':{
                'INDIA',
                'CHINA',
                'INDONESIË',}
        },
    'AUSTRALIË':{
        'INDONESIË':{
                'ZUID-OOST-AZIË',
                'NIEUW-GUINEA',
                'WEST-AUSTRALIË',
                'OOST-AUSTRALIË',},
        'NIEUW-GUINEA':{
                'INDONESIË',
                'WEST-AUSTRALIË',
                'OOST-AUSTRALIË',},
        'OOST-AUSTRALIË':{
                'INDONESIË',
                'NIEUW-GUINEA',
                'WEST-AUSTRALIË',},
        'WEST-AUSTRALIË':{
                'INDONESIË',
                'NIEUW-GUINEA',
                'OOST-AUSTRALIË',}
        }
}






































