import random
import string
def generatepass():
    maxlength=20
    digits=[]
    specialsign=[]
    maxdigits=5
    maxspecialsign=maxdigits
    password=[]
    for i in range(maxdigits):
        digits.append(random.randint(0,9))
    for i in range(maxspecialsign):
        specialsign.append(random.choice(string.punctuation))
    for i in range(maxlength-maxspecialsign-maxdigits):
        password.append(random.choice(string.ascii_letters))
    for i in range(maxdigits):
        password.append(digits[i])
        password.append(specialsign[i])
    random.shuffle(password)
    res=''
    for i in range(len(password)):
        res+=str(password[i])
    return res

if __name__=='__main__':
    print(generatepass())