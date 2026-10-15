libri=[]
def aggiungi_libro(titolo, autore):
	libro={"titolo":titolo,"autore":autore,"prestato":False}
	libri.append(libro)
	return libro
