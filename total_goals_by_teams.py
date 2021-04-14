import requests

team = "Barcelona"
year = 2011


def getTotalGoals(team, year):
    sum = 0
    url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(team) + '&page=1'
    r = requests.get(url).json()
    total_pages = r['total_pages']
    per_page = r['per_page']
    for i in range(1, total_pages + 1):
        url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(
            team) + '&page=' + str(i)
        r = requests.get(url).json()
        try:

            for j in range(0, per_page):
                team1 = r['data'][j]['team1goals']
                sum += int(team1)
        except:
            pass

    url1 = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team2=' + str(team) + '&page=1'
    r1 = requests.get(url1).json()
    total_pages1 = r1['total_pages']
    per_page1 = r1['per_page']

    for i in range(1, total_pages1 + 1):
        url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team2=' + str(
            team) + '&page=' + str(i)
        r1 = requests.get(url).json()
        try:

            for j in range(0, per_page1):
                team2 = r1['data'][j]['team2goals']
                sum += int(team2)
        except:
            pass

    print(sum)


getTotalGoals(team, year)
