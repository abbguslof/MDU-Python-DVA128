import os, requests, json

def BreakLine(character):
    return str(character)*48

def clear(bool):
    os.system('cls' if os.name == 'nt' else 'clear')
    if bool:
        print(BreakLine('*') + '\n' +
              'Football Frenzy'.center(48) + '\n' + 'Stat Viewer'.center(48)
               + '\n' + '1.0.0'.center(48) + '\n' + BreakLine('-') + '\n' + 
               '| List | List available seasons' + '\n' + '| View | View table for season'
               + '\n' + '| Exit | Exit program' + '\n' + BreakLine('-'))

def GetInformation(id, key):
    api = requests.get(
        'http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api' + str(id))
    seasons = json.loads(api.text)[key]
    return seasons

while True:
    clear(True)
    UserInput = input('> ').lower()
    print(BreakLine('-'))
    if UserInput == 'list' or UserInput == 'l':
        Seasons = GetInformation('', 'seasons')
        for Year in Seasons:
            print('| ' + Year)
    elif UserInput == 'view' or UserInput == 'v':
        try:
            SelectedYear = input('> Year ')
            scores, teams = {}, GetInformation('/' + SelectedYear, 'teams')
            print(BreakLine('-'))
            
            for team in teams:
                scores[team] = {"Wins": 0, "Draws": 0, "Loss": 0, "Points": 0}

            for gameday in GetInformation('/' + SelectedYear, 'gamedays'):
                GameDays = GetInformation('/' + SelectedYear + '/' + gameday, 'games')
                for index in GameDays:
                    HomeTeam, HomeT = index['score']['home'], scores[index['score']['home']['team']]
                    AwayTeam, AwayT = index['score']['away'], scores[index['score']['away']['team']]
                    if HomeTeam['goals'] > AwayTeam['goals']:
                        HomeT['Points'], HomeT['Wins'], AwayT['Loss'] = HomeT['Points'] + 3, HomeT['Wins'] + 1, AwayT['Loss'] + 1
                    elif HomeTeam['goals'] < AwayTeam['goals']:
                        AwayT['Points'], AwayT['Wins'], HomeT['Loss'] = AwayT['Points'] + 3, AwayT['Wins'] + 1, HomeT['Loss'] + 1
                    else:
                        AwayT['Draws'], HomeT['Draws'] = AwayT['Draws'] + 1, HomeT['Draws'] + 1
                        AwayT['Points'], HomeT['Points'] = AwayT['Points'] + 1, HomeT['Points'] + 1

            print(f"{'Team' : <23}{'Wins' : <6}{'Draws' : <6}{'Losses' : <7}{'Points'}")
            SortedScores = dict(sorted(scores.items(), reverse=True, key=lambda x: (x[1]["Points"])))

            for team in SortedScores:
                print('| ' + f"{team : <23}{SortedScores[team]['Wins'] : <7}{SortedScores[team]['Draws'] : <8}{SortedScores[team]['Loss'] : <6}{SortedScores[team]['Points']}")
                
        except json.decoder.JSONDecodeError:
            print('Sorry But you have entered an inavalid year')
    elif UserInput == 'exit' or UserInput == 'e':
        exit()
    else:
        print('Unkown command: ' + str(UserInput))
    
    input(BreakLine('-') + '\n' + 'Press enter to contiune...')