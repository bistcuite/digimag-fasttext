import fasttext

classifier = fasttext.train_supervised(
        input='train_processed.txt',
        lr=0.1,
        epoch=10,
        wordNgrams=2
)

classifier.save_model('model.bin')
print("Done!!!")