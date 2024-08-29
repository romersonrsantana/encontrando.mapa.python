print('\n',' '*27,'Testing Global Variables\n')

def understand():
    global spam
    spam = '\ncooking\n'
    print(spam)
    london()
    USA()

def london():
    spam = '\nt - shirt\n'
    print(spam)

def USA():
    print(spam)

spam = 41
understand()
print(spam)