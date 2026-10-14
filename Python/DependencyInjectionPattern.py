from typing import Protocol

# Define the EmailSender interface - describes the expected behaviour
class EmailSender(Protocol):
    def send(self, recipient: str, message: str) -> None: ...

# Create different email sender implementations
class ConsoleEmailSender:
    def send(self, recipient: str, message: str) -> None:
        print(f"Console: Email to {recipient}: {message}")


class FakeEmailSender:
    def __init__(self):
        self.sent = []      # Array to store the emails sent

    def send(self, recipient, message):
        self.sent.append((recipient, message))
        

# Define the WelcomeService that uses the provided EmailSender
class WelcomeService:
    def __init__(self, email_sender: EmailSender):
        self.email_sender = email_sender

    def welcome(self, email:str) -> None:
        self.email_sender.send(
            email, "Welcome to our service!"
        )


# Inject the implementation when constructing the service
sender = ConsoleEmailSender()
service = WelcomeService(sender)
service.welcome("test@email.com")


fake = FakeEmailSender()
service = WelcomeService(fake)
service.welcome("faketest@example.com")

print (f"Fake emails sent: {len(fake.sent)}")
print (f"Fake email sent to: {fake.sent[0][0]}")