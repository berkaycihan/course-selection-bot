import pyautogui
import time

pyautogui.alert(text='Bot çalışmaya başlasın mı?(164,591 koordinatı için 10 tekrar )'
                ,title='istihza', button="Tamam");

for i in range(10):
    
    pyautogui.moveTo(164,591,duration=0.5) # target coordinate

    pyautogui.click(button='left', clicks=1, interval=0.75) # active/deactive

    pyautogui.moveRel(0,300,duration=0.5) #300px down

    pyautogui.click(button='left', clicks=1, interval=0.75) #click

    time.sleep(1) # 1 second
    pyautogui.press("enter") #enter
    time.sleep(1) # 1 second
    pyautogui.press("enter"); time.sleep(1) # 1 second
    

    
pyautogui.alert(text= "TAMAMLANDI 10 KEZ DENENDI"
                ,title='istihza', button="Tamam");

