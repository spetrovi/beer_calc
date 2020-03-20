
def calculate2(nazov, slady, objem, hustota):
    print nazov
    total_cukor = 0
    for item in slady:
        cukor = item[1]/100*item[2]
        print item[0] + ': ' +str(cukor)+'g'
        total_cukor += cukor
    #print 'Total cukor: ' + str(total_cukor) + 'g'
    #print 'V 20l vody: ' + str(total_cukor/20)
    vysledny_objem = objem
    print 'Vysledny objem: ' + str(vysledny_objem) + 'l'
    ucinnost_pre_objem = total_cukor/vysledny_objem


    print 'Vysledna hustota: ' + str(hustota)
    vysledna_ucinnost = hustota/float(ucinnost_pre_objem)
    print 'Vysledna ucinnost: ' + str(vysledna_ucinnost*100)+'%'

    vysledny_cukor = hustota*vysledny_objem
    #print 'Vysledny cukor: ' +str(vysledny_cukor)+'g'
    print '\n'

def calculate(nazov, slady, vyska, hustota):
    print nazov
    total_cukor = 0
    for item in slady:
        cukor = item[1]/100*item[2]
        print item[0] + ': ' +str(cukor)+'g'
        total_cukor += cukor
    #print 'Total cukor: ' + str(total_cukor) + 'g'
    #print 'V 20l vody: ' + str(total_cukor/20)
    vysledny_objem = 3.14 * 1.6 * 1.6 * vyska
    print 'Vysledny objem: ' + str(vysledny_objem) + 'l'
    ucinnost_pre_objem = total_cukor/vysledny_objem


    print 'Vysledna hustota: ' + str(hustota)
    vysledna_ucinnost = hustota/ucinnost_pre_objem 
    print 'Vysledna ucinnost: ' + str(vysledna_ucinnost*100)+'%'

    vysledny_cukor = hustota*vysledny_objem
    #print 'Vysledny cukor: ' +str(vysledny_cukor)+'g'
    print '\n'


nazov = 'Simcoe Smash'
slady = [('PaleAle', 4000, 81.5)]
vyska = 1.5
hustota = 124
calculate(nazov, slady, vyska, hustota)

nazov = 'Nox'
slady = [('Carafa2', 300, 65),\
('Karamel', 600, 76.8),\
('PaleAle', 5000, 81.5)]
vyska = 2.2
hustota = 167
calculate(nazov, slady, vyska, hustota)

nazov = 'Siligo'
slady = [('Psenicny', 2700, 82.3),\
('PaleAle', 1800, 81.5)]
vyska = 2.5
hustota = 100
calculate(nazov, slady, vyska, hustota)

nazov = 'Laponikka'
slady = [('PaleAle', 4000, 81.5)]
vyska = 2.2
hustota = 138
calculate(nazov, slady, vyska, hustota)

nazov = 'Dormiens'
slady = [('Simpsons', 400, 65),\
('PaleAle', 3600, 81.5)]
vyska = 2.8
hustota = 100
calculate(nazov, slady, vyska, hustota)

nazov = 'Avis'
slady = [('PaleAle', 4000, 79)]
objem = 24
hustota = 90
calculate2(nazov, slady, objem, hustota)

nazov = 'psnc'
slady = [('Psenicny', 3000, 82.3),\
('PaleAle', 2000, 81.5)]
objem = 24
hustota = 101
calculate2(nazov, slady, objem, hustota)

nazov = 'Vajano'
slady = [('PaleAle', 5000, 81.5)]
objem = 24
hustota = 120
calculate2(nazov, slady, objem, hustota)


nazov = 'Pumpkin'
slady = [('PaleAle', 5000, 81.5), ('Carabelge', 300, 74)]
objem = 26
hustota = 98
calculate2(nazov, slady, objem, hustota)

nazov = 'PumpkinII'
slady = [('PaleAle', 5000, 81.5), ('Mnichov', 1000, 80), ('Caraaroma', 300, 74)]
objem = 28
hustota = 129
calculate2(nazov, slady, objem, hustota)

nazov = 'Araga'
slady = [('PaleAle', 6000, 81.5)]
objem = 26
hustota = 126
calculate2(nazov, slady, objem, hustota)

nazov = 'BalticP Porter'
slady = [('Mnichovsky', 7000, 80), ('Plzensky', 3500, 81.1), ('Karamelovy', 500, 76.8), ('Carafa 2', 500, 65)]
objem = 26
hustota = 220
calculate2(nazov, slady, objem, hustota)

nazov = 'Orchestree'
slady = [('PaleAle', 5000, 81.5), ('Carahell', 400, 74)]
objem = 26

nazov = 'Medovina'
slady = [('Med', 5000, 100)]
objem = 20
hustota = 250
calculate2(nazov, slady, objem, hustota)

nazov = 'Nelson Ale'
slady = [('Pale Ale', 5500, 81.5)]
objem = 26
hustota = 115
calculate2(nazov, slady, objem, hustota)

nazov = 'Laponika III'
slady = [('Pale Ale', 5500, 81.5)]
objem = 26
hustota = 115
calculate2(nazov, slady, objem, hustota)

nazov = 'Laponika IV'
slady = [('Pale Ale', 5000, 81.5),  ('Carahell', 400, 74)]
objem = 26
hustota = 110
calculate2(nazov, slady, objem, hustota)

nazov = 'Laponika V'
slady = [('Pale Ale', 11000, 81.5)]
objem = 55
hustota = 113
calculate2(nazov, slady, objem, hustota)

nazov = 'Ocistne'
slady = [('Pale Ale', 5000, 81.5)]
objem = 26
hustota = 110
calculate2(nazov, slady, objem, hustota)

nazov = 'Bruno\'s Beer'
slady = [('Pale Ale', 5000, 81.5),  ('Carahell', 400, 74)]
objem = 26
hustota = 110
calculate2(nazov, slady, objem, hustota)

nazov = 'Cherry'
slady = [('Pale Ale', 5000, 81.5)]
objem = 26
hustota = 108
calculate2(nazov, slady, objem, hustota)

nazov = 'Kolaudackove'
slady = [('Pale Ale', 5000, 81.5)]
objem = 26
hustota = 110
calculate2(nazov, slady, objem, hustota)


nazov = 'Brusi Pekko'
slady = [('Pale Ale', 5000, 81.5), ('Carahell', 500, 74)]
objem = 26
hustota = 125
calculate2(nazov, slady, objem, hustota)

nazov = 'Brusi Rakau'
slady = [('Pale Ale', 5000, 81.5), ('Carahell', 500, 74)]
objem = 26
hustota = 125
calculate2(nazov, slady, objem, hustota)

nazov = 'Brusi Cascade'
slady = [('Pale Ale', 5000, 81.5), ('Carahell', 500, 74)]
objem = 26
hustota = 125
calculate2(nazov, slady, objem, hustota)


nazov = 'Stout'
slady = [('Pale Ale', 5000, 81.5), ('Carafa2', 400, 65),('Karamel', 500, 76.8)]
objem = 26
hustota = 135
calculate2(nazov, slady, objem, hustota)


nazov = 'Dvojky'
slady = [('Pale Ale', 3500, 81.5), ('Caraaroma', 500, 74), ('Vytazok', 500, 100)]
objem = 25
hustota = 135
calculate2(nazov, slady, objem, hustota)

nazov = 'Milkshake'
slady = [('Pale Ale', 5000, 81.5), ('Psenicny', 500, 82.3), ('Dextroza', 500, 100), ('Laktoza', 500, 100)]
objem = 26
hustota = 170
calculate2(nazov, slady, objem, hustota)





