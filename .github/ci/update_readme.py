import requests


def fetch_bing_wallpaper():
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['images'][0]


def update_readme(image_info):
    title = image_info.get('title', '🔖今日必应壁纸')
    description = image_info.get('copyright', '')
    with open("README.md", "w") as file:
        file.write(f"# 🔖{title}\n\n")
        file.write(f"![Bing Wallpaper](https://www.bing.com{image_info['url']})\n\n")
        file.write(f"> 📝{description}\n")


def generate_commit_message(image_info):
    title = image_info.get('title', '🔖 今日必应壁纸')
    description = image_info.get('copyright', '')
    return f"📝 docs: update README [skip ci]\n\n🔖 {title}\n📝 {description}"



if __name__ == "__main__":
    image_info = fetch_bing_wallpaper()
    update_readme(image_info)
    commit_message = generate_commit_message(image_info)
    # 仅输出提交信息，避免其他内容干扰 commit_message.txt 的生成
    print(commit_message)
