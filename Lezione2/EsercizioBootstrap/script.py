'''
Costruire una pagina html fatta di:

    •un body dove il css impone il testo centrato
    •nel body mettere una griglia (grid layout di bootstrap)
    •le colonne della griglia sono delle card .
    
    Dividere la pagina html in tre blocchi, chiamati pag11 pag12 pag13 in modo 
    che valga la seguente relazione pag = pag11 + N*pag12 + pag13. 
    Per costruire i tre blocchi tenere conto di quanto discusso in classe. 
    Creare un semplice script in python che, assegnato un numero ad N, es. N = 3 genera la pagina html.     

'''
#Script Python

def genera_pagina(n: int):
    with open("pag11.html") as file:
        pag11 = file.read()

    with open("pag12.html") as file:
        pag12 = file.read()

    with open("pag13.html") as file:
        pag13 = file.read()

    pagina = pag11 + n*pag12 + pag13

    with open("pagina.html", "w") as file:
        file.write(pagina)

genera_pagina(3)