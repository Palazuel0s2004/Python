beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Banda actualmente: ", beatles), print("")
print("="*10)

for i in range(2):
    n = input("Ingrese el nombre del siguiente miembro: ")
    beatles.append(n)
    print("Banda actualmente: ", beatles), print("")
    print("="*10)

del beatles[4]
print("Banda actualmente: ", beatles), print("")
print("="*10)
del beatles[3]
print("Banda actualmente: ", beatles), print("")
print("="*10)

beatles.insert(0, "Ringo Starr")
