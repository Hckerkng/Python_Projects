from gtts import gTTS
import os
wel = 'Welcome to Our bank we are happy to help you'
language = 'en'
mybank = gTTS(text=wel, lang=language, slow=False)
mybank.save("welcome.mp3")
os.system("welcome.mp3")
    
