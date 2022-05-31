import pandas as pd
import numpy as np
# Formatação do código para usar cada etapa do desenvolvimento nesta primeira parte

continua = 0
while continua != "N" :
  parte = int(input("Escolha qual a parte do código você quer visualizar digite o número referente: "
                    "\n P01: Olá Series! - [1] "
                    "\n P02: Propriedades básicas das Series [2] "
                    "\n P03: Indexação booleana [3] "
                    "\n P04: Busca em Series [4] "
                    "\n P05: Inserindo, Alterando e Removendo elementos de Series [5] "
                    "\n #P06: Iteração [6] "
                    "\n P07: Operações aritméticas com computação vetorizada [7] "
                    "\n P08: o valor NaN [8] "
                    "\n P09: Índices datetime [9] "
                    "\n P10: Índexação hierárquica [10] "
                    "\n : " ))
    # Se você aplicar a função type() sobre qualquer Series, sempre
    # receberá como resposta o tipo pandas.core.series.Series . Outra
    # consideração importante é que toda Series está associada a outras
    # propriedades elementares além do dtype . São elas:
    # values : vetor de dados;
    # index : vetor de rótulos;
    # name : nome do vetor de dados;
    # size : tamanho da Series (número de elementos);
    # index.name : nome do vetor de rótulos;
    # index.dtype : dtype do vetor de rótulos.
    # No programa seguinte, apresentamos a forma para trabalhar com
    # essas propriedades.
    
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
   
    """
    Indexação
    Utilizamos colchetes [ ] para indexar (acessar e obter) elementos
    de uma Series. A pandas permite o emprego de três diferentes
    técnicas: indexação tradicional, fatiamento e indexação booleana.
    """
  
  
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
   
    """
    Busca
    O próximo exemplo mostra como verificar se determinados rótulos
    ou valores estão presentes em uma Series.
    """
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
    
    """
    Modificação
    No próximo exemplo, apresentamos a forma básica para inserir,
    modificar e excluir elementos.
    """
  elif parte == 5:
    #P05: Inserindo, Alterando e Removendo elementos de Series
    #cria a Series "alunos"
    alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
     'M14':'Cris','M19':'Jimi'})
    print('Series original:')
    print(alunos)
    #insere o aluno de matrícula M55, Rakesh
    alunos['M55'] = 'Rakesh'
    #altera os nomes Bill, Cris e Jimi para Billy, Cristy e Jimmy
    alunos['M13'] = 'Billy'
    alunos[['M14','M19']] = ['Cristy','Jimmy']
    #remove o aluno de matrícula M02 (Bob)
    alunos = alunos.drop('M02')
    print('---------------------------')
    print('Series após as alterações:')
    print(alunos)
    
    """
    Computação vetorizada
    É possível utilizar a tradicional estrutura for … in para iterar sobre
    uma Series (ou seja, para percorrer "de cabo a rabo" o vetor de dados ou o de rótulos):
    """
  elif parte == 6 :
    #P06: Iteração
    alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
        'M14':'Cris','M19':'Jimi'})
    #itera sobre os dados (nomes dos alunos)
    for aluno in alunos: print(aluno)
    #itera sobre os índices (matrículas)
    for indice in alunos.index: print(indice)
      
    """
    Entretanto, em grande parte das situações práticas, não
    precisaremos fazer uso desse recurso. Isso porque, em geral, as
    operações da pandas podem ser executadas através do mecanismo
    conhecido como computação vetorizada (vectorization). Neste
    processo, as operações são realizadas sobre cada elemento da
    Series automaticamente, sem a necessidade de programar um laço
    com o comando for . Alguns exemplos:
    Se s é uma Series com valores numéricos, e fazemos s * 2 ,
    obteremos como resultado uma Series que conterá todos os
    elementos de s multiplicados por 2.
    Ao efetuarmos uma soma de duas Series s1 e s2 , teremos
    como resultado uma nova Series em que o valor de um rótulo
    (ou índice) i será igual a s1[i] + s2[i] . E da mesma forma
    ocorrerá para todos os demais rótulos.
    O programa a seguir demonstra estes conceitos na prática. Uma
    outra novidade introduzida no exemplo é a importação da biblioteca
    NumPy e a utilização de um de seus métodos, denominado sqrt()
    """
  elif parte == 7 :
    #P07: Operações aritméticas com computação vetorizada
    #cria as Series s1 e s2
    s1 = pd.Series([2,4,6])
    s2 = pd.Series([1,3,5])
    print('s1:'); print(s1)
    print('s2:'); print(s2)
    #efetua as operações aritméticas
    print('---------------------------')
    print('s1 * 2')
    print(s1 * 2) 
    print('---------------------------')
    print('s1 + s2')
    print(s1 + s2)
    print('---------------------------')
    print('raiz quadrada dos elementos de s1')
    print(np.sqrt(s1)) #com a Numpy!
    
    """
    O valor NaN
    O programa a seguir examina o comportamento da pandas ao
    realizar uma operação aritmética (soma) envolvendo duas
    Series que não possuem os rótulos inteiramente compatíveis.
    """
  elif parte == 8 :
    #P08: o valor NaN
    verde = pd.Series({'BR':1, 'FR': 0, 'IT':1, 'UK': 0})
    azul = pd.Series({'AR':1, 'BR':1, 'FR': 1, 'IT':0, 'UK': 1})
    soma = verde + azul
    print("soma:")
    print(soma)
    print('---------------------------')
    print("isnull(soma):")
    print(pd.isnull(soma))

    """
    O programa a seguir mostra como podemos criar essa série
    temporal, configurando explicitamente o vetor de índices para que
    ele possua o tipo data ( dtype datetime64 ). Afinal de contas, essa é
    a semântica correta da nossa série de registro temperaturas!
    """
  elif parte == 9 :
    #P09: Índices datetime
    import pandas as pd 
    #(1)-cria a série temporal
    dias = ['10/02/2019', '11/02/2019','12/02/2019','13/02/2019',
     '14/02/2019','15/02/2019']
    temp_max = [31,35,34,28,27,27]
    serie_temporal = pd.Series(temp_max,index=dias)
    #(2)-converte o tipo do índice para datetime e imprime a série
    serie_temporal.index = pd.to_datetime(serie_temporal.index, 
     format='%d/%m/%Y')
    print(serie_temporal)  
    """
    A indexação hierárquica é um recurso oferecido pela pandas para
    permitir que você trabalhe com mais de um nível de indexação.
    Para que o conceito fique claro, o exemplo desta seção mostra
    como utilizar este recurso para criar uma Series com informações
    sobre os nomes das moedas dos cinco países mostrados na figura a
    seguir. Desta vez, a Series poderá ser indexada não apenas pela
    sigla do país, mas também pelo nome de seu continente.
    """
  elif parte == 10 :  
    #P10: Índexação hierárquica
    import pandas as pd
    moedas = ['Peso', 'Real', 'Euro', 'Euro', 'Libra']
    paises = [['América','América','Europa','Europa','Europa'],
     ['AR','BR','FR','IT','UK']]
    paises = pd.Series(moedas, index=paises)
    print(paises) #imprime toda a Series
    print('----------------------') 
    print(paises['América']) #{AR: Peso, BR:Real}
    print('----------------------') 
    print(paises[:,'IT']) #{Europa: Euro}
    print('----------------------') 
    print(paises['Europa','IT']) #Euro
    
  else :
    break
  continua = input("Deseja continuar visualizando as partes ? \n [S] - Sim \n [N] - Não \n : ").upper().strip()
  
print("Fim do Algorítimo")
