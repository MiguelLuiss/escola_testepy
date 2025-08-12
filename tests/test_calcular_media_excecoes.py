import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    #Definindo a entrada
    entrada = []

    #Executando a função e esperando erro
    with pytest.raises(ValueError, match="Não é permitido uma lista vazia"):
        calcular_media(entrada)

def test_calculcar_media_enviando_string():
    entrada = "ola"


    with pytest.raises(TypeError, match = "nota invalida"):
        calcular_media(entrada)


def test_verificando_itens_lista():

    lista_valores = [1,2,3,4,5,6,7,8,9,0,"ola"]

    with pytest.raises(ValueError, match = "Nota inválida, string identificada"):
        calcular_media(lista_valores)


def test_calcular_media_com_numero_negativo():

    entrada = [-10.0]


    with pytest.raises(ValueError, match= "limite da nota \[0,10\]"):
        calcular_media(entrada)



def test_calcular_media_com_numero_maior_que_10():

    entrada = [9,10,11]

    #barra invertida serve para o python nao interpretar o colchetes como "coringa"
    with pytest.raises(ValueError, match= "limite da nota \[0,10\]"):
        calcular_media(entrada)
           