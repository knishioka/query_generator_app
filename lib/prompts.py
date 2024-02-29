SYSTEM_MESSAGE_PROMPT_TEMPLATE = """あなたはSQL クエリを書くエキスパートです.
以下のテーブル情報を参考に、Questionに答える{dialect}のクエリとその説明を生成してください。
クエリ作成時には制約を考慮してださい。
"""

HUMAN_MESSAGE_PROMPT_TEMPLATE = """テーブル情報:
{table_info}

制約:
{constraints}

Question: {question}

クエリ:
"""
