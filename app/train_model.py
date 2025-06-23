import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("email_spam_cleaned.csv")

#drop nan values
df = df.dropna(subset=['cleaned', 'label'])

X = df['cleaned']
y = df['label']

#train-test split
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

#TF-IDF
vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)

#training SVM
svm = LinearSVC()
svm.fit(X_train_tfidf, y_train)

#saving model & vectorizer
with open('model/svm_model.pkl', 'wb') as f:
    pickle.dump(svm, f)

with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved.")
