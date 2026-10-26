from google import genai
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="""
あなたはSEOに強いITブロガーです。

Microsoft 365 Copilot
Teams
Outlook
Excel
Word
PowerPoint

に関するブログ記事を書いてください。

条件
・HTML形式
・h2とh3を使用
・箇条書きを使用
・2500文字以上
・SEOを意識
・初心者向け
・タイトルを作成
・まとめを入れる
・毎回異なるテーマを選ぶ
・実務で使える内容にする
topics = [
    "Microsoft 365 Copilot",
    "Teams",
    "Outlook",
    "Excel",
    "Word",
    "PowerPoint"
]

"""


)

html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>仕事効率化ラボ</title>
</head>
<body>
<h1>仕事効率化ラボ</h1>
<article>
{response.text}
</article>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
