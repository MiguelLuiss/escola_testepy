import pytest
from  escola.boletim import calcular_media_boletim

def test_calcular_media_boletim_nota_vazia():
    lista_valores = [10.0,5.0,6.0,1.0]

    with pytest.raises(ValueError, match="Não é permitido uma lista vazia"):
        calcular_media_boletim(lista_valores)

def test_calcular_media_boletim_com_menos_de_4_notas():
    lista_valores = [4.0,7.0,9.0]

    with pytest.raises(ValueError, match="Notas insuficientes"):
        calcular_media_boletim(lista_valores)

def test_calcular_media_boletim_com_notas_atingidas_maior_que_10():
    lista_valores = [-5.8]

    with pytest.raises(ValueError, match="Limite atingido"):
        calcular_media_boletim(lista_valores)

def test_calcular_media_boletim_com_notas_atingidas_menor_que_10():
    lista_valores = [9.0,11,10]

    with pytest.raises(ValueError, match="Limite atingido"):
        calcular_media_boletim(lista_valores)

def test_calcular_media_boletim_com_notas_em_string():
    lista_valores = ["ola",3.0]

    with pytest.raises(ValueError, match="Nota invalida"):
        calcular_media_boletim(lista_valores)

def test_calcular_media_boletim_aprovado():
    lista_valores = [10.0,5.0,7.0,7.0]

    with pytest.raises(match="Aprovado"):
        calcular_media_boletim(lista_valores)

def test_calcular_media_boletim_aprovado():
    lista_valores = [10.0,5.0,6.0,1.0]

    with pytest.raises(match="Recuperação"):
        calcular_media_boletim(lista_valores)

def test_calcular_media_boletim_reprovado():
    lista_valores = [2.0,5.0,7.0,3.0]

    with pytest.raises(match="Reprovado"):
        calcular_media_boletim(lista_valores)