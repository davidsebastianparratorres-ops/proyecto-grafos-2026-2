import sys
import os

# Sintaxis para subir un nivel desde 'test/' hacia la raíz del proyecto
# Esto permite que Python encuentre la carpeta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importación adaptada a tu estructura (src.models.NombreArchivo)
from src.models.Graph import Graph

def ejecutar_prueba():
    print("--- Inicializando Grafo de Prueba ---")
    g = Graph()
    
    # 1. Crear Vértices
    g.add_Vertex("A")
    g.add_Vertex("B")
    g.add_Vertex("C")
    g.add_Vertex("D")
    
    # 2. Crear Conexiones (Links) usando tu diccionario de vértices
    vertices = g.get_Vertex()
    
    vertices["A"].links["B"] = vertices["B"]
    vertices["A"].links["C"] = vertices["C"]
    
    vertices["B"].links["D"] = vertices["D"]
    vertices["C"].links["D"] = vertices["D"]
    
    # 3. Ejecutar el BFS desde el nodo "A"
    print("Ejecutando BFS desde el vértice 'A'...")
    resultado = g.bfs("A")
    
    # 4. Verificar resultados
    print(f"Resultado del recorrido: {resultado}")
    
    # Agregar esta línea para auditar:
    print(f"DEBUG - Nodos guardados en la lista: {resultado}")

    
    if resultado == ["A", "B", "C", "D"] or resultado == ["A", "C", "B", "D"]:
        print("✅ ¡Prueba exitosa! Tu BFS con colas nativas funciona perfectamente.")
    else:
        print("❌ Hubo un fallo en el orden del recorrido.")

if __name__ == "__main__":
    ejecutar_prueba()

