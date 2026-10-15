#Progetto didattico
libri=[]
def aggiungi_libro(titolo, autore):
	libro={"titolo":titolo,"autore":autore,"prestato":False}
	libri.append(libro)
	return libro
def lista_libri():
	for libro in libri:
        	stato = "prestato" if libro["prestato"] else "disponibile"
		print(f"{libro['titolo']} - {libro['autore']} ({stato})")
def cerca_libro(titolo):
	for libro in libri:
		if libro["titolo"].lower() == titolo.lower():
			return libro
	return None
