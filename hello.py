# Ask user for their name.
name = input ("What's your name? ").strip().title() #Input tiene dentro el mensaje que queremos mostrar.
# Functions can be put into the input.

# Remove whitespace from str
# name = name.strip()

# Capitalize user's name
# name = name.capitalize() # Capitalize the first letter

# Capitalize the first letter of every word
# name = name.title()

# name = name.strip().title() # We can merge different functions.

# Say hello to user. 
print ("hello,", name) # Comma between arguments add a space when shown in the terminal.
print (f"hello, {name}")
