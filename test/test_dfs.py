import sys
import os

# Permitir que Python encuentre la carpeta 'src' subiendo un nivel
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/models')))

from src.models.Graph import Graph

def probar_dfs_profundo():
    print("--- Inicializando Grafo de Prueba para DFS ---")
    g = Graph()
    
    # 1. Crear Vértices (Camino largo: A -> B -> C -> D y una rama muerta en B -> E)
    g.add_Vertex("A")
    g.add_Vertex("B")
    g.add_Vertex("C")
    g.add_Vertex("D")
    g.add_Vertex("E")
    
    vertices = g.get_Vertex()
    
    # 2. Conectar los nodos de manera secuencial para simular profundidad
    # A se conecta a B
    vertices["A"].links["B"] = vertices["B"]
    
    # B tiene dos caminos: primero E (callejón sin salida) y luego C
    vertices["B"].links["E"] = vertices["E"]
    vertices["B"].links["C"] = vertices["C"]
    
    # C se conecta a D (el final del camino largo)
    vertices["C"].links["D"] = vertices["D"]
    
    
    
    # 3. Ejecutar el DFS desde el nodo inicial "A"
    print("Ejecutando DFS desde el vértice 'A'...")
    resultado = g.dfs("A")  # (Usa el nombre exacto de tu método, si le cambiaste a 'dfs' cámbialo aquí)
    
    # 4. Verificar resultados
    print(f"\nDEBUG - Nodos guardados en la lista: {resultado}")
    
    # El orden estricto de inserción natural debe ser: 
    # Ir a B -> ir a E -> quedarse sin salida -> retroceder a B -> ir a C -> ir a D
    orden_esperado = ["A", "B", "E", "C", "D"]
    
    if resultado == orden_esperado:
        print("✅ ¡Prueba exitosa! El DFS avanzó, retrocedió en el callejón sin salida (E) y terminó el recorrido perfectamente.")
    else:
        print("❌ Hubo un fallo. El orden obtenido no coincide con el comportamiento de profundidad esperado.")

if __name__ == "__main__":
    probar_dfs_profundo()
