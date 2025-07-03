import random
import pandas as pd

# csv files
carlist = pd.read_csv('carlist.csv')
tracklist = pd.read_csv('tracklist.csv')

# picking a random car
x = random.randrange(0, 44, 1)
selectedClass = carlist.iloc[x, 0]
carGrade = carlist.iloc[x, 1]

trackGrade = 5

# picking a random track
while(trackGrade > carGrade):
    y = random.randrange(0, 107, 1)
    selectedTrack = tracklist.iloc[y, 0]
    trackGrade = tracklist.iloc[y, 1]

print('Car Class:', selectedClass)
print('Track:', selectedTrack)