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
Now enter following command to train and save model(model will saved on `model.bin` file) :
```
$ python train.py
```

For testing model :
```
$ python test.py
```
