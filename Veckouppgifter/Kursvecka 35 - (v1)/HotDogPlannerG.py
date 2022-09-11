import math
print('\n---- HotDog Planner ----\nHow many students wants:')
HD2, HD3, VHD2, VHD3 = map(input, ['2 Meat HotDogs: ','3 Meat HotDogs: ','2 Vegan HotDogs: ','3 Vegan HotDogs: '])
if HD2.isnumeric() and HD3.isnumeric() and VHD2.isnumeric() and VHD3.isnumeric():
    TotHD, TotVHD, Drinks = [((int(HD2)*2)+(int(HD3)*3)), ((int(VHD2)*2)+(int(VHD3)*3)), (int(HD2)+int(HD3)+int(VHD2)+int(VHD3))]
    PackHD, PackVHD, PriVHDP, PriDr, = [(math.ceil(TotHD/8)), (math.ceil(TotVHD/4)), '-Vegan HotDog Packages: ', '-Number of Drinks: ']
    PriMHDP, SEK = ['-Meat HotDog Packages: ',((PackHD*20.95)+(PackVHD*34.95)+(Drinks*13.95))]
    print('\n',PriMHDP,PackHD,'\n',PriVHDP,PackVHD,'\n',PriDr,Drinks,'\n\n','-Price: ',SEK,' SEK\n')
else:
    print('Error: Please only input numbers.')