# Revisado para avaliação
def connected(graph, a, b):
    """
    Retorna True se existe um caminho entre 'a' e 'b' no grafo.
    Implementação usando BFS apenas com listas.
    """

    # Verifica se os vértices existem
    if a not in graph or b not in graph:
        return False

    # BFS com listas
    fila = [a]
    visitados = [a]

    while fila:
        u = fila.pop(0)  # remove o primeiro (fila)

        if u == b:
            return True

        # Percorre os vizinhos
        for v in graph.get(u, []):
            if v not in visitados:
                visitados.append(v)
                fila.append(v)

    # Se BFS terminar sem encontrar b
    return False

# Cristiano Silva Lima 
# Pedro Henrique Araruna da Silva
# Kaegila Baliza de Jesus
# Wesley Alves de Barro Teles
# Marya Eduarda Pereira Rodrigues
# Andrew Durães da Costa
