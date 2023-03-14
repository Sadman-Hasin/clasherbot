import os
from fbchat import Client
from fbchat.models import *
import re

#6750292848344715
#100047171536170
#5825488547563264


class HappyClasher(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if self.procced(message_object.text, author_id, thread_id):
            self.sendMessage(
                    self.response(message_object.text),
                    author_id,
                    thread_id,
                    thread_type
                )
            
    def procced(self, message, author_id, thread_id):
        if author_id != self.uid and (str(thread_id) == "6750292848344715" or str(thread_id) == "5825488547563264") and message:
            if message[0] == "~":
                return True

        return False

    def response(self, message):
        if message == "~":
            return "How can I help you?"

        else:
            cmd = message[2:]

            if cmd == "help":
                return "The Prefix is \"~\".\n\n1. \"help\" - reply this content.\n\nDidn't start working on cocapi. No other features are added yet."

            return "use \"~ help\" to show available commands."
            
    def sendMessage(self, response, author_id, thread_id, thread_type):
        mention = client.fetchUserInfo(author_id
)[author_id].name

        client.send(
                Message(
                    text=f"@{mention}\n{response}",
                    mentions=[Mention(author_id, offset=0, length=len(mention)+1)]
                ),
                thread_id=thread_id,
                thread_type=thread_type,
            )
        

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    client = HappyClasher(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    client.listen()
    return "<p>Started Running...</p>"




