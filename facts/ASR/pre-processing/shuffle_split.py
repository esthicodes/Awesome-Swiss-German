import sys
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(sys.argv[1])
train, dev_test = train_test_split(df, test_size=0.3, shuffle=True, random_state=42)
dev, test = train_test_split(dev_test, test_size=0.5, shuffle=True, random_state=42)

train.to_csv('train.csv', index=False)
dev.to_csv('dev.csv', index=False)
test.to_csv('test.csv', index=False)
    
