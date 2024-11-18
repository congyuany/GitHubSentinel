import unittest
from controllers.subscription_controller import SubscriptionController

class TestSubscriptionController(unittest.TestCase):
    def test_add_subscription(self):
        controller = SubscriptionController(None)
        subscription = controller.add_subscription("https://github.com/user/repo", "daily")
        self.assertIsNotNone(subscription)

if __name__ == "__main__":
    unittest.main()
