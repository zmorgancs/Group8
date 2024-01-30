import json
import requests
import csv
import os
from collections import defaultdict

directory = "/Users/codystumbough/Documents/Repos/CS472-Project/repo_mining"
if not os.path.exists("data"):
 os.makedirs("data")

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

def get_languages(repo, lsttokens, ct):
    language_url = 'https://api.github.com/repos/' + repo + '/languages'
    language_data, ct = github_auth(language_url, lsttokens, ct)
    return list(language_data.keys()), ct

def sourceFile(filename, language):
    extensions = {
        'Python': ['.py'],
        'Java': ['.java'],
        'C++': ['.cpp'],
        'Kotlin': ['.kt']
    }
    extension = os.path.splitext(filename)[1]
    for lang in language:
        if extension in extensions.get(lang, []):
            return True
    return False

# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter
    languages, ct = get_languages(repo, lsttokens, ct)
    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)


                filesjson = shaDetails.get('files', [])
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    if sourceFile(filename, languages):
                        dictfiles[filename].append(
                            {
                                'sha': sha,
                                'author': shaObject['commit']['author']['name'],
                                'date': shaObject['commit']['author']['date']
                            }
                        )
                        print(filename)
                    #dictfiles[filename] = dictfiles.get(filename, 0) + 1
                #    print(filename)
            ipage += 1
    except Exception as e:
        print(f"Error receiving data: {e}")
        exit(0)

# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'

# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["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"]
dictfiles = defaultdict(list)
countfiles(dictfiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictfiles)))

file = repo.split('/')[1]

# change this to the path of your file
fileOutput = directory + '/data/file_' + file + '.csv'
rows = ['Filename', 'Author', 'Date']
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

for filename, touches in dictfiles.items():
    for touch in touches:
        writer.writerow([filename, touch['author'], touch['date']])

bigcount = None
bigfilename = None
for filename, touches in dictfiles.items():
    count = len(touches)
    if bigcount is None or count > bigcount:
        bigcount = count
        bigfilename = filename
fileCSV.close()
print('The file ' + bigfilename + ' has been touched ' + str(bigcount) + ' times.')