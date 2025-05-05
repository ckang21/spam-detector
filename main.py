import pickle

# Load the model and vectorizer
with open("notebooks/model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("notebooks/model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_spam(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return "SPAM" if prediction == 1 else "NOT SPAM"

if __name__ == "__main__":
    user_input = input("Enter a message to check if it's spam:\n> ")
    result = predict_spam(user_input)
    print("\nResult:", result)
