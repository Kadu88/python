#python functions
def gera_nome_convite(nome_formatado):
    tamanho = len(nome_formatado)
    return nome_formatado[0:4] + ' ' + nome_formatado[tamanho - 4:tamanho]


def envia_convite(nome_formatado):
    print('Enviando convite para %s' %  nome_formatado)


def processa_convite(nome_formatado):
    envia_convite(gera_nome_convite(nome_formatado))

