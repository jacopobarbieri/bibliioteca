#Progetto didattico
libri=[]
def aggiungi_libro(titolo, autore):
	libro={"titolo":titolo,"autore":autore,"prestato":False}
	libri.append(libro)
	return libro
def lista_libri():
	for libro in libri:
        	stato = "prestato" if libro["prestato"] else "disponibile"
		print(f"[{libro['titolo']}] {libro['autore']} - stato: {libro['prestato']}")
def cerca_libro(titolo):
	for libro in libri:
		if libro["titolo"].lower() == titolo.lower():
			return libro
	return None
def presta_libro(titolo):
    	libro = cerca_libro(titolo)
	if libro:
        	libro["prestato"] = True
	return libro
def calcola_multa(giorni_ritardo):
	return giorni_ritardo * 0.20
def restituisci_libro(titolo):
    	libro = cerca_libro(titolo)
	if libro:
        	libro["prestato"] = False
	return libro
