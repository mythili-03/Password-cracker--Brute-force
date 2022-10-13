import random
import pyautogui
characters = " 0123456789abcdefghijklmnopqrstuvwxyz "
character_list = list( characters )
password = pyautogui.password ( " Enter password : " )
guess_password = ' '
while ( guess_password != password ) :
    guess_password = random.choices ( character_list , k = len ( password ) )
    print ( " -----> " + str ( guess_password ) + " <----- " )
    if ( guess_password == list ( password ) ) :
        print ( " Your Password is : " + " " .join ( guess_password ) )
        break
