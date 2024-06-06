def load_file(file_name): #extrage informatia din fisier
    with open(file_name, 'r') as file:
        continut=[]
        for lines in file:
            lines=lines.strip()
            if '#' in lines:
                continue
            else:
                continut.append(lines)
        return continut
def get_section_list(content): #separa datele
    sections={}
    elements=[]
    sections['F']=[] #initializare stari finale
    sections['S']=[] #initializare stari initiale
    name='a'
    #parcurgere fisier
    for lines in content:
        if lines[-1]==":":
            lines = lines[:len(lines) - 1]
            name = lines.strip()
            elements = []
        #citire pana la stop
        elif lines!='Stop':
            if ' ' in lines or ',' in lines:
                lines=lines.split(",")
                lines=[item.strip() for item in lines]
                if 'S' in lines and 'F' in lines:
                    sections['S'].append(lines[0])
                    sections['F'].append(lines[0])
                    lines=lines[0]
                elif 'S' in lines and len(lines)==2: #gasire stari initiale
                    sections['S'].append(lines[0])
                    lines = lines[0]
                elif 'F' in lines and len(lines)==2: #gasire stari finale
                    sections['F'].append(lines[0])
                    lines = lines[0]
            elements.append(lines)
        elif lines=='Stop': #adaugare elemente in dictionar
            sections[name]=elements
    return sections
def get_section_content(content, section_name): #obtinere valori ale unei sectii
    return content[section_name]
'''
alfabet
stari(finale,initiale)
tranzitii
'''