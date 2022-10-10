import csv

breakline = '\n'+'-'*25
options = ['get_id | Get person by ID','scan_f | Get people by FORENAME','scan_s | Get people by SURNAME','exit | Exit program',breakline.strip('\n')]
stripOptions = ['get_id', 'scan_f', 'scan_s', 'exit']

def check_input(x, options):
    if x in options: return options.index(x)

with open('database.csv', encoding='utf-8') as f:
    csvread = csv.reader(f)
    next = next(csvread)
    rowlist = []
    for row in csvread:
        value = {}
        for y, x in enumerate(next):
            value[x] = row[y]
        rowlist.append(value)

while True:
    print('\n'*15+'The data of the people'+breakline)
    for x in range(5):
        print(options[x])

    selection = input('menu > ').lower()

    if check_input(selection, stripOptions) == 0:
        id = int(input('ID > '))
        print('\nFORENAME: ', rowlist[id]['FORENAME'], '\nSURNAME: ', rowlist[id]['SURNAME'], '\nGENDER: ',rowlist[id]['GENDER'], '\nBIRTH YEAR: ', rowlist[id]['YEAR'], '\nID: ', rowlist[id]['ID'], '\n')
    elif check_input(selection, stripOptions) == 1:
        name = input('FORENAME > ').lower()
        for names in rowlist:
            if names['FORENAME'].lower() == name: print(', '.join(list(names.values())))
    elif check_input(selection, stripOptions) == 2:
        surname = input('SURNAME > ').lower()
        for surnames in rowlist:
            if surnames['SURNAME'].lower() == surname:print(', '.join(list(surnames.values())))
    elif check_input(selection, stripOptions) == 3:
        break
    else:
        print(breakline.strip('\n'),'\nERROR: unknown command', breakline)
    input('Press any key to continue...')