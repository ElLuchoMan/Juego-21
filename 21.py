from random import randint
def Mazo(hand,house,deal):
    for x in hand:
        if hand[hand.index(x)] in deal:
            deal.remove(hand[hand.index(x)])
    for x in house:
        if house[house.index(x)] in deal:
            deal.remove(house[house.index(x)])
    return deal

def CuentaMano(hand):
    if hand == []:
        return 0
    else:
        for i in hand:
            #hand.remove(i)##aqui esta el error
            return i+CuentaMano(hand[1:])


def Mano(hand,mazo):
    print("cantidad cartas mazo:")
    print(len(mazo))
    hand.append(mazo[randint(0,len(mazo))])
   
   
    return hand

def TomarMano(mano,rival):
    return Mano(mano,Mazo(mano,rival,[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]))

def juego(hand,house):
    print("Tienes las siguientes cartas:")
    print(hand)
    if CuentaMano(hand) > 21:
        print("HAS PERDIDO\n la casa gana con una cuenta de: ",CuentaMano(casa))
        
        return False
    else:
        print("Su cuenta es: ")
       
        print(CuentaMano(hand))
       # print(CuentaMano(house))
        print("La casa muestra una carta y su valor es: ",house[0])
        print( " ¿Desea tomar otra carta?")
        print("Y/N")
        if input() == 'y':
            hand=TomarMano(hand,house)
            juego(hand,house)
        else:
            if CuentaMano(hand)>CuentaMano(casa):
                print("HAS GANADO\n la casa pierde con una cuenta de: ",CuentaMano(casa))
                return True
            else:
                print("HAS PERDIDO\n la casa gana con una cuenta de: ",CuentaMano(casa))
                return True
        
print("EMPIEZA EL JUEGO:\n Repartiendo cartas...")
mano=[]
casa=[]
mano=TomarMano(mano,casa)
mano=TomarMano(mano,casa)
casa=TomarMano(casa,mano)
casa=TomarMano(casa,mano)


juego(mano,casa)
    
            
 # print(TomaMazo([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]))

