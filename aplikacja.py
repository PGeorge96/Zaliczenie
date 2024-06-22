import random


while True:
    print("                       ")
    print("Wybierz co chcesz zrobic")
    print("==========")
    print("1: Kostka")
    print("2: Ruletka")
    print("==========")
    print("                       ")

    menu = (input("Podaj liczbe:"))

    if menu == "1":
        print("Właśnie rzuciłeś kostką, twoja wylosowana liczba to:")
        print(random.randint(1, 6))

    if menu == "2":
    
        while True:
            kolor = (str(input("Podaj Kolor (czerwony,czarny,zielony):")))
            if kolor == "czerwony" or kolor == "czarny" or kolor == "zielony":
                break



        liczba = random.randint(0, 36)
        czarne_liczby = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

        if liczba in czarne_liczby:
            kolor_liczby = "czarny"
        
        else:
            kolor_liczby = "czerwony"
        
        if liczba == 0:
            kolor_liczby = "zielony"
        
        print(f"Wypadło {liczba} {kolor_liczby}")
        if kolor == kolor_liczby:
            print("GRATULACJE WYGRAŁEŚ!!!")
            
        else:
            print("PRZEGRAŁEŚ :(")
            


    if menu != "1" and menu != "2":
        print("                       ")
        print("!!!!!!!!!!!!!!!!!!!!!!")
        print("Podaj poprawna liczbe")
        print("!!!!!!!!!!!!!!!!!!!!!!")
        print("                       ")