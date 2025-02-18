#Clase padre de todos los instrumentos, todos los instrumentos dependeran de esta clase
#con los atributos de marca y tipo de instrumento, tambien se definen los metodos ger y setter de cada atributo.

class Instrumentos:
    def __init__(self, nombre, marca, tipo_instrumento):
        self._nombre = nombre
        self._marca = marca
        self._tipo_instrumento = tipo_instrumento
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    @property
    def tipo_instrumento(self):
        return self._tipo_instrumento
    @tipo_instrumento.setter
    def tipo_instrumento(self, tipo_instrumento):
        self._tipo_instrumento = tipo_instrumento
# Se define el metodo str para regresar una cadena de texto en consola con todos los atributos
    def __str__(self):
        return f'Nombre: {self._nombre} Marca: {self._marca}, Tipo: {self._tipo_instrumento}'

#Este codigo de abajo sirve para realizar pruebas solamente si se ejecuta en esta ventana.

if __name__ == '__main__':
    guitarra1 = Instrumentos('Guitarra,', 'Yamaha', 'Cuerdas')
    print(guitarra1)