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