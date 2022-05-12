import pandas as pd
# Formatação do código para usar cada etapa do desenvolvimento nesta primeira parte

continua = 0
while continua != "N" :
  parte = int(input("Escolha qual a parte do código você quer visualizar digite o número referente: \n P01: Olá Series! - [1] \n P02: Propriedades básicas das Series [2] \n : " ))
  
  if parte == 1 :  
    #P01: Olá Series!
    #cria a Series notas
    notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])
    #cria a Series alunos
    listaMatriculas = ['M02','M05','M13','M14','M19']
    listaNomes = ['Bob','Dayse','Bill','Cris','Jimi']
    alunos = pd.Series(listaNomes,index=listaMatriculas)
    #imprime as duas Series
    print(notas); print("---------------"); print(alunos)
   
  elif parte == 2 :
    #P02: Propriedades básicas das Series
    #cria a Series "alunos"
    alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill','M14':'Cris','M19':'Jimi'})
    #atribui nomes para os vetores de dados e rótulos
    alunos.name = "alunos" 
    alunos.index.name = "matrículas" 
    #recupera e imprime as propriedades 
    print(alunos)
    print('-----------')
    tamanho = alunos.size 
    dados = alunos.values 
    rotulos = alunos.index 
    alunosTipo = type(alunos) 
    alunosDtype = alunos.dtype 
    alunosIdxDtype = alunos.index.dtype 
    print('número de elementos: ', tamanho)
    print('vetor de dados: ', dados)
    print('vetor de rótulos: ', rotulos)
    print('tipo (type): ', alunosTipo)
    print('dtype da Series:', alunosDtype)
    print('dtype do vetor de rótulos:', alunosIdxDtype)
   
    """
    Para encerrar a subseção, vamos mostrar a indexação
    booleana, a terceira e última técnica para indexar Series. No
    presente momento, realizaremos apenas uma introdução ao
    assunto, que será revisitado e mais bem detalhado em commits
    posteriores. Neste modo de indexação, subconjuntos de dados são
    selecionados com base nos valores da Series (valores do vetor de
    dados) e não em seus rótulos/índices.
    """
  elif parte == 3 :
    #P03: Indexação booleana
    #cria as Series "notas" e "alunos"
    notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])
    alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill','M14':'Cris','M19':'Jimi'})
    #obtém os índices dos alunos aprovados
    indiceAprovados = notas[notas >= 7].index
    #imprime os alunos aprovados
    print('relação de alunos aprovados:')
    print('---------------------------')
    print(alunos[indiceAprovados])
  
  elif parte == 4 :
    #P04: Busca em Series
    #cria a Series "alunos"
    alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill','M14':'Cris','M19':'Jimi'})
    #testa se rótulos fazem parte de uma Series
    tem_M13 = 'M13' in alunos
    tem_M99 = 'M99' in alunos
    print("existe o rótulo 'M13'? -> ",tem_M13) 
    print("existe o rótulo 'M99'? -> ",tem_M99) 
    print('---------------------------')
    #testa se valor faz parte de uma Series
    tem_Bob = alunos.isin(['Bob'])
    print("existe o valor 'Bob'") 
    print(tem_Bob)
    
  else :
    break
  continua = input("Deseja continuar visualizando as partes ? \n [S] - Sim \n [N] - Não \n : ").upper().strip()
  
print("Fim do Algorítimo")
