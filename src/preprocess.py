import pandas as pd
from pathlib import Path
import tqdm

train_df = pd.read_csv('train.csv', delimiter="	", index_col=False)
test_df = pd.read_csv('test.csv', delimiter="	", index_col=False)
eval_df = pd.read_csv('dev.csv', delimiter="	", index_col=False)

# drop the label columns
train_df.drop(columns=['Unnamed: 0', 'label'], inplace=True)
test_df.drop(columns=['Unnamed: 0', 'label'], inplace=True)
eval_df.drop(columns=['Unnamed: 0', 'label'], inplace=True)

train_processed = Path('train_processed.txt')
test_processed = Path('test_processed.txt')
eval_processed = Path('dev_processed.txt')

with train_processed.open('w', encoding='utf-8') as f:
    for i in tqdm.trange(len(train_df)):
                f.write("__label__" + str(train_df['label_id'][i]) + " " + train_df['content'][i] + "\n")

with test_processed.open('w', encoding='utf-8') as f:
    for i in tqdm.trange(len(test_df)):
                f.write("__label__" + str(test_df['label_id'][i]) + " " + test_df['content'][i] + "\n")

with eval_processed.open('w', encoding='utf-8') as f:
    for i in tqdm.trange(len(eval_df)):
                f.write("__label__" + str(eval_df['label_id'][i]) + " " + eval_df['content'][i] + "\n")