#Carafa 2: 300g, 65%
#Karamelovy slad: 600g, 76.8%
#Pale ale: 5000g, 81.5%

slady = [('Psenicny', 2700, 82.3),\
('PaleAle', 1800, 81.5)]

total_cukor = 0
for item in slady:
        cukor = item[1]/100*item[2]
        print item[0] + ': ' +str(cukor)+'g'
        total_cukor += cukor
print '\n'
print 'Total cukor: ' + str(total_cukor) + 'g'

print 'V 20l vody: ' + str(total_cukor/20)
print '\n'

vyska_vo_fermentacke = 2.5

vysledny_objem = 3.14 * 1.6 * 1.6 * vyska_vo_fermentacke
print 'Vysledny objem: ' + str(vysledny_objem) + 'l'

ucinnost_pre_objem = total_cukor/vysledny_objem
print '100% ucinnost pre vysledny objem: ' + str(ucinnost_pre_objem)

vysledna_hustota = 100
vysledna_ucinnost = vysledna_hustota/ucinnost_pre_objem 
print 'Vysledna ucinnotst: ' + str(vysledna_ucinnost*100)+'%\n\n'

vysledny_cukor = vysledna_hustota*vysledny_objem
print 'Vysledny cukor: ' +str(vysledny_cukor)+'g'










slady = [('Carafa2', 300, 65),\
('Karamel', 600, 76.8),\
('PaleAle', 5000, 81.5)]

total_cukor = 0
for item in slady:
        cukor = item[1]/100*item[2]
        print item[0] + ': ' +str(cukor)+'g'
        total_cukor += cukor
print '\n'
print 'Total cukor: ' + str(total_cukor) + 'g'

print 'V 20l vody: ' + str(total_cukor/20)
print '\n'

vyska_vo_fermentacke = 2.2

vysledny_objem = 3.14 * 1.6 * 1.6 * vyska_vo_fermentacke
print 'Vysledny objem: ' + str(vysledny_objem) + 'l'

ucinnost_pre_objem = total_cukor/vysledny_objem
print '100% ucinnost pre vysledny objem: ' + str(ucinnost_pre_objem)

vysledna_hustota = 190
vysledna_ucinnost = vysledna_hustota/ucinnost_pre_objem 
print 'Vysledna ucinnotst: ' + str(vysledna_ucinnost*100)+'%\n\n'

vysledny_cukor = vysledna_hustota*vysledny_objem
print 'Vysledny cukor: ' +str(vysledny_cukor)+'g'

print 'Vysledny cukor bez laktozy: ' + str(vysledny_cukor - 500)
print 'Vysledna husota bez laktozy: ' + str((vysledny_cukor-500)/vysledny_objem)
print 'Vysledna ucinnost bez laktozy ' + str((((vysledny_cukor-500)/vysledny_objem)/ucinnost_pre_objem)*100)
 

print '\n\n\n\n\n'
slady = [('PaleAle', 4000, 81.5)]

total_cukor = 0
for item in slady:
        cukor = item[1]/100*item[2]
        print item[0] + ': ' +str(cukor)+'g'
        total_cukor += cukor
print '\n'
print 'Total cukor: ' + str(total_cukor) + 'g'

print 'V 20l vody: ' + str(total_cukor/20)
print '\n'

vyska_vo_fermentacke = 1.5

vysledny_objem = 3.14 * 1.6 * 1.6 * vyska_vo_fermentacke
print 'Vysledny objem: ' + str(vysledny_objem) + 'l'

ucinnost_pre_objem = total_cukor/vysledny_objem
print '100% ucinnost pre vysledny objem: ' + str(ucinnost_pre_objem)

vysledna_hustota = 124
vysledna_ucinnost = vysledna_hustota/ucinnost_pre_objem 
print 'Vysledna ucinnotst: ' + str(vysledna_ucinnost*100)+'%'


