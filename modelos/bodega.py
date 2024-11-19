import json
from modelos.entidadvineria import EntidadVineria
from modelos.vino import Vino
from modelos.cepa import Cepa



class Bodega(EntidadVineria):
    
    #agregando init:
    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre)
        
    #agregando obenterVinos
    def obtenerVinos(self) -> list:
        from vinoteca import Vinoteca
        todos_los_vinos = Vinoteca.obtenerVinos()
        vinos = []

        for vino in todos_los_vinos:
            bodega = vino.obtenerBodega()
           # if bodega and str(bodega._id) == str(self._id):  # Convierte ambos a str para compararlos
            if bodega == self:
                vinos.append(vino)

        return vinos


    # agregando obtenerCepas
    def obtenerCepas(self):
        from vinoteca import Vinoteca
        vinos_de_la_bodega = self.obtenerVinos()
        cepas_de_la_bodega = []
        for vino in vinos_de_la_bodega:
            for cepa in vino.obtenerCepas():
                if cepa not in cepas_de_la_bodega:
                    cepas_de_la_bodega.append(cepa)
        return cepas_de_la_bodega
            
        


    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)

