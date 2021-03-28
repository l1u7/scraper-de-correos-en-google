from bs4 import BeautifulSoup

class LinksGoogle:

    def __init__(self):
        self.enlaces = []

    def escanear(self, archivo): 
        bs = BeautifulSoup(archivo, 'lxml')
        elementos = bs.findAll(class_="yuRUbf")        
        for elemento in elementos:
            self.enlaces.append(elemento.a.get('href'))

    def obtener(self):
        return self.enlaces
