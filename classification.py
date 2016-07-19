data = [
    [1, 1, 0],
    [1, 1, 0],
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
]

targets = [1, 1, 1, -1, -1, -1]

test_data = [1, 1, 1]

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(data, targets)

result = model.predict(test_data)

print(result)