# violence_classifier.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

class ViolenceClassifier:
    def __init__(self):
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.train_classifier()

    def train_classifier(self):
        # Simple training data
        texts = [
            "Um tiroteio deixou três feridos no centro da cidade.",
            "A polícia prendeu suspeitos de tráfico de drogas.",
            "Houve um assalto à mão armada no banco local.",
            "Uma briga violenta eclodiu na praça central.",
            "O festival de música atraiu milhares de pessoas.",
            "Nova exposição de arte inaugura no museu da cidade.",
            "Restaurante popular comemora 10 anos de funcionamento.",
            "Parque da cidade recebe melhorias na iluminação."
        ]
        labels = [1, 1, 1, 1, 0, 0, 0, 0]  # 1 for violent, 0 for non-violent
        self.model.fit(texts, labels)

    def predict_violence_likelihood(self, text):
        return self.model.predict_proba([text])[0][1]