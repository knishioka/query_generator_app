import pytest  # noqa: F401

from main import constraints_yaml_to_formatted_string, databases_yaml_to_formatted_string


def test_databases_yaml_to_formatted_string():
    yaml_file = "tests/test_databases.yaml"
    expected_result = """データベース: my_project_database
テーブル: users
カラム情報:
- user_id: ユーザーの一意識別子
- username: ユーザー名
- email: ユーザーのメールアドレス
- password_hash: パスワードのハッシュ値
- created_at: アカウント作成日時
- updated_at: アカウント情報の最終更新日時

テーブル: products
カラム情報:
- product_id: 商品の一意識別子
- name: 商品名
- description: 商品説明
- price: 価格
- stock_quantity: 在庫数
- category_id: 商品カテゴリのID
- created_at: 商品登録日時
- updated_at: 商品情報の最終更新日時"""
    print(expected_result)
    result = databases_yaml_to_formatted_string(yaml_file)
    print(result)
    assert result == expected_result


def test_constraints_yaml_to_formatted_string():
    yaml_file = "tests/test_query_constraints.yaml"
    expected_result = """- user_id: クエリにuser_idが含まれる場合、GROUP BY user_idで集計する必要がある
- order_id: クエリにorder_idが含まれる場合、GROUP BY order_idで集計する必要がある"""
    result = constraints_yaml_to_formatted_string(yaml_file)
    print(result)
    assert result == expected_result
