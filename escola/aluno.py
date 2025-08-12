def calcular_media(notas:list[float]) -> float:
    """Calcula a média de uma lista de notas.
    Parâmetros:
    notas(list[float]): Lista de notas a serem calculadas.
    
    Retorna:
    float: A média das notas, arredondada para uma casa decimal."""

    #Validando se a entrada é uma lista
    if not isinstance(notas, list):
        raise TypeError("nota invalida")
    
    #Validando se a lista possui uma string
    if any(isinstance(valor, str) for valor in notas):
        raise ValueError("Nota inválida, string identificada")
    
    #Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Não é permitido uma lista vazia")
    

    #Validando e a lista possui nota negativa ou maior que 10
        
    for valor_notas in notas:
        if valor_notas < 0:
            raise ValueError("limite da nota [0,10]")
        if valor_notas > 10:
            raise ValueError("limite da nota [0,10]")





    media = sum(notas)/len(notas)
    return round(media,1)
    


    

 
        