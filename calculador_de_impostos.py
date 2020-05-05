# padrão de projeto Strategy
from impostos import ICMS, ISS


class CalculadorDeImpostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadorDeImpostos()

    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, ISS())  # passando método por parâmetro
    calculador.realiza_calculo(orcamento, ICMS())
