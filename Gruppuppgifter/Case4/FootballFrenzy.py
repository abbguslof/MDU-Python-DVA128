import os, requests, json

def BreakLine(character):
    return str(character)*40

def clear(bool):
    os.system('cls' if os.name == 'nt' else 'clear')
    if bool:
        print(BreakLine('*') + '\n' +
              'Football Frenzy'.center(40) + '\n' + 'Stat Viewer'.center(40)
               + '\n' + '1.0.0'.center(40) + '\n' + BreakLine('-') + '\n' + 
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
                    for team in teams:
                        if HomeTeam['team'] == team:
                            if HomeTeam['goals'] > AwayTeam['goals']:
                                scores[team]['Points'] += 3
                                scores[team]['Wins'] += 1
                                scores[AwayTeam['team']]['Loss'] += 1
                            elif HomeTeam['goals'] < AwayTeam['goals']:
                                scores[AwayTeam['team']]['Points'] += 3
                                scores[AwayTeam['team']]['Wins'] += 1
                                scores[team]['Loss'] += 1
                            else:
                                scores[AwayTeam['team']]['Draws'] += 1
                                scores[team]['Draws'] += 1
                                scores[AwayTeam['team']]['Points'] += 1
                                scores[team]['Points'] += 1

            for x in teams:
                print('| ' + x + ' ' + str(scores[x]['Wins']) + ' ' + str(scores[x]['Draws']) + ' ' + str(scores[x]['Loss']) + ' ' + str(scores[x]['Points']))
                
        except json.decoder.JSONDecodeError:
            input(BreakLine('-') + '\n' + 'Sorry But you have entered an inavalid year' + '\n' + 'Press enter to contiune...')
    elif UserInput == 'exit' or UserInput == 'e':
        exit()
    else:
        input('Wrong please die')
    
    input(BreakLine('-') + '\n' + 'Press enter to contiune...')