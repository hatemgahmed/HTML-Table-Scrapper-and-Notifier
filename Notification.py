from pushbullet import Pushbullet
import json

class Notification:
    def __init__(self):
        with open("pushbullet_parameters.json",'r') as file:
            #Load parameters:
            # print(type(file))
            parameters=json.loads(file.read())
            self.pb = Pushbullet(parameters['pushbullet'])
            self.dev = self.pb.get_device(parameters['device'])
    def notify(self,title,text):
        push = self.dev.push_note(title, text)
        return push




