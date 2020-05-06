# Charles Kinzel
# Lab 4
# CSE 408
# Team AlphaOne


def m_time():
    
     time = input('Enter your time: ')
     y = input('am or pm: ')
    
     word = time.split(":")
     hour = int(word[0]);
     if (y == 'pm'):
         hour = hour + 12

     print("Military time: " + str(hour) + ":" + word[1])

m_time()

def password():
     count = 0
     pw = input('Enter your password: ')
     # 33 - 63
     for element in range(0, len(pw)): 
        if (ord(pw[element]) > 32 and ord(pw[element]) < 64):
            count = count + 1
     if (len(pw) < 7):
         print("No good bro")
     elif (count < 2):
         print("No good bro")
     else:
         print("password is good")
         
password()

