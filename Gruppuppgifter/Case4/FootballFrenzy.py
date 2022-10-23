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

def GetSeasons(id, key):
    api = requests.get(
        'http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api' + str(id))
    seasons = json.loads(api.text)[key]
    return seasons

while True:
    clear(True)
    UserInput = input('> ').lower()
    print(BreakLine('-'))
    if UserInput == 'list' or UserInput == 'l':
        Seasons =  GetSeasons('', 'seasons')
        for x in range(len(Seasons)):
            print('| ' + Seasons[x])
    elif UserInput == 'view' or UserInput == 'v':
        try:
            SelectedYear = input('> Year ')
            print(BreakLine('-'))
            
            scores = {}
            teams = GetSeasons('/' + SelectedYear, 'teams')
            
            for x in teams:
                scores[x] = {"Wins": 0, "Draws": 0, "Loss": 0, "Points": 0}
                    
            for x in range(len(GetSeasons('/' + SelectedYear, 'gamedays'))):
                GameDays = GetSeasons('/' + SelectedYear + '/' + GetSeasons('/' + SelectedYear, 'gamedays')[x], 'games')
                for y in range(len(GameDays)):
                    HomeTeam = GameDays[y]['score']['home']
                    AwayTeam = GameDays[y]['score']['away']
                    if HomeTeam['goals'] > AwayTeam['goals']:
                        scores[HomeTeam['team']]['Points'] += 3
                        scores[HomeTeam['team']]['Wins'] += 1
                        scores[AwayTeam['team']]['Loss'] += 1
                    elif HomeTeam['goals'] < AwayTeam['goals']:
                        scores[AwayTeam['team']]['Points'] += 3
                        scores[AwayTeam['team']]['Wins'] += 1
                        scores[HomeTeam['team']]['Loss'] += 1
                    else:
                        scores[AwayTeam['team']]['Draws'] += 1
                        scores[HomeTeam['team']]['Draws'] += 1
                        scores[AwayTeam['team']]['Points'] += 1
                        scores[HomeTeam['team']]['Points'] += 1

            print(f"{'Team' : <23}{'Wins' : <6}{'Draws' : <6}{'Losses' : <7}{'Points'}")
            SortedScores = dict(reversed(sorted(scores.items(), key=lambda x: (x[1]["Points"]))))
                
            for team in SortedScores:
                print(f"{team : <23}{SortedScores[team]['Wins'] : <6}{SortedScores[team]['Draws'] : <6}{SortedScores[team]['Loss'] : <7}{SortedScores[team]['Points']}")
                
        except json.decoder.JSONDecodeError:
            print('Sorry But you have entered an inavalid year')
    elif UserInput == 'exit' or UserInput == 'e':
        exit()
    else:
        print('Unkown command: ' + str(UserInput))
    
    input(BreakLine('-') + '\n' + 'Press enter to contiune...')