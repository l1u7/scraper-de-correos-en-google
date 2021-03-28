import codecs 

class Archivo:

    def __init__(self, route = '', content = ''):
        self.content = content 
        self.route   = route

    def salvar(self):    
        f = codecs.open(self.route, "w", "utf-8")
        f.write(self.content)
        f.close()

    def leer(self, file):
        f = codecs.open(file, 'rb')
        return f.read().decode('utf-8')