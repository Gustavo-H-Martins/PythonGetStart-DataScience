import pandas as pd
import numpy as np
# Formatação do código para usar cada etapa do desenvolvimento nesta primeira parte

continua = 0
while continua != "N" :
  parte = int(input("Escolha qual a parte do código você quer visualizar digite o número referente: "
                    "\n P11: Hello DataFrame! [11] "
                    "\n P12: Propriedades básicas dos DataFrames[12] "
                    "\n P13: Busca em DataFrame [13] "
                    "\n P14: Modificação de DataFrame [14] "
                    "\n "
                    "\n "
                    "\n "
                    "\n "
                    "\n "
                    "\n "
                    "\n : " ))

        """
        Em sua aparência, o DataFrame é igual a uma planilha Excel, uma
        vez que possui linhas e colunas. No entanto, considerando a forma
        como a pandas organiza os DataFrames, cada coluna é, na
        verdade, uma Series. Mais especificamente, o DataFrame é um
        dicionário de Series, todas do mesmo tamanho ( size ). Tanto as
        suas linhas como as suas colunas podem ser indexadas e rotuladas.
        """
  if parte == 11 : 
    print("No DataFrame paises as linhas são indexadas pela sigla do país."
    "\n Este DataFrame possui as seguintes colunas: nome (nome do país),
    "\n continente (nome do continente onde se localiza o país), extensão
    "\n(extensão territorial em milhares de quilômetros quadrados) e
    "\n corVerde (indica se a cor verde está presente na bandeira do país; o
    "\n valor 1 representa sim e 0, não).")
    #P11: Hello DataFrame!
    #cria o DataFrame
    dados = {'nome': ['Argentina','Brasil','França','Itália',
     'Reino Unido'],
     'continente': ['América','América','Europa','Europa',
     'Europa'],
     'extensao': [2780,8511,644,301,244],
     'corVerde': [0,1,0,1,0]
     }
    siglas = ['AR','BR','FR','IT','UK']
    paises = pd.DataFrame(dados,index=siglas)
    #imprime o DataFrame
    print(paises)

    if parte == 12 : 
      #P12: Propriedades básicas dos DataFrames

      #cria o DataFrame
      dados = {'nome': ['Argentina','Brasil','França','Itália',
     'Reino Unido'],
     'continente': ['América','América','Europa','Europa',
     'Europa'],
     'extensao': [2780,8511,644,301,244],
       'corVerde': [0,1,0,1,0]}
      siglas = ['AR','BR','FR','IT','UK']
      paises = pd.DataFrame(dados,index=siglas)
      #recupera e imprime as propriedades 
      print('-----------')
      num_linhas = paises.shape[0]
      num_colunas = paises.shape[1]
      indices = paises.index 
      colunas = paises.columns
      paises_tipo = type(paises) 
      paises_dtypes = paises.dtypes
      paises_idx_dtype = paises.index.dtype 
      print('número de linhas: ', num_linhas)
      print('número de colunas: ', num_colunas)
      print('rótulos das linhas: ', indices)
      print('rótulos das colunas: ', colunas)
      print('tipo (type): ',paises_tipo)
      print('dtypes das colunas:\n', paises_dtypes)
      print('dtype dos rótulos das linhas:', paises_idx_dtype) 
      
      """
      Com relação ao tipo de objeto retornado,
      temos que o resultado do fatiamento de um DataFrame será sempre
      um objeto do tipo DataFrame, exceto quando a operação resultar
      em uma única linha ou uma única coluna retornada. Neste caso, o
      tipo de objeto resultante é uma Series.
      Utilizamos colchetes [ ] para indexar elementos de um DataFrame.
      Assim como ocorre com as Series, é possível empregar três
      técnicas de indexação: indexação tradicional, fatiamento e
      indexação booleana. 
      """

    if parte == 12 :
      #P13: Busca em DataFrames
      #cria o DataFrame
      dados = {'nome': ['Argentina','Brasil','França','Itália',
       'Reino Unido'],
       'continente': ['América','América','Europa','Europa',
       'Europa'],
       'extensao': [2780,8511,644,301,244],
       'corVerde': [0,1,0,1,0]}
      siglas = ['AR','BR','FR','IT','UK']
      paises = pd.DataFrame(dados,index=siglas)
      #testa se um dado rótulo de linha existe
      tem_BR = 'BR' in paises.index
      tem_US = 'US' in paises.index
      print("existe o rótulo 'BR? -> ",tem_BR) 
      print("existe o rótulo 'US'? -> ",tem_US) 
      print('---------------------------')
      #testa se um dado rótulo de coluna existe
      tem_corVerde = 'corVerde' in paises.columns
      tem_corAzul = 'corAzul' in paises.columns
      print("existe o rótulo 'corVerde? -> ",tem_corVerde) 
      print("existe o rótulo 'corAzul'? -> ",tem_corAzul) 
      print('---------------------------')
      #testa se valor faz parte de uma coluna
      tem_Brasil = paises['nome'].isin(['Brasil'])
      print("existe o valor 'Brasil' na coluna 'nome'?") 
      print(tem_Brasil)
      
      """
      Para verificar se um rótulo de linha ou de coluna existe em um
      DataFrame, você deve aplicar o operador in sobre a lista de rótulos
      de linha ou de colunas, respectivamente (propriedades index e
      columns ).
      Se você quiser testar se um valor está armazenado em uma coluna,
      precisará utilizar o método isin() . Em nosso exemplo, passamos
      para o método uma lista com um único elemento ( 'Brasil' ) e
      mandamos checar a coluna nome . Como resultado, o método indicará
      True para a sigla BR .
      O próximo programa mostra:
      1. Como verificar se um determinado rótulo de linha ou coluna
      existe em um DataFrame;
      2. Como verificar se um determinado valor está armazenado em
      alguma coluna do DataFrame.
      """
    if parte == 13 :
      #P13: Busca em DataFrames
      
      #cria o DataFrame
      dados = {'nome': ['Argentina','Brasil','França','Itália',
       'Reino Unido'],
       'continente': ['América','América','Europa','Europa',
       'Europa'],
       'extensao': [2780,8511,644,301,244],
       'corVerde': [0,1,0,1,0]}
      siglas = ['AR','BR','FR','IT','UK']
      paises = pd.DataFrame(dados,index=siglas)
      #testa se um dado rótulo de linha existe
      tem_BR = 'BR' in paises.index
      tem_US = 'US' in paises.index
      print("existe o rótulo 'BR? -> ",tem_BR)
      print("existe o rótulo 'US'? -> ",tem_US)
      print('---------------------------')
      #testa se um dado rótulo de coluna existe
      tem_corVerde = 'corVerde' in paises.columns
      tem_corAzul = 'corAzul' in paises.columns
      print("existe o rótulo 'corVerde? -> ",tem_corVerde)
      print("existe o rótulo 'corAzul'? -> ",tem_corAzul)
      print('---------------------------')
      #testa se valor faz parte de uma coluna
      tem_Brasil = paises['nome'].isin(['Brasil'])
    
    """
    Modificação
    Este tópico apresenta as técnicas básicas para inserir e alterar
    linhas de um DataFrame e para modificar o conteúdo de alguma
    célula.
    Para inserir o Japão, basta indicar os dados desse país em um
    dicionário e realizar a atribuição com o uso do método loc() .
    Caso o DataFrame não possua rótulos de linha, será preciso
    utilizar o método iloc() com o índice da linha a ser inserida.
    Para alterar uma célula, no caso, a extensão do Brasil, utiliza se um comando de atribuição simples que emprega o método
    at() com a indicação dos rótulos de linha e coluna da célula a
    ser alterada. Caso o DataFrame não possua rótulos de linha,
    será preciso utilizar o método iat() com o índice da linha a ser
    alterada.
    Por fim, para remover linhas, basta utilizar o método drop()
    indicando a lista de rótulos de linha a serem removidos.
    """
    
    if parte == 14 :
      #P14: Modificação de DataFrame
      #cria o DataFrame
      dados = {'nome': ['Argentina','Brasil','França','Itália',
       'Reino Unido'],
       'continente': ['América','América','Europa','Europa',
       'Europa'],
       'extensao': [2780,8511,644,301,244],
       'corVerde': [0,1,0,1,0]}
      siglas = ['AR','BR','FR','IT','UK']
      paises = pd.DataFrame(dados,index=siglas)
      #insere o país Japão (JP)
      paises.loc['JP']= {'nome': 'Japão',
       'continente': 'Ásia',
       'extensao': 372,
       'corVerde': 0}
      #altera a extensão do Brasil
      paises.at['BR','extensao']=8512
      #remove a Argentina e o Reino Unido
      paises = paises.drop(['AR','UK'])
      print('DataFrame após as alterações:')
      print(paises)

    else :
    break
  continua = input("Deseja continuar visualizando as partes ? \n [S] - Sim \n [N] - Não \n : ").upper().strip()
  
  print("Fim do Algorítimo")
