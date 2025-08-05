def calcular_media(notas:list[float]) -> float:
    
    #Validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Não é permitido uma lista vazia")

    media = sum(notas)/len(notas)
    return round(media,1)