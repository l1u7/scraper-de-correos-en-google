from config import buscador, path
from scraper import Scraper
from archivo import Archivo

class Buscador:

    def __init__(self, busqueda : str, limit : int):
        self.busqueda = str(busqueda.replace(' ', '+'))
        self.nombre = str(busqueda.replace(' ', '-'))
        self.paginacion = 0  
        self.limit = limit

    def crearPeticion(self) -> str:
        google = buscador.get('google')
        prepareReq = google.get('req') + self.busqueda + google.get('pag') + str(google.get('steps') * self.paginacion) 
        self.paginacion = self.paginacion + 1
        return prepareReq

    def ejecutar(self):
        for i in range(0, self.limit):
            peticion = self.crearPeticion()
            ruta = path.get('google') + self.nombre + '-' + str(i) 
            scraper = Scraper(peticion)
            archivo = Archivo(ruta, scraper.resultado())
            archivo.salvar() 
 