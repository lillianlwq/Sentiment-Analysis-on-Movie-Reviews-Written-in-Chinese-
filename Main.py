import pandas as pd
import sys
import codecs

data = pd.read_csv('df_output.csv')
d1 = data['CONTENT']
#d1.set_option('max_colwidth', 200)
#d1.columns = ['CONTENT', 'RATINGS']
d1.show()
