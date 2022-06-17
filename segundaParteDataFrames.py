import pandas as pd
import numpy as np
# Formatação do código para usar cada etapa do desenvolvimento nesta primeira parte

continua = 0
while continua != "N" :
  parte = int(input("Escolha qual a parte do código você quer visualizar digite o número referente: "
                    "\n P11: Hello DataFrame! [11] "
                    "\n P12: Propriedades básicas dos DataFrames[13] "
                    "\n P13: Busca em DataFrame [13] "
                    "\n "
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
      
    else :
    break
  continua = input("Deseja continuar visualizando as partes ? \n [S] - Sim \n [N] - Não \n : ").upper().strip()
  
  print("Fim do Algorítimo")
