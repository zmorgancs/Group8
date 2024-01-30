import json
import requests
import csv

lstTokens = ["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"]
url = 'https://api.github.com/repos/scottyab/rootbeer/commits?path='
headers = {'Authorization': 'Bearer {}'.format(lstTokens)}
inputFile = "data/file_rootbeer.csv" # input path here, assumes CollectFiles.py has created file
outputFile = "data/authorsFileTouches_data.csv"

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

# script starts here
sourceFiles = []
outputCSV = open(outputFile, 'w')
writer = csv.writer(outputCSV)
row = ["FileName", "Author", "DateTime"]
writer.writerow(row)
with open(inputFile, 'r') as input:
    reader = csv.reader(input)
    next(reader, None) # skip header
# get file paths from csv created from CollectFiles.py
    for row in reader:
       if row: # if row is not empty
            sourceFiles.append(row[0])
# iterate file paths, output, write csv
    for filePath in sourceFiles:
        jsonData, ct = github_auth(url + filePath, lstTokens, 0)
        print("\nFile: " + filePath + "\nCommits:")
        for shaObject in jsonData:
            row = [filePath, shaObject['commit']['author']['name'], shaObject['commit']['author']['date']]
            writer.writerow(row)
            print(shaObject['commit']['author'])