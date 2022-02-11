# digimag-fasttext
Text classification with fasttext and digikala magazine dataset

This model classificate texts in 7 categories :
1. `Video Games`
2. `Shopping Guide`
3. `Health Beauty`
4. `Science Technology`
5. `General`
6. `Art Cinema`
7. `Books Literature`

## Requirements
- `fasttext`
- `numpy`
- `pandas`

## Training and testing model
At first you should download digimag dataset from [this link](https://bit.ly/3ca4bm8) and extract it in `src` folder.

Now enter following command to train and save model(model will saved in `model.bin` file) :
```
$ python train.py
```

For testing model :
```
$ python test.py
```

## Example
```py
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
```

## License
***[MIT](LICENSE)***
