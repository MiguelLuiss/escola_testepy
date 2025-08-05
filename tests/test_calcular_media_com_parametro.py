import pytest
from escola.aluno import calcular_media

@pytest.mark.parametrize("entrada, situacao_esperada", 
                         
                         [
                            ([0.0, 0.0, 0.0, 0.0], 0) , 
                            ([10.0, 10.0, 10.0, 10.0], 10) ,
                            ([7.0], 7.0) ,
                            ([5.0,8.8,6.7,2.0,5.3,8.8,9.9], 6.6) ,
                            ([5.8,9.3], 7.6) ,
                            ([0.8,0.0,0.0], 0.3) ,
                            ([5,6,10], 7.0)
                         ])

def test_calcular_media_calculos_basicos_parametrizados(entrada, situacao_esperada):
    resultado = calcular_media(entrada)

    assert resultado == situacao_esperada