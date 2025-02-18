# Se crea la clase Orden que organizara las compras de los instrumentos en ordenes, las contabilizara y contara el total
class Orden:
    contador_ordenes = 0
    def __init__(self, instrumentos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._instrumentos = instrumentos

    def agregar_instrumento(self, instrumento):
        self._instrumentos.append(instrumento)
    def __str__(self):
        instrumentos_str = ''
        for instrumento in self._instrumentos:
            instrumentos_str += instrumento.__str__()
        return f"""
Orden: {self._id_orden}    
Instrumentos: 
{instrumentos_str}
"""


