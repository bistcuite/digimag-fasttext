import fasttext
import pandas as pd
import numpy as np

categories = {
    1 : 'Video Games',
    2 : 'Shopping Guide',
    3 : 'Health Beauty',
    4 : 'Science Technology',
    5 : 'General',
    6 : 'Art Cinema',
    7 : 'Books Literature',
}

classifier = fasttext.load_model('model.bin')

test_df = pd.read_csv('test.csv', delimiter="	", index_col=False)
i = np.random.randint(0, len(test_df))
input_eg = test_df['content'][i]
input_eg_label = test_df['label_id'][i]
print("Input label :", categories[input_eg_label])
result = classifier.predict(input_eg)
print("Predicted label :", categories[int(result[0][0].replace("__label__", ""))])