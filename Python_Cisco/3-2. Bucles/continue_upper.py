#Ejemplo 1
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
"""
user_word = input("Ingrese un nombre: ")
user_word = user_word.upper()
    # Completa el cuerpo del bucle for.
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        print(letter)
"""


#Ejemplo 2
word_without_vowels = ""
user_word = input("Ingrese un nombre: ")
user_word = user_word.upper()
    # Completa el cuerpo del bucle for.
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)

