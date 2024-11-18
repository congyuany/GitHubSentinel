class NotificationService:
    def __init__(self, config):
        self.config = config

    def send_notifications(self, report):
        # 发送通知
        print(f"Sending notification to {self.config.NOTIFICATION_EMAIL} with report: {report}")
