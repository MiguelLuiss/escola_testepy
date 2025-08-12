def calcular_media_boletim(notas:list[float]) -> float:

   #Validando se a entrada é uma lista
    if not isinstance(notas, list):
        raise TypeError("nota invalida")

    #Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Sem nota")
    
    for nota in notas:
        if nota >= 7:
            raise ValueError("Aprovado")
        if nota < 0 or nota > 10:
            raise ValueError("Nota invalida")
    
    if any(nota >= 7 for nota in notas):
        raise ValueError("Aprovado")
    
    if any(nota < 7 and nota >= 5 for nota in notas):
        raise ValueError("Recuperação")
    
    if (nota < 5 for nota in notas):
        raise ValueError("Reprovado")
    #Tem que ser return
    
