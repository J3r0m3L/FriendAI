import eel 
toggleman = False
def toggleon():
    global toggleman
    toggleman = True

def toggleoff():
    global toggleman
    toggleman = False
  
eel.init('GUI')
eel.start('index.html', block=False)

@eel.expose
def toggle(boolean):
    if boolean == 'true':
        toggleon()
        print('true_good')
    else:
        toggleoff()
        print('false_good')

@eel.expose
def main():
    while(True):
        if (toggleman == True):
                
                eel.addHistory('works')
                    
        eel.sleep(0.05)

main()

