# How to set Column Widths in a Pandas DataFrame

import pandas as pd

pd.set_option('display.max_colwidth', 500)

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl'],
    'description': [
        'Content creator at https://example.com ABC 123',
        'Content creator at https://bobbyhadz.com ABC 123',
        'Content creator at https://google.com ABC 123'
    ],
})

print(df)