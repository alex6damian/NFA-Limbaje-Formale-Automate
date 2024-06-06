import cs112_passer

def validation(content):
    #verificare lungime alfabet
    if len(content['Sigma'])<1:
        return False
    #verificare unicitate aparitii simbol in alfabet
    if sorted(content['Sigma'])!=sorted(list(set(content['Sigma']))):
        return False
    #verificare unicitate aparitii stari
    if sorted(content['States']) != sorted(list(set(content['States']))):
        return False
    #verificare corectitudine tranzitii
    for elements in content['Transitions']:
        if elements[1] not in content['Sigma']:
            return False
        elif len(elements)!=3:
            return False
        elif elements[0] not in content['States'] or elements[2] not in content['States']:
            return False
    #verificare daca avem stare initiala sau stari finale
    if len(content['S'])==0 or len(content['F'])==0:
        return False
    if len(content['S'])>1:
        return False
    return True
file=cs112_passer.load_file("input.cfg")
section=cs112_passer.get_section_list(file)
if(validation(section)==True):
    print("NFA valid")
else:
    print("NFA invalid")