from operacoesbd import *


def listagemManifestacoes(ocorrencias,conexao):
    consultaListagem = 'select * from ocorrencias'
    ocorrencias = listarBancoDados(conexao, consultaListagem)
    if len(ocorrencias) == 0:
        print('Nenhuma manifestação cadastrada no sistema')
    else:
        print('Listagem das Manifestações')
        for ocorrencia in ocorrencias:
            print('codigo', str(ocorrencia[0]), '-', ocorrencia[1], '-', ocorrencia[3], '-', ocorrencia[4])

def listagemManifestacoesTipo(ocorrencias,conexao,tipo):
    consultaListagem = "select * from ocorrencias where tipo = '" + tipo + "'"
    ocorrencias = listarBancoDados(conexao, consultaListagem)
    if len(ocorrencias) == 0:
        print('Nenhuma manifestação cadastrada no sistema')
    else:
        print(len(ocorrencias))
        for ocorrencia in ocorrencias:
            print('codigo', str(ocorrencia[0]), '-', ocorrencia[1], '-', ocorrencia[2])
def criarManifestacao(conexao,titulo,descricao,tipo,autor):
    sqlInsercao = 'insert into ocorrencias (titulo,descricao,tipo,autor) values(%s,%s,%s,%s)'
    valores = [titulo, descricao, tipo, autor]
    insertNoBancoDados(conexao, sqlInsercao, valores)

def quantidadePorTipoManifestacoes (conexao):
    consultaListagem = 'select count(*) from ocorrencias'
    resultado = listarBancoDados(conexao, consultaListagem)
    quantidade = resultado[0][0]
    print('Quantidade de Manifestações:', str(quantidade))

    consultareclamacoes = "select count(*) from ocorrencias where tipo = 'reclamação'"
    resultado = listarBancoDados(conexao, consultareclamacoes)
    quantidadeReclamacoes = resultado[0][0]
    print('Quantidade de reclamações:', str(quantidadeReclamacoes))

    consultarSugestoes = "select count(*) from ocorrencias where tipo = 'sugestão'"
    resultado = listarBancoDados(conexao, consultarSugestoes)
    quantidadeSugestoes = resultado[0][0]
    print('Quantidade de sugestões:', str(quantidadeSugestoes))

    consultarElogios = "select count(*) from ocorrencias where tipo = 'elogio'"
    resultado = listarBancoDados(conexao, consultarElogios)
    quantidadeElogios = resultado[0][0]
    print('Quantidade de elogios:', str(quantidadeElogios))

def pesquisarManifestacaoPorCodigo(conexao):
    codigo = input('Digite o código da manifestação: ')
    consultaListagem = "select * from ocorrencias where codigo = '" + codigo + "'"
    ocorrencias = listarBancoDados(conexao, consultaListagem)
    if len(ocorrencias) == 0:
        print('Nenhuma manifestação cadastrada no sistema')
    else:
        ocorrencias = listarBancoDados(conexao, consultaListagem)
        print(len(ocorrencias))
        for ocorrencia in ocorrencias:
            print('codigo', str(ocorrencia[0]), '-', ocorrencia[1], '-', ocorrencia[2], '-', ocorrencia[3], '-',
                  ocorrencia[4])
            
def alterarManifestacao(conexao,novoTitulo,novaDescricao,codigo):
    sqlAtualizar = 'update ocorrencias set titulo = %s, descricao = %s where codigo = %s'
    valores = [novoTitulo, novaDescricao, codigo]
    atualizarBancoDados(conexao, sqlAtualizar, valores)

def excluirManifestacao(codigo,conexao):
    consultaListagem = 'delete from ocorrencias where codigo = %s '
    dados = [codigo]
    excluirBancoDados(conexao, consultaListagem, dados)
