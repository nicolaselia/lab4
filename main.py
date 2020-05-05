#
# AlphaOne Lab4
#

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