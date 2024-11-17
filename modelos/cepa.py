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
        vinos_de_la_cepa = []
        for vino in vinos:
            cepas = vino.obtenerCepas() # obtiene una lista de objetos cepas, pertenecientes a ese vino
            for cepa in cepas: #recorre las cepas del vino
                if cepa == self: # si la cepa del vino es igual a la cepa en la que estamos
                    vinos_de_la_cepa.append(vino) # agrega ese vino a la lista de vinos de la cepa
                    
        return vinos_de_la_cepa


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
