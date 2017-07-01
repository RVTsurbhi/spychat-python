#import different libraries to main file
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


question = raw_input("Do you want to continue as " + " " + spy.salutation + " " + spy.name + "(Y/N)?")

#create function to have option to update status of the spy from the older status
def add_status():

    updated_status_message = None
    if spy.current_status_message != None:
        print 'Your current status message is %s\n' % (spy.current_status_message)
    else:
        print colored("you don't have have status message currently \n",'blue')

    #to ask user if he/she wants to update new status or to select from the older one
    default = raw_input("do you want to select from the older status (Y/N)?")

     #if user say no to older status, then ask for updating the new status
    if default.upper() == "N":
        new_status_message = raw_input("want to set new status?")
         #to check the new status message should not set empty
        if len(new_status_message) > 0:
             STATUS_MESSAGE.append(new_status_message)
             updated_status_message = new_status_message

     #if user say yes to older statuses,then show all the older status
    elif default.upper()== "Y":

        item_position = 1

        for message in STATUS_MESSAGE:
            print '%d, %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\n choose from above messages"))

       #to check if user has entered the correct(index) no. which is in within the range. and subracting -1 because index starts from 0.
        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection - 1]

     #to check if user has other option rather then yes or no
    else:
        print colored ("unvalid option! press Y or N",'red')

     #if user wants to update his/her new status
    if updated_status_message:
         print colored("your updated status message is: %s" % (updated_status_message),'blue')

     #to show user that status is not updated
    else:
         print colored("you did not update your status message",'red')

    return updated_status_message

# create a function to add spy's new friend
def add_friend():
     #creating empty values for new friend
    new_friend = Spy( '',0,'',0.0)
    #to evaluate all details of spy's new friend like name, age, rating and salutation
    new_friend.name = raw_input("add your friends name:")
    new_friend.salutation = raw_input("are they Mr. or Ms.:?")

    new_friend.name = new_friend.name + " " + new_friend.salutation

    new_friend.age = int(raw_input("age?"))
    new_friend.rating = float(raw_input("spy rating?"))

    #to check the spy's friend's age, rating and the name that should not be empty

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print colored ('Friend Added!','red')
    else:
        print colored('sorry! invalid entry. we can\'t add spy with the details you provided','blue')

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

    #adding the chat in chats list from selected friend
    friends[friend_choice].chats.append(new_chat)

    print colored ("your secret message image is ready!",'red')


#to decode the secret message
def read_message():
    sender = select_a_friend()

    output_path =raw_input("name of the file")
    secret_text = Steganography.decode(output_path)

    #to save the secret message in the decoded form
    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print colored("your secret message has been saved!",'blue')


#function to read chat history of a friend by selecting one of the friend
def read_chat_history():
    read_for = select_a_friend()

    #print 'you have no previous chats'
    if len(friends[read_for].chats) > 0:

        for chat in friends[read_for].chats:
            #if chat is sent by spy
            if chat.sent_by_me:
                print "[%s] %s: %s" % (chat.time.strftime(colored("%d %B %D", 'blue')),
                                       colored('you said:', 'red'), chat.message)
             #if chat is not sent by spy
            elif not chat.sent_by_me:
                 print "[%s] %s said: %s" % (chat.time.strftime(colored("%d %B %Y", 'blue')),
                                            friends[read_for].name, chat.message)

     #otherwise print there are no old chats
    else:
        print colored('there is no previous chats', 'red')

#declare function to start chat
def start_chat(spy):


  spy.name = spy.salutation + " " + spy.name

  #to know about the spy age if it lies between 12 and 50
  if spy.age >12 and spy.age < 50:

      print "authentication complete. welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + \
            str(spy.rating) + "proud to have you on board"

       #to check the spy's rating through different categories
      if spy.rating > 4.5:
          print colored ('awesome!','red')
      elif spy.rating > 3.5 and spy.rating <= 4.5:
          print colored ('You are smart enough.','blue')
      elif spy.rating >= 2.5 and spy.rating <= 3.5:
          print colored('You can do better','red')
      else:
          print colored('We have other options too.','blue')

      #to set all the options available for the application
      show_menu = True

      while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update  \n 2. Add a friend \n 3. send a secret message \n 4. read a secret message \n 5. Read chats from the user\n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                #set status through calling add_status function if selected option is 1
                if menu_choice == 1:
                   spy.current_status_message = add_status()

                 #if user selects option 2 call the add_function
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'you have %d friends' % (number_of_friends)

                  #if the user selects option 3, then call the  send_message function
                elif menu_choice == 3:
                    send_message()

                 #if user selects option 4, then call the read_message function
                elif menu_choice == 4:
                    read_message()

                 #if user selects option 5, then call the chat_history function
                elif menu_choice == 5:
                    read_chat_history()
                 #if user selects option 6, then close the application
                else:
                    show_menu = False

  else:
      print colored("sorry you are not of the correct age to be a spy",'red')


if question == "Y":
     start_chat(spy)
else:
     #declaring empty values for spy
    spy = Spy('',0,'',0.0)

    #to know about the spy while asking all the details like name, salutation, age and rating
    spy.name = raw_input("welcome to spychat. tell me your name:")
     #to check if spy name is not empty
    if len(spy.name) > 0:

        spy.salutation = raw_input("what should we call you(Mr. or Ms.)?")

        spy.age = int(raw_input("what is your age:"))
        spy.rating = float(raw_input("what is your spy rating?"))

        start_chat(spy)

    else:
        print colored("a spy needs to have a valid name. please try again",'blue')

