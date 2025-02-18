# Se importa la clase Padre Instrumento
from Instrumentos import Instrumentos
# Se crea la clase hija de Percusion, dependiendo de la clase padre instrumento para que se le asignen
# los mismos atributos de la clase padre a la clase hija.

class Percusion(Instrumentos):
    contador_percusion = 0
    def __init__(self, nombre, marca, tipo_instrumento):
        Percusion.contador_percusion += 1
        self._id_percusion = Percusion.contador_percusion
# Se inicializa la clase padre para la clase hija, heredando los atributos
        super().__init__(nombre, marca, tipo_instrumento)
# Se define el metodo str para regresar en consola una cadena de texto con los atributos de la clase
    def __str__(self):
        return f'ID: {self._id_percusion}, Nombre: {self._nombre} Marca: {self._marca}, Tipo: {self._tipo_instrumento}\n'

# Este codigo de abajo sirve para realizar pruebas solamente si se ejecuta en esta ventana.
if __name__ == '__main__':
    bateria1 = Percusion('Bateria,','Pearl', 'Percusion')
    print(bateria1)
