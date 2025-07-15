# 🔍 Semantic Search Engine with Streamlit

This project is a **simple semantic search engine** built using **Sentence Transformers** and **Streamlit**.  
It allows you to search for the most relevant sentences or documents based on **semantic meaning**, not just keyword matching.

---

## ✅ Features
- Uses **pre-trained sentence embeddings** (`all-MiniLM-L6-v2` by default).
- Finds **top-k most semantically similar documents** for a given query.
- Reads documents from a `.txt` file.
- Interactive **Streamlit web app** interface.

---

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
git clone <https://github.com/Hima-bindu03/Search_Engine.git>
cd Search_engine

### 2️⃣ Create a Virtual Environment

#### Windows
python -m venv venv
venv\Scripts\activate

#### macOS/Linux
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt


### ▶️ Running the App

streamlit run app.py


### 🔧 How It Works
* The app loads all sentences from data.txt.

* SentenceTransformer converts each sentence into a vector embedding.

* When you search, your query is also converted into a vector.

* Cosine similarity is calculated between the query and all document vectors.

* The most similar documents are returned.



