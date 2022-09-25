print('\n__ -- __ -- __ -- FAME MATCHER -- __ -- __ -- __')
print('Possible Genders: Male, Female\nPossible haircolors: Brown, Red, Gray, Black\nPossible Eyecolors: Brown, Blue, green\n')

a, b, c = map(input, ['Gender? ', 'Hair color? ', 'Eye color? '])
Gender, HairColor, EyeColor = (a, b, c)

class per:
    def __init__(self, name, lastname, gender, haircolor, eyecolor):
        self.name = name
        self.lname = lastname
        self.sex = gender
        self.hairc = haircolor
        self.eyec = eyecolor

persons =  [per('Daniel', 'RadCliffe', 'male','brown','brown'), # Daniel Radcliffe
            per('Rupert', 'Grint', 'male', 'red', 'blue'),  # Rupert Grint
            per('Emma', 'Watson', 'female', 'brown', 'brown'),  # Emma Watson
            per('Selena', 'Gomez', 'female', 'brown', 'brown'),  # Selena Gomez
            per('Bill', 'Gates', 'male', 'gray', 'blue'),  # Bill Gates
            per('Johnny', 'Depp', 'male', 'black', 'brown'),  # Johnny Depp
            per('Ann-Marie', 'Eklund Löwinder', 'female','brown','green'), # Anne-Marie Eklund Löwinder
            per('Linus', 'Torvalds', 'male', 'brown', 'brown'),  # Linus Torvalds
            per('Dennis', 'Ritchie', 'male', 'gray', 'brown'),  # Dennis Ritchie
            per('Guido', 'van Rossum', 'male','gray','blue')]

FoundPersons = [find for find in persons if find.sex == Gender.lower() and find.hairc == HairColor.lower() and find.eyec == EyeColor.lower()]

if len(FoundPersons) >= 1:
    print('\n --- Found some matches! --- \n')
    for find in FoundPersons:
        print(find.name+' '+find.lname)
    print('\n')
else: 
    print('\n --- Sorry! Not matches found :( --- \n')