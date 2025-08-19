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
    

    """"
    Calcula a média de uma lista de notas.

    Parâmetros:
    notas (list[float]): Lista de notas a serem calculadas.

    Retorna:
    float: A média das notas, arredondada para uma casa decimal.
    """
    #Validando se a entrada é uma lista
    if not isinstance(notas, list):
        raise TypeError("nota invalida")


    #Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Não é permitido uma lista vazia")
    


    #Validando e a lista possui nota negativa ou maior que 10
        
    for valor_notas in notas:
        if valor_notas < 0:
            raise ValueError("limite da nota [0,10]")
        if valor_notas > 10:
            raise ValueError("limite da nota [0,10]")





    #A função any() retorna True se pelo menos um elemento da lista for True
    #O isinstance () verifica se um objeto é do tipo especificado
    #Ele verifica se na lista (notas) existe uma string, percorrendo em notas
    if any(isinstance(i, str) for i in notas):
        raise ValueError("String na lista")
    
    #Outra forma de fazer, menos simplificado
    # for nota in notas:
    #     if not type(nota) == int and not type(nota) == float:
    #         raise TypeError("Nota invalida")
    #     if nota < 0 or nota > 10:
    #         raise ValueError("Nota invalida")

    if any(nota < 0 for nota in notas):
        raise ValueError("Nota negativa")
    
    if any(nota > 10 for nota in notas):
        raise ValueError("Nota maior que 10")


    media = sum(notas)/len(notas)
    return round(media,1)
    


    

 
        