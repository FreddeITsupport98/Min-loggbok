
print('Hej wälkommen till ditt loggbok du kommer får välja bland menyer, för att hantera ditt loggbok.')
print('\v')

menu = 0
answer1 = 'No, no, n, N' #Svar för nej ska leda ur programmen
answer2 = 'Yes, yes, y, Y' #svar för ja ska leda in till programmen
logg = [1 , 2 , 3 , 4 ] #planera att lopa listan med 'for x in logg  print(logg)'
datum = ['år ' 'månad ' 'dag']
write = 'x'

while menu != 4: 
    print('Välja bland menyerna (1= Visa alla logg, 2= Skapa ny logg, 3= Spara loggfilen, 4= exit programmen')
    menu = int(input('Val: '))
    print('\v')

    if menu == 1:
        print('\v')
        print('Är du säker du har valt? Visa logg? Yes, yes, y, Y')
        answer = input('Yes or No ?: ')
        if answer2:
           for x in logg:
            for y in datum:
                print(x, y)

        elif answer1:
            menu = 0
            
        else:
            ValueError
            print('fel svar, endast: yes or no')
            menu == 1
       
    
    elif menu == 2:
        print('skapa ny logg') 
        print('\v')
        print('Är du säker du har valt? Visa logg? Yes, yes, y, Y')
        if answer2:
               for x in logg:
                for y in datum:
                    print(x, y)
            val = input(int('välja bland loggarna: '))
            logg.append = 1
            logg.append = 2
            logg.append = 3
            logg.append = 4

        elif answer1:
            menu = 0
            
        else:
            ValueError
            print('fel svar, endast: yes or no')
            menu == 2
    
    elif menu == 3:
        print('spara logen')
    
    elif menu == 4:
        print('exit')
        exit()
    
    else:
        print('Nånting gick fel')



# https://www.w3schools.com/python/python_lists.asp