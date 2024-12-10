import requests

# 获取必应壁纸信息
url = "https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
response = requests.get(url)
data = response.json()

# 提取标题、URL 和描述
image = data['images'][0]
image_url = "https://bing.com" + image['url']
image_title = image.get('title', '🔖 今日必应壁纸')
image_description = image.get('copyright', '无描述')

# 生成 README.md 内容
readme_content = f"""# 🔖 {image_title}

![今日必应壁纸]({image_url})

> 📝 {image_description}
"""

if __name__ == '__main__':
    # 写入 README.md 文件
    with open("../../README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

    print("README.md 已生成！")
