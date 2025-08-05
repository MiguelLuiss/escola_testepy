import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    #Definindo a entrada
    entrada = []

    #Executando a função e esperando erro
    with pytest.raises(ValueError, match="Não é permitido uma lista vazia"):
        calcular_media(entrada)