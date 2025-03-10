#Función 1
def cargar_dataset(archivo):
    import pandas as pd
    import os

    extension = os.path.splitext(archivo)[1].lower()

    if extension == '.csv':
        df= pd.read_csv(archivo, index_col=0)
        return (df)
    elif extension == '.xlsx':
        df= pd.read_excel(archivo)
        return (df)
    else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")
################################################################################################

#Función 2

def sustitución_nulos(dataframe):
    import pandas as pd
    #Separar columnas cuantitativas y cualitativas del dataframe
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    #Separar las numéricas entre pares e impares
    pares_numericas = cuantitativas_con_nulos.iloc[:, ::2]  
    impares_numericas = cuantitativas_con_nulos.iloc[:, 1::2]

    #Sustituir valores nulos
    pares_limpios = pares_numericas.fillna(round(pares_numericas.mean(), 1))
    impares_limpios = impares_numericas.fillna(99)
    cualitativas_limpias=cualitativas_con_nulos.fillna("Este_es_un_valor_nulo")
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([pares_limpios, impares_limpios, cualitativas_limpias], axis=1)
    
    return(Datos_sin_nulos)
################################################################################################

#Función 3

def cuenta_valores_nulos(dataframe):
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()
    
    return("Valores nulos por columna:", valores_nulos_cols,
            "Valores nulos por dataframe: ", valores_nulos_df)
################################################################################################

#Función 4

def valores_atipicos(dataframe):
    import pandas as pd
    cuantitativas=dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas= dataframe.select_dtypes(include=['object', 'datetime','category'])
    y=cuantitativas

    percentile25=y.quantile(0.25) #Q1
    percentile75=y.quantile(0.75) #Q3
    iqr= percentile75 - percentile25

    Limite_Superior_iqr= percentile75 + 1.5*iqr
    Limite_Inferior_iqr= percentile25 - 1.5*iqr

    data3_iqr= cuantitativas[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
    data4_iqr=data3_iqr.copy()
    data4_iqr=data4_iqr.fillna(round(data3_iqr.mean(),1))
    Datos_limpios = pd.concat([cualitativas, data4_iqr], axis=1)
    return Datos_limpios
################################################################################################
