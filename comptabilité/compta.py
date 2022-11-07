personnes = ["Stallman", "Torvalds", "Perlis", "Turing", "VomNeumann",
             "Iverson", "Boole", "Hamming", "Knuth", "Ritchie", "Thompson"]
salaires = [1500, 4700, 1500, 3800, 890, 4200, 480, 395, 1710, 1300, 3900]
primes = [190, 0, 117, 100, 500, 60, 0, 150, 0, 100, 180]

def salaire3000(personnes, salaires):
    salairePlus3000=[]
    for i, salaire in enumerate(salaires):
        if salaire>=3000:
            salairePlus3000.append(personnes[i])
    return salairePlus3000

def prime250(personnes, primes):
    primePlus250=[]
    for i, prime in enumerate(primes):
        if prime>=250:
            primePlus250.append(personnes[i])
    return primePlus250

def prime6Pourcent(personnes, salaires, primes):
    plus6Pourcent=[]
    for i, prime in enumerate(primes):
        if prime !=0 and (prime/salaires[i])>=0.06:
            plus6Pourcent.append(personnes[i])
    return plus6Pourcent

print(salaire3000(personnes,salaires))
print(prime250(personnes,primes))
print(prime6Pourcent(personnes, salaires, primes))

