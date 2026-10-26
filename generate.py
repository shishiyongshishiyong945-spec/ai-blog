from google import genai
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="""
仕事効率化に関するブログ記事を書いてください。

条件
・HTML形式
・h2とh3を使う
・箇条書きを使う
・2000文字以上
・初心者向け
・SEOを意識
・結論→理由→具体例→まとめ
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
