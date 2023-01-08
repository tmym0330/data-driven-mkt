import pandas as pd
import numpy as np

# 1: tính net promoter
# score >= 0 and <= 6: detractor
# (7,8): passive
# (9,10): promoter
df = pd.read_csv('nps.csv')
print(df)
# 2 : tính churn rate
