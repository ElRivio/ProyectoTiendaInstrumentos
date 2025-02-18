# Se importa la clase padre para la clase hija
from Instrumentos import Instrumentos
# Se crea la clase hija de Cuerdas, dependiendo de la clase padre instrumento para que se le asignen
# los mismos atributos de la clase padre a la clase hija.

class Viento(Instrumentos):
    contador_viento = 0
    def __init__(self, nombre, marca, tipo_instrumento):
        Viento.contador_viento += 1
        self._id_viento = Viento.contador_viento
# Se inicializa la clase padre para la clase hija, heredando los atributos
        super().__init__(nombre, marca, tipo_instrumento)

# Se define el metodo str para regresar en consola una cadena de texto con los atributos de la clase
    def __str__(self):
        return f'ID: {self._id_viento}, Nombre: {self._nombre} Marca: {self._marca}, Tipo: {self._tipo_instrumento}\n'

# Este codigo de abajo sirve para realizar pruebas solamente si se ejecuta en esta ventana.
if __name__ == '__main__':
    flauta1 = Viento('Flauta,','Yamaha', 'Viento')
    print(flauta1)

