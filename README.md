# 🛑 Spam Message Detector (Python)

This is a simple spam detection app built with Python and scikit-learn. It uses the popular SMS Spam Collection dataset to train a classifier that can distinguish between spam and non-spam (ham) messages.

---

## 📁 Project Structure
```
spam-detector/
├── data/
│ └── SMSSpamCollection
├── model/
│ ├── model.pkl
│ └── vectorizer.pkl
├── notebooks/
│ └── spam_eda.ipynb
├── main.py
└── README.md
```
---

## 🧠 How It Works

- The model is trained using a Naive Bayes classifier on TF-IDF features extracted from SMS text messages.
- It predicts whether a new message is `SPAM` or `NOT SPAM`.

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install scikit-learn pandas
```

### 2. Run the app

```
python main.py
```

## Dataset

- Dataset used: UCI SMS Spam Collection
- 5,574 labeled SMS messages classified as "ham" or "spam".

## Future Ideas

- Improve accuracy with more diverse data
- Add a web interface using Streamlit or Flask
- Show prediction probabilities
- Train with newer spam sources (e.g., email, social media)

## License

- This project is for educational use and built with open data.
