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
                bodegas = sorted(bodegas, key=lambda bodega: bodega._nombre, reverse=reverso)
            elif orden == "vinos":
                bodegas = sorted(bodegas, key=lambda bodega: len(bodega._vinos), reverse=reverso)
        return bodegas

    def obtenerCepas(orden=None, reverso=False):
        """Devuelve una lista de cepas ordenada según el parámetro 'orden'."""
        cepas = Vinoteca.__cepas
        if isinstance(orden, str):
            if orden == "nombre":
                cepas = sorted(cepas, key=lambda cepa: cepa.nombre, reverse=reverso)
        return cepas

    def obtenerVinos(anio=None, orden=None, reverso=False):
        """Devuelve una lista de vinos filtrada por año (si se proporciona) y ordenada según 'orden'."""
        vinos = Vinoteca.__vinos
        if isinstance(anio, int):
            vinos = [vino for vino in vinos if vino._partidas == anio]
        if isinstance(orden, str):
            if orden == "nombre":
                vinos = sorted(vinos, key=lambda vino: vino._nombre, reverse=reverso)
            elif orden == "bodega":
                vinos = sorted(vinos, key=lambda vino: vino._bodega._nombre, reverse=reverso)
            elif orden == "cepas":
                vinos = sorted(vinos, key=lambda vino: [cepa._nombre for cepa in vino.cepas], reverse=reverso)
        return vinos

    def buscarBodega(id):
        """Busca una bodega por su ID y devuelve la referencia si la encuentra."""
        for bodega in Vinoteca.__bodegas:
            if bodega._id == id:
                return bodega
        return None

    def buscarCepa(id):
        """Busca una cepa por su ID y devuelve la referencia si la encuentra."""
        for cepa in Vinoteca.__cepas:
            if cepa._id == id:
                return cepa
        return None

    def buscarVino(id):
        """Busca un vino por su ID y devuelve la referencia si lo encuentra."""
        for vino in Vinoteca.__vinos:
            if vino._id == id:
                return vino
        return None

    def __parsearArchivoDeDatos():
        """Lee el archivo JSON y retorna un diccionario con los datos."""
        if not os.path.exists(Vinoteca.__archivoDeDatos):
            return {}
        with open(Vinoteca.__archivoDeDatos, 'r') as archivo:
            return json.load(archivo)

    def __convertirJsonAListas(datos):
        """Convierte los datos del JSON en objetos correspondientes."""
        # Convertir bodegas
        #if 'bodega' in lista:
         #   Vinoteca.__bodegas = [Bodega(**bodega) for bodega in lista['bodega']]
            
        for bodega in datos["bodegas"]:
            Vinoteca.__bodegas.append(Bodega(bodega["id"],bodega["nombre"]))
        
        # Convertir cepas
        for cepa in datos["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepa["id"],cepa["nombre"]))
        #if 'cepas' in lista:
         #   Vinoteca.__cepas = [Cepa(**cepa) for cepa in lista['cepas']]
        
        # Convertir vinos
        for vino in datos["vinos"]:
            Vinoteca.__vinos.append(Vino(vino["id"],vino["nombre"],vino["bodega"],vino["cepas"],vino["partidas"]))
        #if 'vinos' in lista:
         #   Vinoteca.__vinos = [Vino(**vino) for vino in lista['vinos']]
