from bs4 import BeautifulSoup
from archivo import Archivo
from config import path
from buscador import Buscador
from linksGoogle import LinksGoogle
from scraper import Scraper
from funciones import extraerCorreo
from conexion import Conexion
import os

busqueda = str(input("Ingresar busqueda: "))

# el número 10 representa la paginación de google hasta la que se scrapeará 
buscarEnGoogle = Buscador(busqueda, 10)
buscarEnGoogle.ejecutar()

archivosCarpetaGoogle = os.listdir(path.get('google'))

lector = Archivo()
gLink = LinksGoogle()

for archivo in archivosCarpetaGoogle:
   contenido = lector.leer(path.get('google') + archivo)
   gLink.escanear(contenido)


enlacesResultados = gLink.obtener()

carpetaWebs = path.get('webs')

prefijo = 'archivo-'
contador = 1
for enlace in enlacesResultados:
   traer = Scraper(enlace)
   nombreArchivo = prefijo + str(contador)
   guardar = Archivo(carpetaWebs +  nombreArchivo , traer.resultado())
   guardar.salvar()
   contador = contador + 1
 

ruta = path.get('webs')
archivosWebs = os.listdir(ruta)
correos = []
archivo = Archivo()
 
for file in archivosWebs:  
    abierto = archivo.leer(ruta + file)
    extraccion = extraerCorreo(abierto)
    if extraccion:
        correos = correos + extraccion

conn = Conexion()
for correo in correos:
    conn.insertar("insert into emails (email) values (?)", (correo,))
conn.cerrar()

print('Fin...')