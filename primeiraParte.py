import pandas as pd
bandeiras= pd.read_csv(f"C:/Users/Jessica e Gustavo/PycharmProjects/pythonProject/ProjetoPandas/pandas-master/flags.csv")
paises = pd.read_csv(f"C:/Users/Jessica e Gustavo/PycharmProjects/pythonProject/ProjetoPandas/pandas-master/countries.csv")
tudojunto = pd.merge(bandeiras, paises,
                     how="inner",
 left_on="name", right_on="country")
print(tudojunto)
print(10*"---")
print(bandeiras)
