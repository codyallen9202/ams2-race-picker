import random, sys
import pandas as pd

# defaults
carGrade = sys.maxsize
trackGrade = sys.maxsize

# csv files
carlist = pd.read_csv('carlist.csv')
tracklist = pd.read_csv('tracklist.csv')

# picking a random car
x = random.randrange(0, 86, 1)
selectedClass = carlist.iloc[x, 0]
carGrade = carlist.iloc[x, 1]

# picking a random track
while(trackGrade > carGrade):
    y = random.randrange(0, 107, 1)
    selectedTrack = tracklist.iloc[y, 0]
    trackGrade = tracklist.iloc[y, 1]

# picking a random date
m = random.randrange(1, 12, 1)
months = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October', 'November', 'December']
mon = months[m-1]

if (m == 2): maxDate = 28
elif (m == 9 or m == 4 or m == 6 or m == 11): maxDate =30
else: maxDate = 31

d = random.randrange(1, maxDate)

date = 'Date: {0} {1}'.format(mon, d)

# print
print('Car Class:', selectedClass)
print('Track:', selectedTrack)
print(date)