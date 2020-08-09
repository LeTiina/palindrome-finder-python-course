# tee ratkaisu tänne
def palindromi(merkkijono):
    lista = []
    value = False
    b = -1
    a = 0
    for i in merkkijono:
        lista.append(i)
    
    while a < len(lista):
        if lista[a] == lista[b]:
            value = True
        else:
            value = False
            break
        a +=1
        b -=1
    
    return value

while True:
    sana = input("Anna sana")
    if palindromi(sana) == True:
        print(sana,"on palindromi!")
        break
    else:
        print("ei ollut palindromi")