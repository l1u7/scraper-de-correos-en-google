import sqlite3

class Conexion:

    def __init__(self):
        try:
            self.conn = sqlite3.connect('almacen.db')
        except sqlite3.Error as e:
            print("Ocurrio un error:", e.args[0])


    def insertar( self, peticion, values ):
        try:
            self.conn.execute( peticion, values )    
            self.conn.commit()
        except sqlite3.Error as e:
            print("Ocurrio un error:", e.args[0])

    def seleccionar( self, tabla ):
        seleccion = self.conn.execute(f"select * from {tabla}")
        return seleccion.fetchall()

    def cerrar(self):
        self.conn.close()    


#conexion = Conexion()
#conexion.insertar("insert into urls (url) values (?)", ("google.com",))
# print(conexion.seleccionar('emails'))
# conexion.cerrar()
