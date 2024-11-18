import requests

def get_github_repo_info(repository_url):
    # 获取GitHub仓库信息
    response = requests.get(repository_url)
    return response.json()
