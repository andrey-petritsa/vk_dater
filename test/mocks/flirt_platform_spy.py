class FlirtPlatformSpy:
    def send_message(self, message):
        self.last_sended_message = message