import json

from modelos.entidadvineria import EntidadVineria 


class Vino(EntidadVineria):
    
    # Agregando init
    def __init__(self, id: str, nombre: str, bodega, cepas, partidas):
        super().__init__(id, nombre) #inicializa los atributos de entidad vineria
        self._bodega = bodega  # Almacena el nombre de la bodega como string
        self._cepas = cepas    # Lista de nombres de cepas
        self._partidas = partidas  # Lista de cantidades por partida

    # comandos
    def establecerBodega(self, bodega):
        self._bodega = bodega

    def establecerCepas(self, cepas):
        self._cepas = cepas

    def establecerPartidas(self, partidas):
        self._partidas = partidas
        
    # consultas
    def obtenerBodega(self):
        from vinoteca import Vinoteca 
        # Utiliza el servicio buscarBodega para obtener el objeto de tipo Bodega
        return Vinoteca.buscarBodega(self._bodega)

    def obtenerCepas(self):
        from vinoteca import Vinoteca 
        # Utiliza el servicio buscarCepa para obtener objetos de tipo Cepa
        return [Vinoteca.buscarCepa(cepa) for cepa in self._cepas]

    def obtenerPartidas(self):
        return self._partidas
    
    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self._partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self._partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
