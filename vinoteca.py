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
        """Devuelve una lista de bodegas ordenada según el parámetro orden"""
        bodegas = Vinoteca.__bodegas
        if isinstance(orden, str):
            if orden == "nombre":
                bodegas = sorted(bodegas, key=lambda bodega: bodega.obtenerNombre(), reverse=reverso)
            elif orden == "vinos":
                bodegas = sorted(bodegas, key=lambda bodega: len(bodega.obtenerVinos()), reverse=reverso)
        return bodegas

    def obtenerCepas(orden=None, reverso=False):
        """Devuelve una lista de cepas ordenada según el parámetro 'orden'."""
        cepas = Vinoteca.__cepas
        if isinstance(orden, str):
            if orden == "nombre":
                cepas = sorted(cepas, key=lambda cepa: cepa.obtenerNombre(), reverse=reverso)
        return cepas

    def obtenerVinos(anio=None, orden=None, reverso=False, bodega_id=None):
        """Devuelve una lista de vinos filtrada por año (si se proporciona) y ordenada según 'orden', o por bodega si se proporciona."""
        vinos = Vinoteca.__vinos
        vinos_filtrados = []  # Inicialización de la lista

        # Si se proporciona un bodega_id, filtrar los vinos por bodega
        if bodega_id:
            vinos_filtrados = [vino for vino in vinos if vino.obtenerBodega().obtenerId() == bodega_id]
        else:
            vinos_filtrados = vinos
        
        # Filtrar por año si se proporciona
        if isinstance(anio, int):
            vinos_filtrados = [vino for vino in vinos_filtrados if anio in vino.obtenerPartidas()]

        # Ordenar según el criterio especificado (si se proporciona)
        if isinstance(orden, str):
            if orden == "nombre":
                vinos_filtrados = sorted(vinos_filtrados, key=lambda vino: vino.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                vinos_filtrados = sorted(vinos_filtrados, key=lambda vino: vino.obtenerBodega().obtenerNombre(), reverse=reverso)
            elif orden == "cepas":
                vinos_filtrados = sorted(vinos_filtrados, key=lambda vino: [cepa.obtenerNombre() for cepa in vino.obtenerCepas()], reverse=reverso)

        return vinos_filtrados



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
        with open(Vinoteca.__archivoDeDatos, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    def __convertirJsonAListas(datos):
        """Convierte los datos del JSON en objetos correspondientes."""
        
        # Convertir bodegas  
        for bodega in datos["bodegas"]:
            Vinoteca.__bodegas.append(Bodega(bodega["id"],bodega["nombre"]))
        
        # Convertir cepas
        for cepa in datos["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepa["id"],cepa["nombre"]))
            
        # Convertir vinos
        for vino in datos["vinos"]:
            Vinoteca.__vinos.append(Vino(vino["id"],vino["nombre"],vino["bodega"],vino["cepas"],vino["partidas"]))
       
