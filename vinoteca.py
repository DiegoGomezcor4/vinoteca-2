# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:
    
    # Atributos de clase
    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []
    
    # Metodos de clase

    def inicializar():
        """Inicializa la vinoteca cargando los datos desde un archivo Json."""
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    def obtenerBodegas(orden=None, reverso=False):
        """Devuelve una lista de bodegas ordenada segun el parametro orden"""
        bodegas = Vinoteca.__bodegas
        if isinstance(orden, str):
            if orden == "nombre":
                bodegas = sorted(bodegas, key=lambda bodega: bodega.nombre, reverse=reverso)
            elif orden == "vinos":
                bodegas = sorted(bodegas, key=lambda bodega: len(bodega.vinos), reverse=reverso)
        return bodegas

    def obtenerCepas(orden=None, reverso=False):
        """Devuelve una lista de cepas ordenada según el parámetro 'orden'."""
        cepas = Vinoteca.cepas
        if isinstance(orden, str):
            if orden == "nombre":
                cepas = sorted(cepas, key=lambda cepa: cepa.nombre, reverse=reverso)
        return cepas

    def obtenerVinos(anio=None, orden=None, reverso=False):
        """Devuelve una lista de vinos filtrada por año (si se proporciona) y ordenada según 'orden'."""
        vinos = Vinoteca.vinos
        if isinstance(anio, int):
            vinos = [vino for vino in vinos if vino.anio == anio]
        if isinstance(orden, str):
            if orden == "nombre":
                vinos = sorted(vinos, key=lambda vino: vino.nombre, reverse=reverso)
            elif orden == "bodega":
                vinos = sorted(vinos, key=lambda vino: vino.bodega.nombre, reverse=reverso)
            elif orden == "cepas":
                vinos = sorted(vinos, key=lambda vino: [cepa.nombre for cepa in vino.cepas], reverse=reverso)
        return vinos

    def buscarBodega(id):
        """Busca una bodega por su ID y devuelve la referencia si la encuentra."""
        for bodega in Vinoteca.bodegas:
            if bodega.id == id:
                return bodega
        return None

    def buscarCepa(id):
        """Busca una cepa por su ID y devuelve la referencia si la encuentra."""
        for cepa in Vinoteca.cepas:
            if cepa.id == id:
                return cepa
        return None

    def buscarVino(id):
        """Busca un vino por su ID y devuelve la referencia si lo encuentra."""
        for vino in Vinoteca.vinos:
            if vino.id == id:
                return vino
        return None

    def __parsearArchivoDeDatos():
        """Lee el archivo JSON y retorna un diccionario con los datos."""
        if not os.path.exists(Vinoteca.archivoDeDatos):
            return {}
        with open(Vinoteca.archivoDeDatos, 'r') as archivo:
            return json.load(archivo)

    def __convertirJsonAListas(lista):
        """Convierte los datos del JSON en objetos correspondientes."""
        # Convertir bodegas
        if 'bodegas' in lista:
            Vinoteca.bodegas = [Bodega(**bodega) for bodega in lista['bodegas']]
        
        # Convertir cepas
        if 'cepas' in lista:
            Vinoteca.cepas = [Cepa(**cepa) for cepa in lista['cepas']]
        
        # Convertir vinos
        if 'vinos' in lista:
            Vinoteca.vinos = [Vino(**vino) for vino in lista['vinos']]
