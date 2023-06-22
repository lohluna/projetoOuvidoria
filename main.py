
from operacoesbd import *
from Metodos import *

ocorrencias = []
opcao = 1
codigo = 1
conexao = abrirBancoDados('localhost', 'root', '12345', 'projetoouvidoria')

while opcao != 8:
    print()
    print('Menu')
    print()
    print('1) Listagem das Manifestações', '\n2) Listagem de Manifestações por Tipo', '\n3) Criar uma nova Manifestação'
          , '\n4) Exibir quantidade de manifestações', "\n5) Pesquisar uma manifestação por código",
          '\n6) Alterar o Título e Descrição de uma Manifestação'
          , '\n7) Excluir uma Manifestação pelo Código', '\n8) Sair do Sistema.')

    print()
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        print()
        listagemManifestacoes(ocorrencias,conexao)

    elif opcao == 2:
        print()
        tipo = input('Digite o tipo da manifestação: reclamação, elogio ou sugestão: ')
        listagemManifestacoesTipo(ocorrencias,conexao,tipo)
