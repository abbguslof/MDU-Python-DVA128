all_students = ['Anna', 'Lars', 'Eva', 'Mikael', 'Maria', 'Anders']
team_a = ['Anna', 'Maria']
team_b = ['Eva', 'Anders']

for x in all_students:
    if not (x in team_a + team_b):
        print(x)