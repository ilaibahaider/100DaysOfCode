#Caeser Cipher
import art 
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
  'v', 'w', 'x', 'y', 'z']

def caesar(cipher_text, shift_amount, cipher_direction): 				   #cipher_direction = encode or decode 
	output_text = ""
	if cipher_direction == "decode":                #Changes the sign to negative if user inputs 'decode'
		shift_amount *= -1
	for letter in cipher_text: 
		if letter not in alphabet: 					#any letter that is not an alphabet, will be left as it was
			output_text += letter
		else:		
			shifted_position = alphabet.index(letter) + shift_amount #Adds shifted number to the index of each letter
			shifted_position %= len(alphabet) # 0-25
			output_text += alphabet[shifted_position]                #Stores final string with updated shifted indexes
	print(f"Here is the {cipher_direction}d result : {output_text}")

should_continue = True

while should_continue: 
	
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	
	caesar(cipher_text = text, shift_amount = shift, cipher_direction = direction)

	restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

	if restart == "no":
		should_continue = False
		print("Goodbye")
