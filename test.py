#smått test

print('Hej wälkommen till ditt loggbok du kommer får välja bland menyer, för att hantera ditt loggbok.')
print('\v')

menu = 0
answer1 = 'No, no, n, N' #Svar för nej ska leda ur programmen
answer2 = 'Yes, yes, y, Y' #svar för ja ska leda in till programmen
logg = [1 , 2 , 3 , 4 ] #planera att lopa listan med 'for x in logg  print(logg)'
datum = ['år ' 'månad ' 'dag']
write = 'x'


for x in logg:
    for y in datum:
        print(x, y)
        
print('välja bland loggarna: ')

val = input()
logg.insert = 1
logg.insert = 2
logg.insert = 3
logg.insert = 4