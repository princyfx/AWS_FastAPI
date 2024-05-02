# frontend.py
import streamlit as st
import requests
import json

# Define the FastAPI endpoint URL
FASTAPI_URL = "http://localhost:8004"

def get_answer(context, question):
    # Make a POST request to the FastAPI endpoint
    response = requests.post(f"{FASTAPI_URL}/qna/", json={"context": context, "question": question})

    # Check if the request was successful
    if response.status_code == 200:
        data = response.text
        # Parse the JSON string
        jsonData = json.loads(data)

# Access the value of the "answer" key
        answer = jsonData["answer"]
        print(answer)
        return answer
    else:
        return "Error: Failed to get answer"


# Streamlit UI
def main():
    st.title("Question Answering System")

    # Input fields for context and question
    context = st.text_area("Enter Context", "", height=200)
    question = st.text_input("Enter Question", "")

    # Button to get the answer
    if st.button("Get Answer"):
        if context and question:
            result = get_answer(context, question)
            st.write("Answer:", result)
        else:
            st.write("Please provide both context and question.")

if __name__ == "__main__":
    main()
