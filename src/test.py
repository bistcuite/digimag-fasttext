import fasttext

classifier = fasttext.load_model('model.bin')

result = classifier.test('test_processed.txt')
print("N:", result[0])
print("P:", result[1])
print("R:", result[2])