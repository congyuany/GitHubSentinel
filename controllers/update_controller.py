class UpdateController:
    def __init__(self, github_service):
        self.github_service = github_service

    def fetch_updates(self):
        # 获取更新
        return self.github_service.fetch_updates()
