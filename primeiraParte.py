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
    lst_matriculas = ['M02','M05','M13','M14','M19']
    lst_nomes = ['Bob','Dayse','Bill','Cris','Jimi']
    alunos = pd.Series(lst_nomes,index=lst_matriculas)
    #imprime as duas Series
    print(notas); print("---------------"); print(alunos)
   
  elif parte == 2
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
    alunos_tipo = type(alunos) 
    alunos_dtype = alunos.dtype 
    alunos_idx_dtype = alunos.index.dtype 
    print('número de elementos: ', tamanho)
    print('vetor de dados: ', dados)
    print('vetor de rótulos: ', rotulos)
    print('tipo (type): ', alunos_tipo)
    print('dtype da Series:', alunos_dtype)
    print('dtype do vetor de rótulos:', alunos_idx_dtype)
    
else :
    break
  continua = input("Deseja continuar visualizando as partes ? \n [S] - Sim \n [N] - Não \n : ").upper().strip()
  
print("Fim do Algorítimo")
