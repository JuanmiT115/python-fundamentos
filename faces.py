#This is how to define a function
def main(): 
    text = input('Type something: ')
    text = convert(text)
    print(text)



def convert(text_emoji):
    text_emoji = text_emoji.replace(':)','🙂').replace(':(','🙁')
    return text_emoji

main()