import sys
import pandas as pd
import sqlite3 as sq


data = pd.read_csv(sys.argv[1] + '.csv', index_col=False)

data['level'] = 0

con  = sq.connect(sys.argv[1] + '.db')

data.to_sql('word', con)