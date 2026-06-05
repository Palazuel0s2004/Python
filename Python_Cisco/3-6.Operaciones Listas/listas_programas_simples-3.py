#Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.
#Los números que han salido sorteados son: 5, 11, 9, 42, 3, y 49.
#La pregunta es: ¿A cuántos números le has atinado?
#Este programa te dará la respuesta:

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)
 
#Nota:
#la lista drawn almacena todos los números sorteados;
#La lista bets almacena los números con que se juega;
#La variable hits cuenta tus aciertos.
#La output del programa es: 4.