
print('Hej wälkommen till ditt loggbok du kommer får välja bland menyer, för att hantera ditt loggbok.')
print('\v')

menu = 0
answer1 = 'No, no, n, N'
answer2 = 'Yes, yes, y, Y'

while menu != 4: #Fel?
    print('Välja bland menyerna (1= Visa alla logg, 2= Skapa ny logg, 3= Spara loggfilen, 4= exit programmen')
    a = int(input('Val: '))
    print('\v')

    if menu == 1:
        print('\v')
        print('Är du säker du har valt? Visa logg? Yes, yes, y, Y')
        answer = input('Yes or No ?: ')
    
    elif menu == 2:
        print('skapa ny logg')
    
    elif menu == 3:
        print('spara logen')
    
    elif menu == 4:
        print('exit')
        exit()
    
    else:
        print('Nånting gick fel')