import os
import pandas as pd
import numpy as np

name = os.environ.get('NAME','World')
print(f'Hello, {name}')

pandas_version = pd.__version__
print(f'You currently have version {pandas_version} of Pandas installed. This was pulled in from your requirements.txt file.')

max_number = os.environ.get('MAX',1000)
rows = os.environ.get('ROWS', 1000)
print(f'This is a randomly generated dataframe with {rows} rows and numbers between 0 and {max_number}.')
df = pd.DataFrame(np.random.randint(0,max_number,size=(rows, 4)), columns=list('ABCD'))
print(df)
