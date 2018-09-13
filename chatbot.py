from fbchat import Client, log
from fbchat.models import *


r = 1


class chandbot(Client):
    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        self.markAsRead(author_id)
        log.info("message {} from {} in {}".format(message_object, thread_id, thread_type))
        msgText = message_object.text
        reply = 'hello'
        reply1 = "chandan jha is currently buisy he will be available in minute"
        global r
        if author_id!=self.uid:
            if(r==1): 
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
                r = 2 
            else:
                self.send(Message(text=reply1), thread_id=thread_id, thread_type=thread_type)




        self.markAsDelivered(author_id, thread_id)
        

client = chandbot("jhachandan888293@gmail.com", "*#*#1998#*#*")
client.listen()
