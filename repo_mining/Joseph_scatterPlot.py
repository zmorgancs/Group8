import csv
import datetime
import matplotlib.pyplot as mpl
import numpy as np

x = []
y = []
inputFile = "data/authorsFileTouches_data.csv"
with open(inputFile, 'r') as input:
    reader = csv.reader(input)
    next(reader, None) # skip header
    prevFile = None
    prevAuthor = None
    xCoord = -1
    for row in reader: # parse csv
        if row: # skip row if empty
            file = row[0]
            author = row[1]
            if file == prevFile:
                y.append((int(datetime.datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%SZ").timestamp()) - 1400000000)*4)
                x.append(xCoord)
            else:
                xCoord += 1
                prevFile = file
                y.append((int(datetime.datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%SZ").timestamp()) - 1400000000)*4)
                x.append(xCoord)
mpl.scatter(x, y, s=10, alpha=0.5)
mpl.show()