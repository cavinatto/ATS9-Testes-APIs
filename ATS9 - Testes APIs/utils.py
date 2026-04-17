def validar_lista_tarefas(response_as_json):
    """
    Valida a resposta HTTP de uma lista de tarefas.

    Verifica se:
    - O retorno é uma lista (não vazia).
    - Pelo menos uma das tarefas contém a chave 'completed'.

    Usada via verify_response_with no Tavern.
    """
    data = response_as_json

    assert isinstance(data, list), (
        f"Esperava uma lista, mas recebeu: {type(data).__name__}"
    )
    assert len(data) > 0, "A lista de tarefas está vazia."

    tem_completed = any("completed" in tarefa for tarefa in data)
    assert tem_completed, (
        "Nenhuma tarefa na lista contém a chave 'completed'."
    )
