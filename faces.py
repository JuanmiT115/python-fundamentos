#This is how to define a function
def main(): 
    var_1 = input('Type something: ')
    var_1 = convert(var_1)
    print(var_1)



def convert(var_1):
    var_1 = var_1.replace(':)','🙂').replace(':(','🙁')
    return var_1

main()