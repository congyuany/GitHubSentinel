from config import Config
from services.github_service import GitHubService
from services.notification_service import NotificationService
from services.report_service import ReportService

def main():
    config = Config()
    github_service = GitHubService(config)
    notification_service = NotificationService(config)
    report_service = ReportService(config)

    # 定期获取更新并生成报告
    github_service.fetch_updates()
    report = report_service.generate_report()
    notification_service.send_notifications(report)

if __name__ == "__main__":
    main()
