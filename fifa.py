import csv


#for line in csv_reader:
    #print( line['Name'], line['Nationality'], line['Club'], line['Overall'])
    #print(line['Position'])
Napastnik=['ST','LF','CF','RF']
Skrzydlowy=['LW','RW','LM','RW']
Pomocnik=['LCM','CM','RCM','LDM','CDM','RDM','CAM']
Obronca=['LB','LCB','CB','RCB','RB','LWB','RWB']
class LST:
    rola=Napastnik
    nazwa=""
    liga=''
    kraj=""
    klub=""
    ocena=""
    pozycja="ST"
    LST_laczy_sie_z=[]
class RST:
    rola = Napastnik
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="ST"
    RST_laczy_sie_z=[]
class LM:
    rola = Skrzydlowy
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="LM"
    LM_laczy_sie_z=[]
class LCM:
    rola = Pomocnik
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="CM"
    LCM_laczy_sie_z=[]
class RCM:
    rola = Pomocnik
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="CM"
    RCM_laczy_sie_z=[]
class RM:
    rola = Skrzydlowy
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="RM"
    RM_laczy_sie_z=[]
class LB:
    rola = Obronca
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="LB"
    LB_laczy_sie_z=[]
class LCB:
    rola=Obronca
    nazwa = ""
    kraj = ""
    liga=''
    klub = ""
    ocena = ""
    pozycja="CB"
    LCB_laczy_sie_z=[]
class RCB:
    rola=Obronca
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="CB"
    RCB_laczy_sie_z=[]
class RB:
    rola=Obronca
    nazwa = ""
    kraj = ""
    liga=''
    klub = ""
    ocena = ""
    pozycja="RB"
    RB_laczy_sie_z=[]
class GK:
    rola="GK"
    nazwa = ""
    kraj = ""
    klub = ""
    liga=''
    ocena = ""
    pozycja="GK"
    GK_laczy_sie_z=[]

class Formacja4_4_2:
    nazwa=442
    Pozycje=[LST,RST,LM,RCM,LCM,RM,LB,LCB,RCB,RB,GK]

def polacz442():
   
    LST.LST_laczy_sie_z.append(LM)
    LST.LST_laczy_sie_z.append(LCM)
    LST.LST_laczy_sie_z.append(RST)

    RST.RST_laczy_sie_z.append(RM)
    RST.RST_laczy_sie_z.append(RCM)
    RST.RST_laczy_sie_z.append(LST)

    LM.LM_laczy_sie_z.append(LST)
    LM.LM_laczy_sie_z.append(LCM)
    LM.LM_laczy_sie_z.append(LB)

    LB.LB_laczy_sie_z.append(LM)
    LB.LB_laczy_sie_z.append(LCB)

    LCM.LCM_laczy_sie_z.append(LST)
    LCM.LCM_laczy_sie_z.append(LM)
    LCM.LCM_laczy_sie_z.append(RCM)
    LCM.LCM_laczy_sie_z.append(LCB)

    RCM.RCM_laczy_sie_z.append(RST)
    RCM.RCM_laczy_sie_z.append(LCM)
    RCM.RCM_laczy_sie_z.append(RM)
    RCM.RCM_laczy_sie_z.append(RCB)

    RM.RM_laczy_sie_z.append(RST)
    RM.RM_laczy_sie_z.append(RCM)
    RM.RM_laczy_sie_z.append(RB)

    RB.RB_laczy_sie_z.append(RM)
    RB.RB_laczy_sie_z.append(RCB)

    LCB.LCB_laczy_sie_z.append(LB)
    LCB.LCB_laczy_sie_z.append(RCB)
    LCB.LCB_laczy_sie_z.append(LCM)
    LCB.LCB_laczy_sie_z.append(GK)

    RCB.RCB_laczy_sie_z.append(RB)
    RCB.RCB_laczy_sie_z.append(RCM)
    RCB.RCB_laczy_sie_z.append(LCB)
    RCB.RCB_laczy_sie_z.append(GK)

    GK.GK_laczy_sie_z.append(RCB)
    GK.GK_laczy_sie_z.append(LCB)



#print(LST.LST_laczy_sie_z)


#print("LST laczy sie z:  ")
#for x in range(len(LST.LST_laczy_sie_z)):
   # print(LST.LST_laczy_sie_z[x].pozycja)


def generuj():
    for szukany_pilkarz in range(len(Formacja4_4_2.Pozycje)):
        baza_danych = open('data.csv', 'r')
        csv_reader = csv.DictReader(baza_danych)
        pilkarz_uzyty=[]

        for line in csv_reader:
            alert = 0
            for h in range(len(Formacja4_4_2.Pozycje)):

                if Formacja4_4_2.Pozycje[h].nazwa == line['Name']:
                    alert=1
            czy_dalej=0
            for r in range(len(Formacja4_4_2.Pozycje[szukany_pilkarz].rola)):
                if line['Position']==Formacja4_4_2.Pozycje[szukany_pilkarz].rola[r]:
                    czy_dalej=1

            if (Formacja4_4_2.Pozycje[szukany_pilkarz].pozycja==line['Position'] or czy_dalej==1)   and alert==0:





                Formacja4_4_2.Pozycje[szukany_pilkarz].nazwa=line['Name']
                Formacja4_4_2.Pozycje[szukany_pilkarz].kraj=line['Nationality']
                Formacja4_4_2.Pozycje[szukany_pilkarz].klub=line['Club']
                Formacja4_4_2.Pozycje[szukany_pilkarz].liga=znajdz_moja_lige(line['Club'])
                Formacja4_4_2.Pozycje[szukany_pilkarz].ocena=line['Overall']


                break
            #else:
                #for r in range(len(Formacja4_4_2.Pozycje[szukany_pilkarz].rola)):
                    #if Formacja4_4_2.Pozycje[szukany_pilkarz].rola[r] == line['Position']
polacz442()





def wyswietl_overall():
    overall=0
    for x in range(len(Formacja4_4_2.Pozycje)):
        overall=overall+int(Formacja4_4_2.Pozycje[x].ocena)
    print(overall/11)

def wyswietl_pilkarzy_w_formacji():
	for x in range(len(Formacja4_4_2.Pozycje)):
		print(Formacja4_4_2.Pozycje[x].pozycja)
		print(Formacja4_4_2.Pozycje[x].nazwa)
		print(Formacja4_4_2.Pozycje[x].liga)
lista_klubow=[]


list_lig=[]
def stworz_liste_lig():
	c = open('Ligi.txt', 'r').read().splitlines()
	for x in range(len(c)):
		list_lig.append(c[x])
	#print(list_lig)

	
def wczytaj_lige(szukanaliga):
	c = open(szukanaliga+'.txt', 'r').read().splitlines()
	for x in range(len(c)):
		lista_klubow.append(c[x])

def czy_ta_sama_liga(liga1,liga2):
	if liga1==liga2:
		return True
	else:
		return False
	
def znajdz_klub(nazwaklubu,nazwaligi):
	#print (len(lista_klubow))
	for x in range(len(lista_klubow)):
		#print("wchodzi")
		if nazwaklubu==lista_klubow[x]:
			#print(nazwaklubu+"\n")
			#print(nazwaligi)
			return True
def znajdz_moja_lige(moj_klub):
	
	nieznaleziono=0
	for x in range(len(list_lig)):
		liga=list_lig[x]
		wczytaj_lige(liga)
		if znajdz_klub(moj_klub,liga)==True:
			#list_lig.clear()
			nieznaleziono=1
			lista_klubow.clear()
			return liga
	if nieznaleziono==0:
		liga="blad"
		lista_klubow.clear()
		return liga
		

#argument=input("Wprowadź wartość:\n")
stworz_liste_lig()
generuj()
wyswietl_pilkarzy_w_formacji()
#wyswietl_overall()


#print(list_lig)
#stworz_liste_lig()
#znajdz_moja_lige('Legia Warszawa')

#wczytaj_lige('PREMIER LEAGUE')
#znajdz_moja_lige('Juventus')
