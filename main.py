import streamlit as st
import yaml
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI

from lib.prompts import HUMAN_MESSAGE_PROMPT_TEMPLATE, SYSTEM_MESSAGE_PROMPT_TEMPLATE


def main():
    # Main Panel
    st.title("Query Generator for SQL Database")
    st.write("You can use this tool to generate SQL queries for your database.")

    # Sidebar
    databases_yaml_path = "config/databases.yaml"
    table_info = databases_yaml_to_formatted_string(databases_yaml_path)
    constraints_yaml_path = "config/query_constraints.yaml"
    constraints = constraints_yaml_to_formatted_string(constraints_yaml_path)

    st.sidebar.text_area("Table Info", key="table_info", value=table_info, height=500)
    st.sidebar.text_area("Constraints", key="constraints", value=constraints, height=500)

    st.chat_message("assistant").write("What kind of query would you like to generate?")
    user_msg = st.chat_input("ここにメッセージを入力")
    if user_msg:
        st.chat_message("user").write(user_msg)
        with st.spinner("回答を生成中..."):
            response = generate_sql_query(user_msg)
            st.chat_message("assistant").markdown(response)


def databases_yaml_to_formatted_string(yaml_file):
    """
    Reads database and table information from a YAML file and converts it into a formatted string.

    This function processes a YAML file containing databases and their tables, including columns and descriptions,
    and formats this information into a readable string suitable for documentation or display purposes.

    Parameters:
    - yaml_file: Path to the YAML file containing database schemas.

    Returns:
    - A string representing the database and table information in a formatted structure.
    """
    # String to store the result
    result_str = ""

    # Load the YAML file
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Assemble the database and table information into a string
    for db in data["databases"]:
        result_str += f"データベース: {db['name']}\n"
        for table in db["tables"]:
            result_str += f"テーブル: {table['name']}\n"
            result_str += "カラム情報:\n"
            for column in table["columns"]:
                result_str += f"- {column['name']}: {column['description']}\n"
            result_str += "\n"  # Insert a blank line between tables

    return result_str.strip()  # Remove any trailing newline characters


def constraints_yaml_to_formatted_string(yaml_file):
    """
    Reads query constraints from a YAML file and converts them into a text format
    that can be used in ChatGPT prompts.

    Parameters:
    - yaml_file: Path to the YAML file

    Returns:
    - A string representing the query constraints in text format
    """
    # String to store the result
    result_str = ""

    # Load the YAML file
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Convert the constraints to text format
    for constraint in data["query_constraints"]:
        column = constraint["column"]
        constraint_description = constraint["constraint"]
        result_str += f"- {column}: {constraint_description}\n"

    return result_str.strip()


def generate_sql_query(message):
    system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_MESSAGE_PROMPT_TEMPLATE)
    human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_MESSAGE_PROMPT_TEMPLATE)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    table_info = st.session_state["table_info"]
    constraints = st.session_state["constraints"]

    model = ChatOpenAI(model="gpt-4", streaming=True)
    chain = chat_prompt | model | StrOutputParser()

    return chain.invoke(
        {"table_info": table_info, "constraints": constraints, "question": message, "dialect": "athena"}
    )


if __name__ == "__main__":
    main()
