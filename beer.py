
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


