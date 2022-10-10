today, tomorrow, later = ['Today: '], ['Tomorrow: '], ['Later: ']
info, lastinput = ['\n n | Next day\n','c | Change goal\n', 'e | Exit program\n'], ''

while True:
    print(('\n'*15),'.: Three day planner :.\n')
    for i in [today, tomorrow, later]:
        print(*i)
    print(('-'*30), *info, ('-'*30))

    selection = input('\nOperation > ').lower()
    # Choosen to not for example append a task from later to today if user would like to have a resting(blank) day.
    if selection == 'n':
        if len(today) > 1:
            del today[1]
        if len(tomorrow) > 1:
            today.append(tomorrow[1])
            del tomorrow[1]
        if len(later) > 1:
            tomorrow.append(later[1])
            del later[1]
        print('\n'*15)
    elif selection == 'c':
        print('\n',('-'*30),('\n'*15),'Changing a goal!')
        print('\n t | Today\n to | Tomorrow\n l | Later\n')
        changeday = input('What day? > ').lower()
        
        def selection_function(day):
            if len(day) > 1: 
                del day[1]
            print('\n Changing '+str(day[0].split(':')[0])+'s'+' goal.\nWhat would you like it to be?')
            day.append(input('> '))
            
        if changeday == 't':
            selection_function(today)
        elif changeday == 'to':
            selection_function(tomorrow)
        elif changeday == 'l':
            selection_function(later)

    elif selection == 'e':
        print('\nExiting program.')
        break