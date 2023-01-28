
from password_generator import PasswordGenerator 
import os,time,string,pyautogui,random
import keyboard

pwo = PasswordGenerator()


def wait(seconds):
    time.sleep(seconds)

def getFirstName():
    names_list = ["Emma","Liam","Oliver","Amelia","Jack","Isabella","Noah","Sophia","George","Charlotte","Harry","Daisy","William","Poppy","James","Ava","Benjamin","Isla","Alexander","Lucy","Michael", "Evelyn","Elizabeth","Harriet","Joseph","Alice","Samuel","Chloe","David","Mia","Daniel","Harper","Matthew","Elsie","Ryan","Ella","Adam","Imogen","Thomas","Sophie","Jake","Grace","Luke","Rosie","Joshua","Lola","Andrew","Freya","Jonathan","Phoebe","Benjamin","Florence","Nathan","Brooke","Christopher","Holly","Lewis","Mia","Tyler","Leah","Zachary","Eliza","Aaron","Summer","Kyle","Scarlett","Brandon","Abigail","Lewis","Isabelle","Jordan","Sienna","Dylan","Harper","Alex","Aria","Connor","Amelia","Ellie","Isabella","Jessica","Lucy","Charlotte","Emily","Sophie","Megan","Lauren","Bethany","Abigail","Chloe","Holly","Ellie","Lucy","Rebecca","Rachel"]
    name = random.choice(names_list)
    return name
def getLastName():
    last_names_list = ["Smith","Jones","Williams","Brown","Taylor","Davies","Evans","Moore","Wilson","Thomas","Johnson","Roberts","Robinson","Thompson","White","Hughes","Edwards","Green","Hall","Wood","Harris","Lewis","Martin","Jackson","Clarke","Turner","Hill","Scott","Cooper","King","Wright","Lopez","Carter","Mitchell","Perez","Green","Robertson","Chapman","Webb","Jordan","Lawrence","Garner","Ellis","Harrison","Gibson","Mcdonald","Cruz","Marshall","Ortiz","Gomez","Murray","Freeman","Wells","Webb","Simpson","Stevens","Tucker","Porter","Hunter","Hicks","Crawford","Henry","Boyd","Mason","Morales","Kennedy","Warren","Dixon","Ramos","Reyes","Burns","Gordon","Shaw","Holmes","Rice","Robertson","Hunt","Black","Daniels","Palmer","Mills","Nichols","Grant","Knight","Ferguson","Rose","Stone"]
    lastName = random.choice(last_names_list)
    return lastName

def getUsername():
    adjectives = ['adorable', 'beautiful', 'clean', 'drab', 'elegant', 'fancy', 'glamorous', 'handsome', 'long', 'magnificent', 'old-fashioned', 'plain', 'quaint', 'sparkling', 'ugliest', 'unsightly', 'wide-eyed', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gray', 'black', 'white', 'pink']
    nouns = ['cat', 'dog', 'horse', 'pig', 'cow', 'chicken', 'duck', 'goose', 'sheep', 'bird', 'fish', 'whale', 'dolphin', 'butterfly', 'lizard', 'toad', 'bear', 'lion', 'tiger', 'elephant', 'monkey', 'giraffe', 'zebra', 'llama', 'hippopotamus', 'rhinoceros', 'kangaroo', 'leopard', 'panda']
    num = list(range(1, 10000))
    numberhigher = list(range(999, 10000))
    username = random.choice(adjectives) + "." +  random.choice(nouns) + random.choice(str(num)) 
    print(username)
    return username

def random_year():
    start = 1985
    end = 2002
    return str(random.randint(start, end))

firstName = getFirstName()
lastName = getLastName()
username = getUsername()
year = random_year()



#settings
pwo.minlen = 30 # (Optional)
pwo.maxlen = 30 # (Optional)
pwo.excludeschars = "!%^>+.,-=)("

password = pwo.generate()


f = open("accountDetails.txt", "w")
f.write("")
f.write("first name: "+ firstName+"\nlast name: "+lastName+"\nusername: "+username + "\npassword: "+password+"\nBirth Year: "+year)
f.close()
print(pyautogui.size())

pyautogui.moveTo(1530, 100, duration = 1)

#pyautogui.moveRel(0, 50, duration = 1)

print(pyautogui.position())

os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
wait(0.2)
#fullscreen google
pyautogui.leftClick()
wait(0.2)
pyautogui.moveTo(556, 45, duration = 0.25)
pyautogui.leftClick()
#enter address 
pyautogui.typewrite("outlook.com")
wait(0.2)
#enters the address into google
pyautogui.typewrite(["enter"])

# moves to create account
wait(0.2)
pyautogui.moveTo(1327, 940, duration = 0.25)
wait(1)
#press to create new account
pyautogui.leftClick()
wait(2)
pyautogui.typewrite(username)
wait(0.1)
pyautogui.typewrite(["tab","tab","enter"])
wait(1)
pyautogui.typewrite(password)
wait(0.3)
pyautogui.typewrite(["tab","enter"])
wait(1)
pyautogui.typewrite(firstName)
wait(0.1)
pyautogui.typewrite(["tab"])
wait(0.1)
pyautogui.typewrite(lastName)
wait(0.1)
#removes save password popup
pyautogui.moveTo(1732, 335, duration = 0.25)
wait(0.5)
pyautogui.leftClick()
wait(0.25)
pyautogui.typewrite(["tab","tab","tab"])
wait(0.2)
pyautogui.typewrite(["enter"])
wait(1)
pyautogui.typewrite(["tab","enter"])
wait(.5)
pyautogui.typewrite(["down","enter",])
wait(1)
pyautogui.typewrite(["tab"])
wait(0.2)
pyautogui.typewrite(["enter"])
wait(0.2)
pyautogui.typewrite(["down"])
wait(0.2)
pyautogui.typewrite(["enter"])
wait(0.2)
pyautogui.typewrite(["tab"])
wait(1)
pyautogui.typewrite(str(year))
wait(0.5)
pyautogui.typewrite(["tab","enter"])
wait(2)
pyautogui.typewrite(["tab"])
print('\033[93m' + "PLEASE ENTER THE CAPTCHA TO COMPLETE THE ACCOUNT PROCESS"+ '\033[0m')
