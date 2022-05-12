import pandas as pd
# Formatação do código para usar cada etapa do desenvolvimento nesta primeira parte

continua = 0
while continua != "N" :
  parte = int(input("Escolha qual a parte do código você quer visualizar digite o número referente: \n P01: Olá Series! - [1] \n : " ))
  
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
    
  else :
    break
  continua = input("Deseja continuar visualizando as partes ? \n [S] - Sim \n [N] - Não \n : ").upper().strip()
  
print("Fim do Algorítimo")
