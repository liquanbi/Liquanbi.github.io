import os

def generate_index_html(directory=".", output_filename="index.html"):
    """
    扫描指定目录下所有的 .html 文件（不包括输出文件本身），
    并生成一个包含这些文件链接的新的 HTML 文件。
    """
    # 存储找到的 HTML 文件名
    html_files = []

    # 遍历当前目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否是以 .html 结尾，并且不是我们要生成的那个文件
        if filename.endswith(".html") and filename != output_filename:
            html_files.append(filename)

    # 对文件名进行排序，使其在索引页面上看起来更有序
    html_files.sort()

    # --- 生成 HTML 内容 ---
    
    # 1. 头部和样式
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文件索引 - 自动生成</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }}
        h1 {{ border-bottom: 2px solid #eee; padding-bottom: 10px; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; background-color: #f9f9f9; padding: 10px; border-radius: 5px; box-shadow: 1px 1px 3px rgba(0,0,0,0.1); }}
        a {{ text-decoration: none; color: #007bff; font-weight: bold; }}
        a:hover {{ text-decoration: underline; color: #0056b3; }}
        .count {{ color: #6c757d; font-size: 0.9em; margin-left: 15px; }}
    </style>
</head>
<body>
    <h1>📂 目录下的 HTML 文件列表</h1>
    <p class="count">共找到 **{len(html_files)}** 个 HTML 文件。</p>
    <ul>
"""

    # 2. 链接列表
    if not html_files:
        html_content += '        <li><p>未找到其他 HTML 文件。</p></li>\n'
    else:
        for file in html_files:
            # 这里的 <a href="{file}"> 会直接链接到同目录下的文件
            html_content += f'        <li><a href="{file}">{file}</a></li>\n'

    # 3. 底部
    html_content += """    </ul>
    <hr>
    <footer>
        <p>此页面由 Python 脚本自动生成。</p>
    </footer>
</body>
</html>
"""

    # --- 写入文件 ---
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ 成功生成索引文件: {output_filename}")
        print(f"   共包含 {len(html_files)} 个链接。")
    except Exception as e:
        print(f"❌ 写入文件时发生错误: {e}")

if __name__ == "__main__":
    # 默认会在当前目录下生成 index.html
    generate_index_html()
