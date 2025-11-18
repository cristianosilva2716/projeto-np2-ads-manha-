# Ajuste final - Cristiano
# tree_logic.py

class Node:
    def __init__(self, question, yes=None, no=None):
        self.question = question
        self.yes = yes
        self.no = no

    def is_leaf(self):
        return self.yes is None and self.no is None


def navigate_tree(node, answers):
    """
    Percorre a árvore a partir de 'node' seguindo a sequência de respostas.
    Cada resposta deve ser 'sim' ou 'não' (aceite 'nao' como 'não').
    """

    current = node
    index = 0  # para saber qual resposta estamos lendo

    while not current.is_leaf():

        # Se acabaram as respostas antes de chegar numa folha
        if index >= len(answers):
            raise ValueError("Faltam respostas para concluir a decisão.")

        # Normalizar a resposta
        resp = answers[index].strip().lower()

        # Tratar variações de "não"
        if resp == "nao":
            resp = "não"

        # Avançar pela árvore
        if resp == "sim":
            current = current.yes
        elif resp == "não":
            current = current.no
        else:
            raise ValueError(
                f"Resposta inválida: '{answers[index]}'. Use 'sim' ou 'não'."
            )

        index += 1

        # Caso o próximo nó seja None (árvore malformada)
        if current is None:
            raise ValueError(
                "A árvore de decisão está incompleta para essa sequência de respostas."
            )

    # Chegou numa folha → decisão final
    return current.question
