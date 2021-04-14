import requests
import json

def getNumDraws(year):
    url = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year)
    response = requests.get(url)
    result = json.loads(response.content)
    current_page = 1
    total_page_url = result['total_pages']
    total = 0
    for i in range(0, 12):
        url = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={1}".format(
            year, i, i)
        response = requests.get(url)
        result = json.loads(response.content)
        total += result['total']

    print(total)
getNumDraws(2011)