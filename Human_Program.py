# Importing os library to interact wiith operating system
import os

#initializing the program 
print('Welcome to my program')

#writing the logic
while True:
    print("Type your text and lets chat : "  , end='')
    p = input()
    
    x = 'run' in p or 'launch' in p or 'execute' in p or 'open' in p
    y = 'stop' in p or 'quit' in p or 'exit' in p
    
    if ('media' in p and 'player' in p) and x:
        os.system('wmplayer')
    elif ('notepad' in p or 'editor' in p) and x:
        os.system('notepad')
    elif 'chrome' in p and x:
        os.system('chrome')
    elif ('adobe' in p and 'acrobat' in p) and x:
        os.system('AcroRd32')
    elif ('vlc' in  p and 'player' in p) and x:
        os.system('vlc')
    elif 'firefox' in p and x:
        os.system('firefox')
    elif ('vs' in p and 'code' in p) and x:
        os.system('Code')
    elif (('dev' in p and 'c++' in p) or 'devc++' in p) and x:
        os.system('devcpp')
    elif 'Photoshop' in p and x:
        os.system('Photoshop')
    elif ('Adobe' in p and 'After' in p and 'Effects' in p) and x:
        os.system('AfterFX')
    elif ('Adobe' in p and 'Illustrator' in p) and x:
        os.system('Illustrator')
    elif ('excel' in p or 'spreadsheet' in p) and x:
        os.system('EXCEL')
    elif 'powerpoint' in p and x:
        os.system('POWERPNT')
    elif 'word' in p and x:
        os.system('WINWORD')
    elif 'skype' in p and x:
        os.system('lync')
    elif y:
        break
    else:
        print('Does not support')

#end of program
print('Program ends')
    

