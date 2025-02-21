import random 
import string 

print('****welcome to the password generador****')
length =int(input('enter the total numbers to length password: '))

letter = int(input('enter number of letter in password: '))
number= int(input('enter the number of numbers in password: '))
pun = int(input('enter the number of sympols in password'))

if length != (letter + number + pun):
	print('\ninvalid input, the sum dosnt match with length of password')
else:
	let = string.ascii_letters
	num = string.digits
	sym = string.punctuation
	
	m1=random.choices(let,k=letter)
	m2=random.choices(num,k=number)
	m3=random.choices(sym,k=pun)
	password1 =m1+m2+m3
	
	random.shuffle(password1)
	password = ''.join(password1)
	print('\nthe password: ',password)


