"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import Dfs&Bfs as dbs
from datetime import datetime

"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    rgraph = g.newGraph(5500,compareByKey)
    catalog = {'reviewGraph':rgraph}    
    marcas_dfs= map.newMap(capacity=11000, maptype='PROBING',comparefunction=compareByKey)
    path_dfs=lt.newList()
    catalog['marcas_dfs']=marcas_dfs
    catalog['marcas_bfs']=None
    catalog['path_dfs']=path_dfs
    return catalog


def addReviewNode (catalog, row):
    """
    Adiciona un nodo para almacenar un libro o usuario 
    """
    if not g.containsVertex(catalog['delayGraph'], row['SOURCE']):
        g.insertVertex (catalog['delayGraph'], row['SOURCE'])
    if not g.containsVertex(catalog['delayGraph'], row['DEST']):
        g.insertVertex (catalog['delayGraph'], row['DEST'])

def addReviewEdge (catalog, row):
    """
    Adiciona un enlace para almacenar una revisión
    """
    g.addEdge (catalog['delayGraph'], row['SOURCE'], row['DEST'], row['ARRIVAL_DELAY'])


def countNodesEdges (catalog):
    """
    Retorna la cantidad de nodos y enlaces del grafo de revisiones
    """
    nodes = g.numVertex(catalog['delayGraph'])
    edges = g.numEdges(catalog['delayGraph'])

    return nodes,edges

def getPath (catalog, source, dst):
    """
    Retorna el camino, si existe, entre vertice origen y destino
    """
    mapa= catalog['marcas_dfs']
    grafo= catalog['reviewGraph']
    path= catalogo['path_dfs']
    if dst==source:
        return path
    if map.size(mapa)==0:
        dbs.depth_first_search(grafo,mapa,source)

    nod_bus=map.get(mapa, dst)
    if nod_bus != None:
        new_node=node_bus['predecesor']
        lt.addFirst(path,new_node)
        getPath(catalog,source,new_node)

    else:
        return None

def carga_bfs(catalog, source):
    search= dbs.newBFS(catalog['reviewGraph'], source)
    catalogo['marcas_bfs']= search['visitedMap']

def path_small(catalog, source, dst):

    mapa= catalog['marcas_bfs']
    grafo= catalog['reviewGraph']
    path= catalogo['path_bfs']
    if dst==source:
        return path
    if mapa == None:
        carga_bfs(catalog, source)
    nod_bus=map.get(mapa, dst) 
    if nod_bus != None:
        new_node=node_bus['predecesor']
        lt.addFirst(path,new_node)
        getPath(catalog,source,new_node)
    else:
        return None
    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

