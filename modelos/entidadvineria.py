from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    @abstractmethod
    def __init__(self, id: str, nombre: str):
        self._id = id
        self._nombre = nombre

    def establecerNombre(self, nombre: str):
        self._nombre = nombre

    def obtenerId(self) -> str:
        return self._id

    def obtenerNombre(self) -> str:
        return self._nombre

    def __eq__(self, other) -> bool:
        if isinstance(other, EntidadVineria):
            return self._id == other._id
        return False
    