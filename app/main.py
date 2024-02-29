import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI
from prompts import HUMAN_MESSAGE_PROMPT_TEMPLATE, SYSTEM_MESSAGE_PROMPT_TEMPLATE

DEFAULT_TABLE_INFO = """
### 1. ユーザーテーブル (Users)
- user_id : ユーザーの一意識別子
- username : ユーザー名
- email : ユーザーのメールアドレス
- password_hash : パスワードのハッシュ値
- created_at : アカウント作成日時
- updated_at : アカウント情報の最終更新日時
### 2. 商品テーブル (Products)
- product_id : 商品の一意識別子
- name : 商品名
- description : 商品説明
- price : 価格
- stock_quantity : 在庫数
- category_id : 商品カテゴリのID
- created_at : 商品登録日時
- updated_at : 商品情報の最終更新日時
### 3. カテゴリテーブル (Categories)
- category_id : カテゴリの一意識別子
- name : カテゴリ名
- description : カテゴリ説明
- parent_id : 親カテゴリのID（サブカテゴリの場合）
### 4. 注文テーブル (Orders)
- order_id : 注文の一意識別子
- user_id : 注文したユーザーのID
- total_price : 注文の合計金額
- status : 注文の状態（例: 処理中、発送済み）
- created_at : 注文日時
- updated_at : 注文情報の最終更新日時
### 5. 注文詳細テーブル (Order_Details)
- order_detail_id : 注文詳細の一意識別子
- order_id : 注文のID
- product_id : 商品のID
- quantity : 数量
- price : 価格（時点）
### 6. ショッピングカートテーブル (Shopping_Carts)
- cart_id : カートの一意識別子
- user_id : ユーザーのID
- product_id : 商品のID
- quantity : 数量
- added_at : カートへの追加日時
"""


def main():
    # Main Panel
    st.title("Query Generator for SQL Database")
    st.write("You can use this tool to generate SQL queries for your database.")

    # Sidebar
    st.sidebar.text_area("Table Info", key="table_info", value=DEFAULT_TABLE_INFO, height=500)

    # Add chatbox to send request to ChatGPT by langchain
    user_input = st.text_input("Enter your message")
    if st.button("Send"):
        response = generate_sql_query(user_input)
        st.write(response)


def generate_sql_query(message):
    system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_MESSAGE_PROMPT_TEMPLATE)
    human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_MESSAGE_PROMPT_TEMPLATE)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    table_info = st.session_state["table_info"]

    model = ChatOpenAI(model="gpt-4", streaming=True)
    chain = chat_prompt | model | StrOutputParser()

    return chain.invoke({"table_info": table_info, "analysis": message})


def send_request_to_chatgpt():
    # Code to send request to ChatGPT by langchain and get response
    # Replace this with your actual implementation
    response = "This is the response from ChatGPT"
    return response


if __name__ == "__main__":
    main()
