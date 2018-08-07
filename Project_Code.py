# Aztec Code

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 12:00:14 2018

@author: crich
"""

# In[ MODULES ]
import os
import pandas as pd

# In[ Directory Stuff ]
#os.getcwd()
#os.chdir()

# In[ DF MAIN ]

saferparks = pd.read_csv('C:/Users/crich/OneDrive/UCSD/Aztecs/Aztecs---Project-1/saferparks_dataset.csv')

bup = saferparks
# <codecell>


# In[ ORGANIZE MAIN ]

saferparks_grouped = saferparks.groupby('Device type').max()


# In[ EXAMPLE CODE ]
# =============================================================================
# 
DF['Employer'] = DF['Employer'].replace(
        {'Self Employed': 'Self-Employed', 'Self': 'Self-Employed'})
# 
# =============================================================================

# In[ BUILDER ]
saferparks['Device type'] = saferparks['Device type'].replace({
        # alphabatized by new Value var
        'Bumper car' : 'Car ride',
        'Go-kart' : 'Car ride',
        'Coaster - miscellaneous' : 'Coaster',
        'Coaster - wooden' : 'Coaster',
        'Coaster - 4th dimension' : 'Coaster',
        'Coaster - inverted' : 'Coaster',
        'Coaster - wild mouse' : 'Coaster',
        'Coaster - family/kiddie' : 'Coaster',
        'Coaster - zyklon' : 'Coaster',
        'Coaster - bobsled' : 'Coaster',
        'Coaster - flying' : 'Coaster',
        'Coaster - stand-up' : 'Coaster',
        'Coaster - suspended' : 'Coaster',
        'Coaster - pipeline' :'Coaster',
        'Coaster - mine train' : 'Coaster',
        'Bumper boat': 'Boat ride', 
        'Lazy river' : 'Boat ride',
#        'Inflatable - misc.' : 'Inflatable ' #check with team,
        'Spinning cups/tubs' : 'Spinning type ride',
         'Spinning ride - misc.' : ,
         
        })

# In[ STRING FINDER ]
# =============================================================================
# string = Any string you are searching for
# column = The column you are looking in
# =============================================================================

def string_finder(string, column):    
    device_list = []
    for device in saferparks[column]:
        if string in device:
            if device not in device_list:
                device_list.append(device)
    
    return device_list
# In[]
string_finder('Spin', 'Device type')
# In[]
