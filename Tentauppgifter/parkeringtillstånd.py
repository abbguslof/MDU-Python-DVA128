granted_parking_permits = ['910101-1234', '820202-5678']

print('_ _- - Parking Permit - -_ _')
print('Grant | Grant parking permit')
print('Check | Check if parking permit granted\n')

def grant(user):
    if user not in granted_parking_permits:
        granted_parking_permits.append(user)
        return user + ' is now granted'
    else:
        return user + ' is already granted'

def check(user):
    if user in granted_parking_permits:
        return user + ' is granted'
    else:
        return user + ' is not granted'

while True:
    selection = input('> ').lower()
    if selection == 'check':
        isgranted = input('> ')
        print(check(isgranted))
    elif selection == 'grant':
        grant1 = input('> ')
        print(grant(grant1))