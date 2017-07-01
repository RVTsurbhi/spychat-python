from datetime import datetime
#to make the class of spy details
class Spy :

     def __init__(self, name, age, salutation, rating):
         self.name = name
         self.age = age
         self.salutation = salutation
         self.rating = rating
         self.is_online = True
         self.chats = []
         self.current_status_message = None

#to make tha class of chats
class ChatMessage:

    def __init__(self,message, sent_by_me):
        self.message = message
        self.sent_by_me = sent_by_me
        self.time = datetime.now()

spy = Spy('bond', 22, 'Mr.',5.5)

#information about spy's friends
friend_one = Spy('nihar', 22, 'Dr.', 6.02)
friend_two = Spy('kiara', 21, 'Ms', 6.12)
friend_three = Spy('Arnav', 24, 'Mr.', 7)

friends = [friend_one, friend_two,friend_three]



