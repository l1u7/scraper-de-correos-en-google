import sqlite3

conn = sqlite3.connect('almacen.db')
conn.execute( "DELETE FROM emails" ) 
conn.execute( "DELETE FROM urls" ) 
conn.commit()
conn.close() 