# Se importa la clase padre para la clase hija
from Instrumentos import Instrumentos
#Se crea la clase hija de Cuerdas, dependiendo de la clase padre instrumento para que se le asignen los mismos atributos de la clase padre a la clase hija.

class Cuerdas(Instrumentos):
    contador_cuerdas = 0
    def __init__(self, nombre, marca, tipo_instrumento):
        Cuerdas.contador_cuerdas += 1
        self._id_cuerdas = Cuerdas.contador_cuerdas
        super().__init__(nombre, marca, tipo_instrumento)

# Se define el metodo str para regresar en consola una cadena de texto con los atributos de la clase
    def __str__(self):
        return f'ID: {self._id_cuerdas}, Nombre: {self._nombre} Marca: {self._marca}, Tipo: {self._tipo_instrumento}\n'


# Este codigo de abajo sirve para realizar pruebas solamente si se ejecuta en esta ventana.

if __name__ == '__main__':
    guitarra1 = Cuerdas('Guitarra, ','Yamaha', 'Cuerdas')
    print(guitarra1)