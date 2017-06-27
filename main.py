from spydetails import spy, friends
from datetime import datetime
from steganography.steganography import Steganography

#written by surbhi rawat
#how to print in python
print 'hello!'

#to print in double quotes
#print"hello world"

#single quotes can be well defined by using backslash

#default statuses. these status lies outside the function and can be declare as global. here the list of older status
#has been stored in a list
STATUS_MESSAGE = ['Hey there! ', 'Spy is working on something ', 'Work in progress.']


#creating friends list:

#friends = []

print 'let\'s get started'

question = raw_input("Do you want to continue as " + " " + spy['salutation'] + " " + spy['name'] + "(Y/N)?")

#create function to have option to update status of the spy from the older status
def add_status(current_status_message):
    updated_status_message = None
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print "you don't have have status message currently"

     #to ask user if he/she wants to update new status or to select from the older one
    default = raw_input("do you want to select from the older status (Y/N)?")

    if default.upper() == "N":
        new_status_message = raw_input("want to update new status?")

        if len(new_status_message) > 0:
                STATUS_MESSAGE.append(new_status_message)
                updated_status_message = new_status_message

    elif default.upper()== "Y":

        item_position = 1

        for message in STATUS_MESSAGE:
            print '%d, %s' % (item_position, message)
            item_position =  item_position + 1


        message_selection = int(raw_input("\n choose from above messages"))
       #to check if user has entered the correct(index) no. which is in within the range. and subracting -1 because index starts from 0.
        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection-1]

    else:
        print "unvalid option! press Y or N"

    if current_status_message:
         print "your updated status message is: %s" % (current_status_message)

    else:
         print "you did not update your status message"

    return updated_status_message

# to know the details of spy friend

def add_friend():

    new_friend ={
        'name': '',
        'salutation' : '',
        'age': 0,
        'rating': 0.0,
        'chats': []
    }
    new_friend['name'] = raw_input("add your friends name:")
    new_friend['salutation'] = raw_input("are they Mr. or Ms.?:")

    new_friend['name'] = new_friend['name'] + " " + new_friend['salutation']

    new_friend['age'] = int(raw_input("age?"))
    new_friend['rating'] = float(raw_input("spy rating?"))

    #to create a function to check the spy friend's age, rating and to check that the name should not be empty

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'sorry! invalid entry. we can\'t add spy with the details you provided'

        return len(friends)

# to select which friend of spy's friend-list is being choosen by the user
def select_friend():
    item_number = 0

    for friend in friends:
       print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['name'],
                                                            friend['age'], friend['rating'])

       item_number = item_number + 1

    friend_choice =  raw_input("choose from your friends")
    #-1 because the index starts from 0
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

#select that friend whom you want to send the secret message in encoded form
def send_message():

    friend_choice = select_friend()

    #original_image is that image in which we write our text, output_path indicates our that encoded img with the
    # secret message in it. and the text is our secret message. encode the secret message using encode()function
    original_image = raw_input("what is the name of your image?")
    output_path ="output.jpg"
    text = raw_input("write your text here")
    Steganography.encode(original_image, output_path, text)

    #to save the secret message
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me" : True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print "your secret message image is ready!"


#to decode the secret message
def read_message():
    sender = select_friend()

    output_path =raw_input("name of the file")
    secret_text = Steganography.decode(output_path)

    #to save the secret message in the decoded form
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)

    print "your secret message has been saved!"

#update spy-status and initialize current status value to none

def start_chat(spy):
  current_status_message = None

  spy['name'] = spy['salutation'] + " " + spy['name']

  #to know about the spy age
  if spy['age'] >12 and spy['age'] < 50:

      print "authentication complete. welcome" + spy['name'] + "age:" + str(spy['age']) + "and rating of:" + \
            str(spy['rating']) + "proud to have you on board"

      #to set all the options available for the application
      show_menu = True

      while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update  \n 2. Add a friend \n 3. send a secret message \n 4. read a secret message \n 5. Read chats from the user\n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                #set status
                if menu_choice == 1:
                   current_status_message = add_status(current_status_message)

                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print "you have %d friends" % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()

                else:
                    show_menu = False

  else:
      print "sorry you are not of the correct age to be a spy"


if question == "Y":
     start_chat(spy['name'],spy['rating'],spy['age'])
else:

    spy = {
        'name' : '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }



    #to-know-more about spy
    #if len(spy['name']) > 0:

        #string cncatenation
        #print 'welcome' + spy_name + '. glad to have you back with us.'
    spy['name'] = raw_input("welcome to spychat. tell me your name:")

    spy['salutation'] = raw_input("what should we call you(Mr. or Ms.)?")

        #print "alright" + " " + spy_name + ". i'd like to know a little more about you."

    spy['age'] = int(raw_input("what is your age:"))
    spy['rating'] = float(raw_input("what is your spy rating?"))

    spy['is_online'] = True

    start_chat(spy)

    #else:
       #print "a spy needs to have a valid name. try again please"

