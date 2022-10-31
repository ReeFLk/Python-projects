# ce fichier rassemble quelques données utiles pour l'exercice

'''
Exercice 1:
fn+1=fn*2^(1/12)
fdo3=fdo2*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)*2^(1/12)
soit fdo3=fdo2*2
'''
# Exercice 2:a)


def freq(n):
    DO2 = 130.81278265029934
    if n == 0:
        return DO2
    else:
        return freq(n-1)*2**(1/12)


print(freq(48))

# Exercice 2:b)


def list_freq(n):
    global frequence
    frequence = []
    for i in range(n):
        frequence.append(freq(i))
    return frequence


print(list_freq(48))

# Exercice 2:c)
base = ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA',
        'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']
notes_gammes = [base[i]+str(e) for e in range(1, 5) for i in range(len(base))]
print(notes_gammes)

# Exercice 2:d)

notes = {notes_gammes[i]: frequence[i] for i in range(len(notes_gammes))}
print(notes)


"""
# # Faire siffler "Au Clair de la Lune" à un Python
do=130.81278265029934  # fréquence du DO2

base = ['DO', 'DO#', 'RE','RE#', 'MI', 'FA',
        'FA#', 'SOL','SOL#', 'LA', 'LA#', 'SI']

# durées des notes
dt = 0.5    # permet de régler la rapidité d'exécution du morceau
n = dt      # durée d'une noire (= 1 temps)
b = 2*dt    # durée d'une blanche (= 2 temps)
bp = 3*dt   #durée d'une blanche pointée (= 3 temps)

# codage du début d'Au Clair de la Lune dans une liste de tuples :
chanson = [('DO3',n), ('DO3',n), ('DO3',n), ('RE3',n), ('MI3', b),
           ('RE3',b), ('DO3',n), ('MI3', n), ('RE3',n), ('RE3',n),
           ('DO3',bp), ('silence', dt)]

# Utilisation du module pyo :
# tester ce bout de code (à recopier dans un autre fichier.
# On doit entendre distinctement trois notes : hausser
# le volume du PC si nécessaire

from pyo import *
import time
s = Server(duplex=0)
s.boot().start()

# série de notes à jouer
a = Sine(880, 0, 0.1).out()
time.sleep(0.5)
a = Sine(440, 0, 0.1).out()
time.sleep(0.5)
a = Sine(880, 0, 0.1).out()
time.sleep(0.5)

s.stop()


# Résultats à obtenir :
# Question 2.b :
# Pour ceux qui n'arrivent pas à créer la liste frequences,
# recopier cette liste pour l'utiliser dans les questions suivantes :

frequences =[130.81278265029934, 138.59131548843607, 146.83238395870382,
             155.5634918610405, 164.81377845643502, 174.614115716502,
             184.99721135581726, 195.99771799087472, 207.65234878997265,
             220.00000000000009, 233.08188075904505, 246.94165062806215,
             261.62556530059874, 277.1826309768722, 293.6647679174077,
             311.12698372208104, 329.6275569128701, 349.22823143300405,
             369.99442271163457, 391.9954359817495, 415.30469757994535,
             440.0000000000002, 466.16376151809015, 493.8833012561244,
             523.2511306011976, 554.3652619537446, 587.3295358348156,
             622.2539674441624, 659.2551138257405, 698.4564628660085,
             739.9888454232696, 783.9908719634994, 830.6093951598912,
             880.000000000001, 932.327523036181, 987.7666025122495,
             1046.5022612023959]

# Question 2.c :
# Pour ceux qui n'arrivent pas à créer la liste notes_gammes,
# recopier cette liste pour l'utiliser dans les questions suivantes :

notes_gammes = ['DO1', 'DO#1', 'RE1', 'RE#1', 'MI1', 'FA1', 'FA#1',
                'SOL1', 'SOL#1', 'LA1', 'LA#1', 'SI1', 'DO2', 'DO#2',
                'RE2', 'RE#2', 'MI2', 'FA2', 'FA#2', 'SOL2', 'SOL#2',
                'LA2', 'LA#2', 'SI2', 'DO3', 'DO#3', 'RE3', 'RE#3',
                'MI3', 'FA3', 'FA#3', 'SOL3', 'SOL#3', 'LA3', 'LA#3',
                'SI3']

# Question 2.d :
# Pour ceux qui n'arrivent pas à créer le dictionnaire final 'notes'
# le recopier pour l'utiliser dans les questions suivantes :

notes = {'DO1': 130.81278265029934, 'DO#1': 138.59131548843607,
         'RE1': 146.83238395870382, 'RE#1': 155.5634918610405,
         'MI1': 164.81377845643502, 'FA1': 174.614115716502,
         'FA#1': 184.99721135581726, 'SOL1': 195.99771799087472,
         'SOL#1': 207.65234878997265, 'LA1': 220.00000000000009,
         'LA#1': 233.08188075904505, 'SI1': 246.94165062806215,
         'DO2': 261.62556530059874, 'DO#2': 277.1826309768722,
         'RE2': 293.6647679174077, 'RE#2': 311.12698372208104,
         'MI2': 329.6275569128701, 'FA2': 349.22823143300405,
         'FA#2': 369.99442271163457, 'SOL2': 391.9954359817495,
         'SOL#2': 415.30469757994535, 'LA2': 440.0000000000002,
         'LA#2': 466.16376151809015, 'SI2': 493.8833012561244,
         'DO3': 523.2511306011976, 'DO#3': 554.3652619537446,
         'RE3': 587.3295358348156, 'RE#3': 622.2539674441624,
         'MI3': 659.2551138257405, 'FA3': 698.4564628660085,
         'FA#3': 739.9888454232696, 'SOL3': 783.9908719634994,
         'SOL#3': 830.6093951598912, 'LA3': 880.000000000001,
         'LA#3': 932.327523036181, 'SI3': 987.7666025122495,
         'silence': 10}"""
