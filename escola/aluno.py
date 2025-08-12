def calcular_media(notas:list[float]) -> float:
    """Calcula a média de uma lista de notas.
    Parâmetros:
    notas(list[float]): Lista de notas a serem calculadas.
    
    Retorna:
    float: A média das notas, arredondada para uma casa decimal."""
    
    #Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Não é permitido uma lista vazia")

    media = sum(notas)/len(notas)
    return round(media,1)