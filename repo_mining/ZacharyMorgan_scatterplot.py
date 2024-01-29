import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.colors as colors
import matplotlib.cm as cm
import pandas as pd

# If you are using jupyter to run this (this was my method), uncomment the following line:
data = pd.read_csv('file_rootbeer.csv')

# If you are not using jupyter, uncomment the following line:
# data = pandas.read_csv(r'data\file_rootbeer.csv')

dateToday = datetime.today().strftime('%Y-%m-%d')

data['Time'] = pd.to_datetime(data['Time'], format='%Y-%m-%d')
data['TimeFormat'] = data['Time'].astype(str).str[:10]
weeks = []

for i in data.index:
    curr = datetime.strptime(dateToday, '%Y-%m-%d')
    commDate = data['TimeFormat'][i]
    commDate = datetime.strptime(commDate, '%Y-%m-%d')
    diff = curr - commDate
    weeks.append(diff.days//7)

data['Weeks'] = weeks

fileNumbers = []
fileDict = {val: idx for idx, val in enumerate(data['Filename'].unique())}
for i in data.index:
    grabName = data['Filename'][i]
    fileNumbers.append(fileDict.get(grabName))
data['FileNumber'] = fileNumbers

# Make a dictionary and match authors with an individual color and store it in a color array
authorColor = []
authDict = {val: idx for idx, val in enumerate(data['Author'].unique())}
for i in data.index:
    grabName = data['Author'][i]
    authorColor.append(authDict.get(grabName))

# Random color hex values made with a generator
colorMapping = np.array(['#FF5733', '#FFC300', '#FF3333', '#33FF57', '#3366FF', '#9933FF', '#33FFC3',
                         '#33FF99', '#FF33C7', '#33CCFF', '#33FF33', '#FF3366', '#FF9933', '#336633',
                         '#663399'])

plt.scatter(data['FileNumber'], data['Weeks'], c = colorMapping[authorColor])
plt.title("Repository Activity")
plt.xlabel("File")
plt.ylabel("Weeks")
plt.show()
