from datetime import datetime
default_password='python'

class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status_message=None


class chatmessage:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.datetime=datetime.now()
        self.sent_by_me=sent_by_me

spy = Spy('sunjeet', 'Mr.', 20, 4.7)

friend_one = Spy('shubham', 'Mr.', 19, 4.8)
friend_two = Spy('akash', 'Mr.', 20, 4.5)
friend_three = Spy('kajal', 'Miss.', 21, 4.6)

friends = [friend_one, friend_two, friend_three]



