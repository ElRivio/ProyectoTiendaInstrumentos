from Cuerdas import Cuerdas
from Viento import Viento
from Percusion import Percusion
from Orden import Orden

# Crea instancias de Cuerdas, Viento y Percusion
guitarra1 = Cuerdas('Guitarra, ', 'Yamaha', 'Cuerda')
flauta1 = Viento('Flauta, ', 'Yamaha', 'Viento')
bateria1 = Percusion('Bateria, ', 'Pearl', 'Percusion')

guitarra2 = Cuerdas('Guitarra, ', 'Ibanez', 'Cuerda')
flauta2 = Viento('Flauta, ', 'Mistica', 'Viento')
bateria2 = Percusion('Bateria, ', 'Mapple', 'Percusion')

# Crea una lista de instrumentos directamente con las instancias de Cuerdas, Viento y Percusion
instrumentos1 = [guitarra1, flauta1, bateria1]
instrumentos2 = [guitarra2, flauta2, bateria2]

# Crea ordenes con la lista de instrumentos
orden1 = Orden(instrumentos1)
orden2 = Orden(instrumentos2)

# Imprime las ordenes
print(orden1)
print(orden2)

# ID otorga a cada instrumento del mismo tipo un identificador unico.