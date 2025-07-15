import streamlit as st
from search_engine import SemanticSearchEngine, load_documents

st.title("Semantic Search Engine")

# Load and prepare
search_engine = SemanticSearchEngine()
documents = load_documents('data.txt')
search_engine.add_documents(documents)

query = st.text_input("Search your question:")
top_k = st.radio("How many results do you want to see?", [1, 3, 5])


if query:
    results = search_engine.search(query, top_k=top_k)
    
    if results:
        st.write(f"### Results for: '{query}'")
        for result in results:
            st.write(f"Score: {result['similarity']:.2f}")
            st.write(f"Document:{result['document']}")
    else:
        st.warning("No results found.")
