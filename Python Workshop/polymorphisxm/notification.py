class Notification:
    def get_notification(self):
        pass

class Instagram(Notification):

    def get_notification(self):
        print("Notification from Instagram")

class Facebook(Notification):
    def get_notification(self):
        print("Notification from Facebook")

instagram=Instagram()
instagram.get_notification()

Facebook=Facebook()
Facebook.get_notification()
