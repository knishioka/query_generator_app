import streamlit as st
import yaml
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI
from prompts import HUMAN_MESSAGE_PROMPT_TEMPLATE, SYSTEM_MESSAGE_PROMPT_TEMPLATE


def main():
    # Main Panel
    st.title("Query Generator for SQL Database")
    st.write("You can use this tool to generate SQL queries for your database.")

    # Sidebar
    # YAMLファイルのパスを指定
    yaml_file_path = "config/databases.yaml"
    table_info = yaml_to_formatted_string(yaml_file_path)

    st.sidebar.text_area("Table Info", key="table_info", value=table_info, height=500)

    # Add chatbox to send request to ChatGPT by langchain
    user_input = st.text_input("Enter your message")

    if st.button("Send"):
        response = generate_sql_query(user_input)
        st.markdown(response)


def yaml_to_formatted_string(yaml_file):
    # 結果を格納するための文字列
    result_str = ""

    # YAMLファイルを読み込む
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # データベースとテーブルの情報を文字列に組み立てる
    for db in data["databases"]:
        result_str += f"データベース: {db['name']}\n"
        for table in db["tables"]:
            result_str += f"テーブル: {table['name']}\n"
            result_str += "カラム情報:\n"
            for column in table["columns"]:
                result_str += f"- {column['name']}: {column['description']}\n"
            result_str += "\n"  # テーブル間に空行を挿入

    return result_str.strip()  # 末尾の余分な改行を削除


def generate_sql_query(message):
    system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_MESSAGE_PROMPT_TEMPLATE)
    human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_MESSAGE_PROMPT_TEMPLATE)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    table_info = st.session_state["table_info"]

    model = ChatOpenAI(model="gpt-4", streaming=True)
    chain = chat_prompt | model | StrOutputParser()

    return chain.invoke({"table_info": table_info, "question": message, "dialect": "athena"})


def send_request_to_chatgpt():
    # Code to send request to ChatGPT by langchain and get response
    # Replace this with your actual implementation
    response = "This is the response from ChatGPT"
    return response


if __name__ == "__main__":
    main()
