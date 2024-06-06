import cs112_passer
import dfa_checker


c=cs112_passer.load_file("input") # spargem fisierul

s=cs112_passer.get_section_list(c) #extragem sectiunile

stari=cs112_passer.get_section_content(s, "States") #separam starile

transitions=cs112_passer.get_section_content(s,"Transitions") #separam tranzitii

curent=cs112_passer.get_section_content(s,'S') #separam starea initiala

curent=[curent[0]] #starea in care ne aflam

final=cs112_passer.get_section_content(s, 'F') #stari finale

def parcurgere(plecare):

    cv=[] #vectorul de stari curente
    acum=plecare #starea curenta

    for t in transitions: #parcurgem tranzitiile
        if plecare==t[0] and t[1]=='e': #verificam daca tranzitia este epsilon
            acum=parcurgere(t[2]) #apelam recursiv functia
            cv.append(acum) #adaugam starea curenta
    if acum==plecare: #daca nu s-a schimbat starea
        return acum #returnam starea
    return cv #returnam vectorul de stari

string="100"

urmator=[]

for s in string: #parcurgem stringul
    for t in transitions: #parcurgem tranzitiile
        pasi=0  #numarul de pasi
        if t[0] in curent and t[1]=='e' and t[2] not in curent: # verificam pasul de pe epsilon
            urmator.extend(parcurgere(t[0])) #apelam functia de parcurgere
            urmator.append(t[0]) #adaugam starea curenta
            curent=urmator.copy() #copiem in curent
        if t[0] in curent and t[1]==s: #verificam daca tranzitia este valida
            if t[0] in urmator: #verificam daca starea curenta se afla in urmator
                urmator[urmator.index(t[0])]=t[2] #daca da, o inlocuim
            else:
                urmator.append(t[2]) #daca nu, o adaugam
    curent=urmator.copy()

if curent in final: # verificare daca starea curenta este finala
    print("Acceptat")  # afisare acceptat
else: # altfel
    print("Respins") # afisare respins