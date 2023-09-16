##try and except
##if conditin matches, it will return output from else statment
## if conditin did not match, it will try to match except handler. the one which matches
##gets displayed

def try_it(value):
    try:
        x = int(value)
    except ValueError: ##if try fails, it runs and go to finally
        print(f'{value} could not be converted to an integer')
    else: #if try code executes successfully else clause will run
        print(f'int{value} is {x}')
    finally: ##finally always executes no matter what
        print('finally executed')

print(try_it(10))