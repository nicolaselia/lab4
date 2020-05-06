# Charles Kinzel
# Nick Elia
# David Monge
# Lab 4
# CSE 408
# Team AlphaOne


# Charles Code
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


# Done by Nick
def reverse_string(string):
	return string[::-1]


def is_prime(numb):
	if numb > 1:
	    for i in range(2, numb):
	        if (numb % i) == 0:
	            return False
	    else:
	        return True

string = input("Input a string")
print("The reversed string is", reverse_string(string))

numb = int(input("Input a number"))
if(is_prime(numb)):
	print("The number", numb, "is prime.")
else:
	print("The number", numb, "is not prime.")

# Done by David 

def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

nNum = 10
for i in range(nNum):
    print(fibo(i))