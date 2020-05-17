from datetime import date


class Item:
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


# para os parâmetros opcionais, nesse caso data_de_emissao e detalhes,
# temos de passar um valor default no construtor para na chamada da classe
# ser aceito não ser passado esses parâmetros
# parâmetros opcionais devem ser passados como os últimos parâmetros
class NotaFiscal:
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':
    from criador_de_nota_fiscal import CriadorDeNotaFiscal

    itens = [
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    # para evitar que os argumentos possam ser passados fora de ordem,
    # podemos usar parâmetros nomeados
    # posso inverter a ordem com parâmetros nomeados
    nota_fiscal = NotaFiscal(
        razao_social='FHSA Limitada',
        cnpj='012345678901234',
        itens=itens,
        data_de_emissao=date.today(),
        detalhes=''
    )

    nota_fiscal_criada_com_builder = (
        CriadorDeNotaFiscal().
        com_razao_social('FHSA Limitada').
        com_cnpj('012345678901234').
        com_itens(itens).constroi()
    )
