class SubscriptionController:
    def __init__(self, github_service):
        self.github_service = github_service

    def add_subscription(self, repository_url, update_frequency):
        # 添加订阅
        subscription = Subscription(repository_url, update_frequency)
        # 存储订阅信息
        return subscription
