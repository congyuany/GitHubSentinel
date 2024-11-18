import requests
from models.repository import Repository

class GitHubService:
    def __init__(self, config):
        self.config = config

    def fetch_updates(self):
        # 从GitHub获取更新
        response = requests.get(f"https://api.github.com/repos/{self.config.GITHUB_API_KEY}")
        data = response.json()
        repository = Repository(data['name'], data['owner'], data['last_updated'])
        return repository
