libri=[]
def aggiungi_libro(titolo, autore):
	libro={"titolo":titolo,"autore":autore,"prestato":False}
	libri.append(libro)
	return libro
def lista_libri():
	for libro in libri:
        	stato = "prestato" if libro["prestato"] else "disponibile"
		print(f"{libro['titolo']} - {libro['autore']} ({stato})")
