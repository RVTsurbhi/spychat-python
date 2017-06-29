from spydetails import spy, friends, Spy, ChatMessage
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

#written by surbhi rawat
#how to print in python in double quotes
print "hello!"

#single quotes can be well defined by using backslash
print 'let\'s get started'

#default statuses. these status lies outside the function and can be declare as global. here the list of older status
#has been stored in a list
STATUS_MESSAGE = ['we are on a mission! ', 'Spy is working on something ', 'Work in progress', 'mission accomplished.']


#creating friends list:

#friends = []



question = raw_input("Do you want to continue as " + " " + spy.salutation + " " + spy.name + "(Y/N)?")

#create function to have option to update status of the spy from the older status
def add_status():

    updated_status_message = None
    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print "you don't have have status message currently \n"

    #to ask user if he/she wants to update new status or to select from the older one
    default = raw_input("do you want to select from the older status (Y/N)?")

    if default.upper() == "N":
        new_status_message = raw_input("want to set new status?")

        if len(new_status_message) > 0:
             STATUS_MESSAGE.append(new_status_message)
             updated_status_message = new_status_message

    elif default.upper()== "Y":

        item_position = 1

        for message in STATUS_MESSAGE:
            print '%d, %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\n choose from above messages"))

       #to check if user has entered the correct(index) no. which is in within the range. and subracting -1 because index starts from 0.
        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection - 1]

    else:
        print "unvalid option! press Y or N"

    if updated_status_message:
         print "your updated status message is: %s" % (updated_status_message)

    else:
         print "you did not update your status message"

    return updated_status_message

# create a function to add spy's new friend
def add_friend():

    new_friend = Spy( '',0,'',0.0)

    new_friend.name = raw_input("add your friends name:")
    new_friend.salutation = raw_input("are they Mr. or Ms.:?")

    new_friend.name = new_friend.name + " " + new_friend.salutation

    new_friend.age = int(raw_input("age?"))
    new_friend.rating = float(raw_input("spy rating?"))

    #to create a function to check the spy's friend's age, rating and to check that the name should not be empty

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'sorry! invalid entry. we can\'t add spy with the details you provided'

    return len(friends)

# to select which friend of spy's friend-list is being choosen by the user
def select_a_friend():
    item_number = 0

    for friend in friends:
       print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                            friend.age, friend.rating)

       item_number = item_number + 1

    friend_choice =  raw_input("choose from your friends")
    #-1 because the index starts from 0
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

#select that friend whom you want to send the secret message in encoded form
def send_message():

    friend_choice = select_a_friend()

    #original_image is that image in which we write our text, output_path indicates our that encoded img with the
    # secret message in it. and the text is our secret message. encode the secret message using encode()function
    original_image = raw_input("what is the name of your image?")
    output_path ="output.jpg"
    text = raw_input("write your text here")
    Steganography.encode(original_image, output_path, text)

    #to save the secret message
    new_chat = ChatMessage(text, True)


    friends[friend_choice].chats.append(new_chat)

    print "your secret message image is ready!"


#to decode the secret message
def read_message():
    sender = select_a_friend()

    output_path =raw_input("name of the file")
    secret_text = Steganography.decode(output_path)

    #to save the secret message in the decoded form
    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "your secret message has been saved!"



#function to read chat history of a friend by selecting one of the friend
def read_chat_history():
    read_for = select_a_friend()

    #print 'you have no previous chats'
    if len(friends[read_for].chats) > 0:

        for chat in friends[read_for].chats:
            #if chat is sent by spy
            if chat.sent_by_me:
                print '[%s] %s: %s' % (chat.time.strftime(colored("%d %B %D", 'blue')),
                                       colored('you said:', 'red'), chat.message)
             #if chat is not sent by spy
            elif not chat.sent_by_me:
                 print'[%s] %s said: %s' % (chat.time.strftime(colored("%d %B %Y", 'blue')),
                                            friends[read_for].name, chat.message)

     #otherwise print there are no old chats
    else:
        print colored('there is no previous chats', 'red')


#update spy-status

def start_chat(spy):


  spy.name = spy.salutation + " " + spy.name

  #to know about the spy age if it lies between 12 and 50
  if spy.age >12 and spy.age < 50:

      print "authentication complete. welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + \
            str(spy.rating) + "proud to have you on board"

       #to check the spy's rating
      if spy.rating > 4.5:
          print 'awesome!'
      elif spy.rating > 3.5 and spy.rating <= 4.5:
          print 'You are smart enough.'
      elif spy.rating >= 2.5 and spy.rating <= 3.5:
          print 'You can do better'
      else:
          print 'We have other options too.'

      #to set all the options available for the application
      show_menu = True

      while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update  \n 2. Add a friend \n 3. send a secret message \n 4. read a secret message \n 5. Read chats from the user\n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                #set status
                if menu_choice == 1:
                   spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'you have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False

  else:
      print "sorry you are not of the correct age to be a spy"


if question == "Y":
     start_chat(spy)
else:

    spy = Spy('',0,'',0.0)

    #to-know-more about spy
    #if len(spy['name']) > 0:

    #string cncatenation
    # print 'welcome' + spy_name + '. glad to have you back with us.'
    spy.name = raw_input("welcome to spychat. tell me your name:")

    if len(spy.name) > 0:

        spy.salutation = raw_input("what should we call you(Mr. or Ms.)?")

        spy.age = int(raw_input("what is your age:"))
        spy.rating = float(raw_input("what is your spy rating?"))

        start_chat(spy)

    else:
        print "a spy needs to have a valid name. please try again"

