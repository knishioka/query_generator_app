# noqa: E501

SYSTEM_MESSAGE_PROMPT_TEMPLATE = """
あなたはSQL クエリを書くエキスパートです.
テーブル情報を参考に、分析用のクエリを書いてください.
"""

HUMAN_MESSAGE_PROMPT_TEMPLATE = """
テーブル情報:
{table_info}

分析:
{analysis}

クエリ:
"""
