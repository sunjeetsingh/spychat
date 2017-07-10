#PASSWORD FOR DEFAULT USER=python
#ENCODING IMAGE=hello.jpg
#DECODING IMAGE=output.jpg
from steganography.steganography import Steganography                       #importing stenanography module
from spy_details import spy,Spy,chatmessage,friends,default_password        #importing different classes
from termcolor import colored                                               #Importing termcolor module

friend_choice=0

#GREETING TEXT

print'WELCOME TO SPYCHAT'
print'\t1.CONTINUE AS SUNJEET\n\t2.NEW USER'
with open("status.txt","r+") as STATUS_MESSAGES:
    STATUS_MESSAGES = STATUS_MESSAGES.read().splitlines()

def status_file(text):
    file = open("status.txt", "a")
    file.write("HELLO")
    file.write("\n")
    file.write("I\'m Back")
    file.write("\n")
    file.write("What\'s Upp")
    file.write("\n")
    file.write("DAY DREAMER")
    file.write("\n")
    file.write("NIGHT THINKER")
    file.write('\n')
    file.write(text)
    file.close()


#DEFINING  A FUNCTION FOR SELECTION OF FRIEND

def select_friend():
    while True:
        item_number = 1
        for friend in friends:
            print '\t%d.) %s aged %d with rating %.2f is online.' % (item_number, friend.name, friend.age, friend.rating)
            item_number = item_number + 1
        try:
            friend_choice = int(raw_input('\nChoose from your friends:'))
            friend_choice_position = friend_choice - 1
            return friend_choice_position
        except:
            print 'Please input correct value\n'
            continue


def start_chat(spy):
    a=0
    show_menu=True
    current_status_message=None

    #OPTIONS FOR DIFFERENT MENU CHOICE

    while(show_menu):
        menu_choices = "CHOOSE:\n\t 1.ADD A STATUS UPDATE\n\t 2.ADD A FRIEND\n\t 3.SEND A MESSAGE\n\t 4.READ A MESSAGE\n\t 5.CHAT HISTORY\n\t 6.DELETE A FRIEND\n\t 7.EXIT THE APPLICATION"
        print menu_choices
        try:
            menu_choice=raw_input('Enter the choice:')
            menu_choice=int(menu_choice)
        except ValueError:
            print"INVALID INPUT.PLEASE CHOOSE AGAIN"
        if menu_choice>7:
            print 'INVALID INPUT'


        #STATUS UPDATION

        if menu_choice == 1:
            print 'YOU CHOOSE TO UPDATE THE STATUS'

            def add_status(current_status_message):

                if current_status_message != None:
                    print'Your current status is' + " " + current_status_message
                else:
                    print'YOU DON\'T HAVE ANY CURRENT STATUS MESSAGE'
                    print 'Do you want to choose from older status message \n\t a.YES\n\t b.NO'
                while True:
                    default = raw_input('Enter your choice:')

                    # INSERTING A NEW STATUS
                    if default == "NO" or default == "b":

                        new_status_message = raw_input('PLEASE INPUT YOUR STATUS MESSAGE:')

                        if len(new_status_message) > 0:  # CHECKING LENGTH OF INSERTED STATUS

                            updated_status_messsage = new_status_message
                            STATUS_MESSAGES.append(updated_status_messsage)
                            print'UPDATING............'
                            print 'YOUR STATUS HAS BEEN UPDATED,YOUR CURRENT STATUS IS:', updated_status_messsage
                            print 'LIST OF STATUS MESSAGES:'

                            item_position = 1
                            for statuses in STATUS_MESSAGES:
                                print str(item_position) + "." + statuses
                                item_position = item_position + 1
                                # return updated_status_messsage


                        else:
                            print'Please enter a valid status message'  # ERROR HANDLING FOR EMPTY STATUS

                            # CHOOSING STATUS FROM OLDER STATUS MESSAGE

                    elif default == "YES" or default == "a":
                        while True:
                            print 'OLDER STATUS MESSAGE ARE:'
                            item_position = 1
                            for statuses in STATUS_MESSAGES:
                                print str(item_position) + "." + statuses
                                item_position = item_position + 1

                            while True:
                                try:
                                    message = int(raw_input('Choose from above messages:'))
                                    message_selection = message
                                except ValueError:
                                    print "Numbers only"
                                    continue
                                break
                            if len(STATUS_MESSAGES) >= message_selection:
                                updated_status_messsage = STATUS_MESSAGES[message_selection - 1]
                                print'UPDATING......'
                                print'\tYOUR STATUS HAS BEEN UPDATED SUCCESSFULLY AND YOUR CURRENT STATUS IS:' + " " + updated_status_messsage
                                break

                            else:
                                print 'PLEASE SELECT A VALID NUMBER'


                    else:
                        print'INVALID INPUT.PLEASE ENTER a OR b'
                    break


            current_status_message = add_status(current_status_message)


            #ADDING A FRIEND

        elif menu_choice == 2:
            print 'You choose to ADD A FRIEND'

            def add_friend():

                new_friend = Spy('', '', 0, 0.0)
                new_friend.name = raw_input('\tYOUR FRIEND NAME:')           #FRIEND NAME
                new_friend.salutation = raw_input("\tMR./MRS./MISS:")        #SALUTATION FOR FRIEND
                while True:
                    try:
                        new_friend.age = int(raw_input("\tAGE:"))                  #FRIEND AGE
                    except ValueError:
                        print'INVALID AGE'
                        continue
                    break
                print'SPY-RATING:'
                print'\t>> BETWEEN 1-1.9: We can always use somebody to help in the office '
                print'\t>> BETWEEN 2-2.9: BEGINNER'
                print'\t>> BETWEEN 3-4.4: INTERMEDIATE'
                print'\t>> BETWEEN 4.5-5: EXPERT'

                while True:
                    try:
                        new_friend.rating = float(raw_input("\tSpy Rating(Out of 5):"))       #RATING OF FRIEND
                    except ValueError:
                        print'INVALID RATING'
                        continue
                    break

                if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating <5:
                    friends.append(new_friend)                                                 #ADDING FRIEND
                    return len(friends)
                else:
                    print'Sorry! Invalid Entry. Please try again.'
                return add_friend()

            add_friend()                                                        #add-friend function call

            print'LOADING......'
            print'CONGRATS! YOU FRIEND IS SUCESSFULLY ADDED'
            print 'KEEP ADDING YOUR FRIENDS'

            #PRINT ALL THE FRIENDS
            item_number=1
            for friend in friends:
                print '%d. %s aged %d with rating %.2f is online.' %(item_number, friend.name, friend.age, friend.rating)
                item_number=item_number+1

                #SENDING A MESSAGE TO FRIEND

        elif menu_choice == 3:
            print 'You choose to SEND A MESSAGE\n'

            def send_message():
                while True:
                    friend_choice=select_friend()
                    try:                                             #ERROR HANDLING FOR WRONG INPUT
                        friends[friend_choice]
                    except ValueError:
                        print'\nInvalid number'
                        print'Please choose again '
                        continue
                    except:
                        print'Please choose a valid friend\n'
                        continue
                    break
                while True:
                    try:
                        original_image=raw_input('\tNAME OF IMAGE:')              #NAME OF IMAGE TO BE SENDED
                        output_path='output.jpg'
                        text=raw_input('\tENTER THE TEXT:')                       #TEXT TO BE HIDDEN INSIDE IMAGE
                        print'LOADING.....\n'
                        print'\tYOUR MESSAGE IS BEING READY\n'
                        Steganography.encode(original_image,output_path,text)      #ENCODING OF IMAGE
                    except IOError:                                              #ERROE HANDLING FOR INVALID FILE
                        print'NO SUCH IMAGE OR FILE EXIST.PLEASE TRY AGAIN'
                        continue
                    break

                new_chat = chatmessage(text, True)
                friends[friend_choice].chats.append(new_chat)                   #APPEND CHATS

            send_message()

            #READING A MESSAGE

        elif menu_choice == 4:
            print 'You choose to read a message\n'

            def read_message():
                special_messages=['SAVEME','HELP','SOS','FIRE','AMBULANCE','saveme','help','fire','sos','ambulance']   #SPECIAL MESSAGES FOR EMERGENCY
                while True:
                    sender=select_friend()
                    try:                                                    #ERROR HANDLE FOR WRONG INPUT
                        friends[sender]
                    except ValueError:
                        print'\nInvalid number'
                        print'Please choose again '
                        continue
                    except:
                        print'Please choose a valid friend'
                        continue
                    break
                while True:
                    try:
                        output_path=raw_input("\tFILE NAME:")                     #NAME OF OUTPUT IMAGE
                        secret_text=Steganography.decode(output_path)             #DECODING OF IMAGE
                    except IOError:                                             #ERROR HANDLING FOR INVALID IMAGE FILE
                        print'NO SUCH FILE EXIST'
                        continue
                    break

                new_chat = chatmessage(secret_text, False)
                friends[sender].chats.append(new_chat)                         #APPENDING CHATS
                print"DECRYPTING....."

                if len(secret_text)==0:                                        #ERROR HANDLING FOR EMPTY MESSAGE
                    print"SORRY!! THIS IMAGE DOESN\'T CONTAIN ANY MESSAGE"
                elif secret_text in special_messages:                          #SPECIAL MESSAGES IN ENCRYPTING IMAGE
                    print'\n\tMESSAGE FOUND:'+secret_text
                    print'\tPLEASE CALL ON THIS NUMBER:+918976543210\n'
                else:
                    print"\n\tYour secret message is ready"
                    print '\tMESSAGE IS:%s\n' %(secret_text)
            read_message()

            #READ CHAT HISTORY OF FRIEND

        elif menu_choice == 5:
            print 'YOU choose to read chat history\n'

            def read_chat_history():
                while True:
                    read_for= select_friend()
                    try:                    #ERROR HANDLE FOR WRONG INPUT
                        friends[read_for]
                    except ValueError:
                        print'\nInvalid number'
                        print'Please choose again '
                        continue
                    except:
                        print'Please choose a valid friend\n'
                        continue
                    break
                text = 'You said:'

                #COLOR IMPLEMENTATION ON DATETIME,FRIEND NAME AND CHATS
                for chat in friends[read_for].chats:
                    if chat.sent_by_me==True:
                        print colored ('[%s] '%chat.datetime,'blue'),
                        print colored ('%s'%text,'red'),
                        print colored (' %s'%chat.message,'green')
                    else:
                        print colored('[%s]'%chat.datetime,'blue'),
                        print colored('%s said:'%friends[read_for].name,'red'),
                        print colored('%s'%chat.message,'green')

            read_chat_history()

            #DELETING A FRIEND

        elif menu_choice==6:
            print 'YOU CHOOSE TO DELETE A FRIEND'

            def delete_friend():
                while True:
                    select= select_friend()
                    try:                         #ERROR HANDLE FOR WRONG INPUT
                        friends[select]
                    except ValueError:
                        print'\nInvalid number'
                        print'Please choose again '
                        continue
                    except:
                        print'Please choose a valid friend\n'
                        continue
                    break
                if len(friends[select].chats)==0:
                    print 'FRIEND CANT BE DELETED.PLEASE CHAT FIRST'
                else:
                    for temp in friends[select].chats:
                        if len(temp.message)>100:
                            del friends[select]
                            item_number = 0
                            print 'YOU HAVE DELETED YOUR FRIEND:%s' % friends[i].name
                            for friend in friends:
                                print '%d. %s aged %d with rating %.2f is online.' % (item_number + 1, friend.name, friend.age, friend.rating)
                                item_number = item_number + 1
                        else:
                            print'Sorry! Friend spoke less than 100 words'
                            break

            delete_friend()

            #EXIT THE APPLICATION

        elif menu_choice==7:
            print'\tGOOD DAY!!!'
            show_menu = False
            #else:
            #print'INVALID INPUT'


    s = open("status.txt","w")
    for statuses in STATUS_MESSAGES:
        s.write(statuses+'\n')
    exit()

#LOGIN FOR DEFAULT USER
j=True
while(j):
    while True:
        try:
            #
            logi = int(raw_input('Enter your choice:'))
            login = logi
        except ValueError:
            print "ONLY NUMBERS 1 & 2"
            continue
        break
    if login!=1 and login!=2:
        print'Invalid Entry'
    elif login==1:
        i = True
        while (i):
            password = raw_input('PLEASE ENTER YOUR PASSWORD:')

            # CHECK FOR PASSWORD OF DEFAULT USER
            # i = True
            # while (i):
            if password != default_password:
                print'\tPASSWORD INCORRECT'
                # password = raw_input('PASSWORD INCORRECT!! PLEASE ENTER THE CORRECT PASSWORD:')
            else:
                print 'Loading.....'
                print 'PASSWORD MATCHED'
                print'Hey! SUNJEET,Nice to see you again'

                # STATUS FOR DEFAULT USER
                spy_is_online = True
                while (spy_is_online):
                    status = raw_input('Your status(ONLINE/OFFLINE):')
                    if status != "ONLINE" and status != "OFFLINE":
                        print'Please enter a valid status'
                    elif status == "OFFLINE" or status == "offline":
                        print'YOU ARE OFFLINE NOW'
                        spy_is_online = False
                    elif status == "ONLINE" or status == "online":
                        print 'YOU ARE ONLINE NOW'
                        spy_is_online = False
                i = False


        start_chat(spy)

    #SIGN UP FOR NEW USER....
    elif login==2:

        while True:
            print'PLEASE SIGN UP'
            spy_name = raw_input('\tUSERNAME:')
            if len(spy_name) > 0:
                spy_salutation = raw_input('\tMR/MRS/MISS:')
                while True:
                    try:
                        spy_age = raw_input('\tAGE:')
                        spy_age = int(spy_age)
                    except ValueError:
                        print 'PLEASE ENTER VALID AGE'
                        continue
                    break
                if spy_age > 12 and spy_age < 50:
                    print'SPY-RATING:'
                    print'\t>> BETWEEN 1-1.9: We can always use somebody to help in the office '
                    print'\t>> BETWEEN 2-2.9: BEGINNER'
                    print'\t>> BETWEEN 3-4.4: INTERMEDIATE'
                    print'\t>> BETWEEN 4.5-5: EXPERT'
                    while True:
                        try:
                            spy_rating = float(raw_input('\nEnter your Spy Rating(Out of 5):'))
                            if spy_rating >= 4.5 and spy_rating <= 5:
                                print'\tEXPERT'
                            elif spy_rating >= 3 and spy_rating < 4.5:
                                print'\tINTERMEDIATE'
                            elif spy_rating >= 2 and spy_rating < 3:
                                print'\tBEGINNER'
                            else:
                                print '\tWe can always use somebody to help in the office'
                        except ValueError:
                            print 'Numbers only'
                            continue
                            user_password = raw_input('\tCREATE YOUR PASSWORD:')
                            print 'Creating your account....'
                            print '\tBOOM......Your account has been successfully created.'
                            print  '\t' + spy_salutation + " " + spy_name + '!!' + " " + 'WELCOME TO THE WORLD OF SPYCHAT'
                            print 'Your username is' + " " + spy_name + " " + 'and password is' + " " + user_password
                        break

                        # else:
                        #   print'NOT ELIGIBLE'
                        # continue

                        # USER STATUS(ONLINE/OFFLINE)
                        spy_is_online = True
                        while (spy_is_online):
                            status = raw_input('Your status(ONLINE/OFFLINE):')
                            if status != "ONLINE" and status != "OFFLINE":
                                print'Please enter a valid status'
                            elif status == "OFFLINE":
                                print'YOU ARE OFFLINE NOW'
                                spy_is_online = False
                            elif status == "ONLINE":
                                print 'YOU ARE ONLINE NOW'
                                spy_is_online = False
                    start_chat(spy)


                else:
                    print'Sorry, You are not eligible for SPYCHAT'
                continue
            else:
                print 'ENTER YOUR USERNAME FIRST'

j=False
