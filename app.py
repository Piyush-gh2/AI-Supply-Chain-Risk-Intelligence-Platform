import streamlit as st

from src.agents import run_supply_chain_ai
from src.rag import load_knowledge, build_index, retrieve

st.title("📦 AI Supply Chain Risk Intelligence Platform")

query = st.text_input("Ask Supply Chain Insight")

if st.button("Analyze Supply Chain"):

    df, prediction, risk, explanation = run_supply_chain_ai()

    st.subheader("📊 Supply Chain Dataset")
    st.dataframe(df)

    st.subheader("📈 Demand Forecast")
    st.write(f"Predicted Demand Next Month: {prediction:.2f}")

    st.subheader("⚠️ Risk Detection")
    st.write(risk)

    st.subheader("🧠 Explainable AI Insight")
    st.write(explanation)

    st.line_chart(df.set_index("month")["demand"])

    # RAG
    docs = load_knowledge()
    index = build_index(docs)

    if query:

        insights = retrieve(query, docs, index)

        st.subheader("🔎 Supply Chain Insights")

        for i in insights:
            st.write(i)