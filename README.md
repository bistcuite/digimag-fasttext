# DigiMag fasttext

Text classification with fasttext and digikala magazine dataset.

Model classifies texts in 7 categories :
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

```
$ pip install -r requirements.txt
```

## Training and testing model
At first you should download digimag dataset from [this link](https://bit.ly/3ca4bm8) and extract it into `src` directory.

Now enter following command to preprocess dataset, train and save model(model will saved in `model.bin` file) :
```
$ python preprocess.py && python train.py
```

Test model :
```
$ python test.py
```

## Example
```py
import fasttext

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
input_txt = "your text"
result = classifier.predict(input_txt)
print("Predicted label :", categories[int(result[0][0].replace("__label__", ""))])
```
See [example.py](src/example.py).

## License
***[MIT](LICENSE)***
