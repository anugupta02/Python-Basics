
'''
from gtts import gTTS
import os

tes=input("Enter Test")
language='en'
obj=gTTS(text=test,lang=language,slow=False)
obj.save('wel.mp3')
#os.system("mpg321 wel.mp3")
'''

from gtts import gTTS 
import os 
test = input ('enter')
language= 'en'
obj = gTTS (text = test , lang = language, show = False ) 
obj.save('wel.mp3')
 
