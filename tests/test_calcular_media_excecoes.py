import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    #Definindo a entrada
    entrada = []

    #Executando a função e esperando erro
    with pytest.raises(ValueError, match="Não é permitido uma lista vazia"):
        calcular_media(entrada)

<<<<<<< HEAD
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
           
=======
# def test_calcular_media_eviando_string():
#     #Definindo a entrada
#     entrada = "ola"

#     #Executando a função e esperando erro
#     with pytest.raises(TypeError, match="Nota inválida"):
#         calcular_media(entrada)

def test_verificando_itens_lista():
    lista_valores = [1,"olá"]

    with pytest.raises(ValueError, match="String na lista"):
        calcular_media(lista_valores)

def test_calcular_media_com_numero_negativo():
    lista_valores = [-10.0]

    with pytest.raises(ValueError, match="Nota negativa"):
        calcular_media(lista_valores)

def test_calcular_media_com_numero_maior_que_10():
    lista_valores = [8,10,11]

    with pytest.raises(ValueError, match="Nota maior que 10"):
        calcular_media(lista_valores)
>>>>>>> 913c036b6135e46c52f78dad05eac74cf11859de
