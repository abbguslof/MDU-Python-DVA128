import os, requests, json

def BreakLine(character):
    return str(character)*44

def get_score(team):
    return team['Points']

def clear(bool):
    os.system('cls' if os.name == 'nt' else 'clear')
    if bool:
        print(BreakLine('*') + '\n' +
              'Football Frenzy'.center(44) + '\n' + 'Stat Viewer'.center(40)
               + '\n' + '1.0.0'.center(44) + '\n' + BreakLine('-') + '\n' + 
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
                
            gamedays = GetSeasons('/' + SelectedYear, 'gamedays')
            
            for x in range(len(gamedays)):
                GameDays = GetSeasons('/' + SelectedYear + '/' + gamedays[x], 'games')
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

            print('Teams'.center(22) + '    W    D    L    P\n'+ BreakLine('-'))
            scoreslist = []
            i = 0
            for team in teams:
                scoreslist.append(scores[team])
                scoreslist[i]["Name"] = team 
                i += 1
            sortedScores = sorted(scoreslist, key=get_score, reverse=True)
            for team in sortedScores:
                print('| ' + team['Name'].ljust(24) + str(team['Wins']).ljust(4) + ' ' + str(team['Draws']).ljust(4) + ' ' + str(team['Loss']).ljust(4) + ' ' + str(team['Points']))
                
        except json.decoder.JSONDecodeError:
            input(BreakLine('-') + '\n' + 'Sorry But you have entered an inavalid year' + '\n' + 'Press enter to contiune...')
    elif UserInput == 'exit' or UserInput == 'e':
        exit()
    else:
        input('Unkown command')
    
    input(BreakLine('-') + '\n' + 'Press enter to contiune...')
