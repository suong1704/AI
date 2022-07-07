import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Using One Hot Encoding
Text = "I am learning NLP"
dt = pd.get_dummies(Text.split())
print(dt)

# Count Vectorizing
text = ["I love NLP and I will learn NLP in 2month "]
# create the transform
vectorizer = CountVectorizer()
# tokenizing
vectorizer.fit(text)
# encode document
vector = vectorizer.transform(text)
# summarize & generating output
print(vectorizer.vocabulary_)
print(vector.toarray())