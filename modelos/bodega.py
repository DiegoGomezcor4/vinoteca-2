import json
from modelos.entidadvineria import EntidadVineria
from vinoteca import Vinoteca


class Bodega(EntidadVineria):
    
    #agregando init:
    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre)
        
    #agregando obenterVinos
    def obtenerVinos(self) -> list:
        # obtiene todos los vinos asociados a esta bodega
        return [Vinoteca.buscarVino(vino_id) for vino_id in self.vinos]

    # agregando obtenerCepas
    def obtenerCepas(self):
        """Obtiene las cepas asociadas a esta bodega a través de los vinos desde la clase Vinoteca."""
        cepas = set()  # Usamos un set para evitar duplicados
        for vino_id in self.vinos:
            vino = Vinoteca.buscarVino(vino_id)
            if vino:
                cepas.update(vino.cepas)  # Añadimos los IDs de cepas del vino
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in cepas]


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
