import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Welcome to my app!")

    # Add chatbox to send request to ChatGPT by langchain
    user_input = st.text_input("Enter your message")
    if st.button("Send"):
        response = send_request_to_chatgpt(user_input)
        st.write(response)

def send_request_to_chatgpt(message):
    # Code to send request to ChatGPT by langchain and get response
    # Replace this with your actual implementation
    response = "This is the response from ChatGPT"
    return response

if __name__ == "__main__":
    main()