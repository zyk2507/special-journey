import pandas as pd
from xpinyin import Pinyin

# Load Excel file into a DataFrame
df = pd.read_excel('input.xlsx')

# Initialize Pinyin object
p = Pinyin()

# Convert Chinese names to Pinyin

df['Password'] = 'password'
df['email'] = 'example@example.com'
df.insert(3, 'Original Chinese Name', df['姓名'].copy())
df['姓名'] = df['姓名'].apply(lambda x: p.get_pinyin(x, ''))

# Save DataFrame as CSV file
df.to_csv('output.csv', index=False)
