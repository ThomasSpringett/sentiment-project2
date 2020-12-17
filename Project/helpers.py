import numpy as np
import pandas as pd

    
def oftype(x):
    if isinstance(x,pd.core.series.Series):
        print ('pandas series')
    elif isinstance(x,pd.DataFrame):
        print ("pandas DataFrame")
        df = x
        print (df.shape)
        percent = 100*(df.isnull().sum().sum()/(df.shape[0]*df.shape[1]))
        print ("\nThe total number of missing values: {} or {:.1f}%. \
        ".format(df.isnull().sum().sum(),percent))
        display (df.head())
    elif isinstance(x,np.ndarray):
        df = x
        print ("numpy",df.shape)
    elif isinstance(x,int):
        print ("Integer 32")
    elif isinstance(x,float):
        print ("float")
    elif isinstance(x,str):
        print ("string of length: ",len(x),",",x)
    elif isinstance(x,dict):
        print ("Dictionary of length: ",len(x))
    elif isinstance(x,list):
        print ("List of length: ",len(x))
    else:
        print ("Type Unknown") 
        
def describe_df(df):
    try:
        print (df.shape)
        percent = 100*(df.isnull().sum().sum()/(df.shape[0]*df.shape[1]))
        print ("\nThe total number of missing values: {} or {:.1f}%. \
        ".format(df.isnull().sum().sum(),percent))
        display (df.head())
        #print (df.info())
        #print (df.dtypes) 
    except AttributeError:
        pass
    except NameError:
        pass
def restart():
    azdias_clean = pd.read_pickle("azdias_clean.pkl")
    pca2 = pickle.load(open('pca_robust_10', 'rb'))
    Xpca25 = pickle.load(open("Xpca10", 'rb'))
    return azdias_clean, pca10, Xpca10

def mysample(df,sample_size):
    print (oftype(df))
    df_s=random.sample(list(df), 1000)
    print (oftype(df_s))
    return df_s