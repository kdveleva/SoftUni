class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to " \
               f"{self.receiver}: {self.content}." \
               f" Sent: {self.is_sent}"


emails =[]
while True:
    command = input()
    if command == "Stop":
        break
    mails = command.split(" ")
    sender = mails[0]
    receiver = mails[1]
    content = mails[2]
    email = Email(sender, receiver, content)
    emails.append(email)

sent_emails = list(map(lambda x: int(x), input().split(', ')))

for x in sent_emails:
    emails[x].send()
for e in emails:
    print(e.get_info())

