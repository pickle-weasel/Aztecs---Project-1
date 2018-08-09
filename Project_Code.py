# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 12:00:14 2018

@author: crich

# back_up = Backup DF if needed to revert to original dataframe
"""

# In[ MODULES ]
import os
import pandas as pd

# In[ Directory Stuff ]
#os.getcwd()
os.chdir('C:/Users/crich/Desktop/ucsd/chris/')

# In[ DF MAIN ]

saferparks = pd.read_csv('C:/Users/crich/OneDrive/UCSD/Aztecs/Aztecs---Project-1/saferparks_dataset.csv')

# In[ DF BUILDER ]

saferparks['Day'] =  [int(x.split('-')[0]) for x in saferparks.loc[:,'Date']]
saferparks['Week'] = [1+int(x)//7 for x in saferparks.loc[:,'Day']]

# In[ DF BUILDER ]


saferparks['Device type'] = saferparks['Device type'].replace({
        # alphabatized by new Value var
        'Bumper boat': 'Boat ride', 
        'Bumper car' : 'Car ride',
        'Bungee' : 'Gravity drop ride',
        'Carousel' : 'Car ride',
        'Claw-type' : 'Spinning type ride',
        'Climbing wall' : 'Play strucutre',
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
        
        'Drop tower' : 'Gravity drop ride',
        'Enterprise' : 'Spinning type ride',
        
        'Ferris/gondola wheel' : 'Flipping platform',
        'Flume ride' : 'Water ride',
        'Flying carpet ride' : 'Flipping platform',
        'Fun house' : 'Play strucure',
        
        'Giant swing' : 'Gravity drop ride',
        'Go-kart' : 'Car ride',
        
        'Hanglider ride' : 'Gravity drop ride',
        'Himalaya-type' : 'Spinning type ride',
        'Hurricane-type': 'Spinning type ride',
        
        'Inflatable bouncer': 'Inflatable',
        'Inflatable climb wall' : 'Inflatable',
        'Inflatable - misc.' : 'Inflatable', #check with team,
        'Inflatable slide' : 'Inflatable',
        'Inverter' : 'Flipping platform',
        
        'Lazy river' : 'Boat ride',
        'Looper' : 'Flipping platform',
        
        'Non-motorized spinners' : 'Flipping platform',
        
        'Monorail' : 'Safe ride',
        
        'Obstacle course' : 'Play structure',
        'Orbiter/octopus/remix' : 'Flipping platform',
        
        'Paratrooper-type' : 'Flipping platform',
        'Plane/jet/helicopter': 'Car ride',
        'Pirate ship' : 'Gravity drop ride',
        
        'Rafting ride' : 'Boat ride',
        'Ranger/kamikaze' : 'Flipping platform',
        'Robotic ride' : 'Coaster',
        'Roll-o-plane/booster/speed' : 'Flipping platform',
        'Rotor/gravitron' : 'Spinning type ride',
        'Roundabout' : 'Safe ride',
        
        'Simulator' : 'Car ride',
        'Sizzler/scrambler' : 'Spinning type ride',
        'Sky cycle' : 'Car ride',
        'Sky ride/ski lift': 'Car ride',
        'Slide' : 'Slide ride',
        'Shoot the chute' : 'Slide ride',
        'Snow tube/toboggan' : 'Slide ride',
        'Spinning cups/tubs' : 'Spinning type ride',
        'Spinning tower ride' : 'Spinning type ride',
        'Spinning pendulum' : 'Spinning type ride',
        'Spinning ride - misc.' : 'Spinning type ride',
        'Spinning track ride' : 'Spinning type ride',
        'Skydiving ride' : 'Gravity drop ride',
        'Swing ride' : 'Spinnin ride',
        
        'Tilt-a-whirl/waltzer': 'Spinning type ride',
        'Track ride' : 'Car ride',
        'Train' : 'Safe ride',
        'Trabant' : 'Spinning ride',
        'Tram/trolley' : 'Safe ride',
        'Tornado-type' : 'Spinning ride',

        'Water ski tow' : 'Car ride',
        'Water slide' : 'Slide ride',
        'Wave pool' : 'Play structure',
        'Wet Play' : 'Play structure',
        'Wheel w/spinning cars' : 'Car ride',
        'Whip' : 'Car ride'         
        })

saferparks['Category'] = saferparks['Category'].replace({
        
        'Collision: operator-controlled vehicles': 'Collision',
        'Collision: patron-controlled vehicles': 'Collision',
        
        'Derailment' : 'Equipment failure',
        
        'Extremity hit something outside carrier': 'Patron collided with object/other patron',
        
        'Go-kart crashed (no further description)' : 'Go-kart crash',
        'Go-kart or bumper car hit stationary object' : 'Go-kart crash',
       
        
        'Load/Unload: hit or pinched by restraint': 'Injury during loading/unloading',
        'Load/Unload: scrape or stumble': 'Injury during loading/unloading',
        
        'Other': 'Other/Unknown',
        
        'Patron flipped off inner tube or mat' : 'Fell or slid out of waterslide or snowtube', 
        'Patron hit by ride': 'Patron hit',
        'Patron hit something within ride vehicle': 'Patron hit',
        
        'Restraint too tight' : 'Load/Unload: hit or pinched by restraint',
        
        'Seatbelt abrasion or bruising' : 'Load/Unload: hit or pinched by restraint',
        
        'Unknown (not enough info)': 'Other/Unknown'
        
        })


saferparks.to_csv('cleaned.csv', sep = '\t', index = False)

# In[]

# In[]

saferparks = pd.read_csv('cleaned.csv', sep = '\t', index_col = None)
# In[]
# In[]
# In[ DF to read from ]
back_up = saferparks[['Date', 'State', 'Device type', 'Manufacturer',\
                  'Age', 'Accident Description', 'Injury', 'Category']]

# In[ ask team about this ]

#back_up.columns



# In[]
def string_finder(df, string, column):    
    device_list = []
    
    for device in df[column]:
        if string in device:
            if device not in device_list:
                device_list.append(device)
    
    return device_list

def unique_finder(df, column):
    unique_ = []
    for name in df[column].unique():
        unique_.append(name)
    
    return unique_

def data_grabber(string, df, column):
#    df.loc[df[column] == string,]
    return pd.DataFrame(df.loc[df[column] == string,])

#    **similar to**
#    string = 'Illness or neurological symptoms'
#    column = 'Category'
#    ehh_ = saferparks.loc[saferparks[column] == string]
# In[ FINDER ]

string = 'Illness or neurological symptoms'
column = 'Category'
ehh_ = saferparks.loc[saferparks[column] == string]

# In[]
explore = unique_finder(saferparks, 'Category')
# In[]
# In[]
# In[]


# In[]

# In[]
data = saferparks.groupby(['State', 'Manufacturer']).count()
# In[]
# In[]

# In[]
unique_injuries = unique_finder('Injury')
unique_categories = unique_finder('State')

#

# In[]

# In[]


