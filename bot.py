import os
from fbchat import Client
from fbchat.models import *
import re

#6750292848344715
#100047171536170
#5825488547563264


class HappyClasher(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if author_id != self.uid and str(thread_id) == "5825488547563264" and message_object.text:
            if message_object.text[0] == "~":
                reply = self.reply(message_object.text)
                mention = client.fetchUserInfo(author_id)[author_id].name

                client.send(
                    Message(
                        text=self.reply(f"@@{mention}\n{reply}"),
                        mentions=[Mention(author_id, offset=0, length=len(mention)+1)]),
                    thread_id=thread_id,
                    thread_type=thread_type,
                )

    def reply(self, cmd):
        if cmd == "~":
            return "How can I help you?"

        command = cmd[1:]

        return "grrr, 'am sleeping, don't disturb!"
        


client = HappyClasher(os.getenv("EMAIL"), os.getenv("PASSWORD"))

client.listen()



