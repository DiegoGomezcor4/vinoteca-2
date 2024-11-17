import json
from modelos.entidadvineria import EntidadVineria



class Cepa(EntidadVineria): 
    
    # agregando init
    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre)
        

    def __repr__(self):
        """representacion textual de a cepa en formato JSON simplificado"""
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        """convierte la cepa a un formato JSON simple
        Return: Diccionario conlos datos basicos de la cepa
        """
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        """
        Convierte la cepa a un formato JSON completo, incluyendo sus vinos.
        
        :return: Diccionario con los datos completos de la cepa y sus vinos asociados.
        """
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }
        
    # Agregando obtenerVinos
    def obtenerVinos(self):
        from vinoteca import Vinoteca
        """
        Obtiene todos los vinos que utilizan esta cepa.
        
        :return: Lista de objetos Vino asociados a esta cepa.
        """
        # Obtiene todos los vinos desde Vinoteca
        vinos = Vinoteca.obtenerVinos()
        # Filtra los vinos que incluyen esta cepa por su ID
        return [vino for vino in vinos if self.obtenerId() in [cepa.obtenerId() for cepa in vino.cepas]]


    def __mapearVinos(self):
        """
        Mapea los vinos asociados para obtener su nombre y bodega.
        
        :return: Lista de cadenas con la información de cada vino.
        """
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)
