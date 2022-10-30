import json
file = open('Tentauppgifter/Filhantering/lösenordhantering/passworddb.json')
data = json.load(file)
file.close()

MasterPassword = input('Master Password: ')

if data['master_password'] == MasterPassword:
    print('SUCCESS: authorized')
    domain = input('Domain: ')
    if domain in data['passwords']:
        print('username: ' + str(data['passwords'][domain]['username']))
        print('password: ' + str(data['passwords'][domain]['password']))
    else:
        print('Error: unkown domain')
else:
    print('Error: Wrong password')