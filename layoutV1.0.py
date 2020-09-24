"""This is a simple application written in Python and TKinter.
The application's main purpose is not to serve a specific one. This is a generic application
for sending and receiving data from the computer to UART host controller (Arduino).
The major functions are self update and get data which are threaded to make sure the GUI does not freeze.
The GUI runs in the main thread, the worker threads are the two separate ones.
A simple Arduino Test Sketch is also made to test the purpose of this app which sends data in a specific 
format. 
Format: 
    String outgoing_data = {"1,2,3,4,5"};
The array size has been limited to 5 since the UNO has 5 analogue Sources and the progress bars 
represent the 5 bars.
@author: Prateek guru <pratik.gurudatt@gmail.com>
"""


import time
import threading
import Tkinter
from Tkinter import *
import serial
import ttk

serial_data = ''
filter_data = ''
update_period = 5
serial_object = None
gui = Tk()
gui.title("UAV Command Software")




def connect():
    global serial_object
    port = 'ACM0'
   # port = 'AMA0'
    baud = '9600'   
    try:
        try:
            serial_object = serial.Serial('/dev/tty' + str(port), baud)                
        except:
            print "Cant Open Specified Port"
    except ValueError:
        print "Enter Baud and Port"
        return
    t1 = threading.Thread(target = get_data)
    t1.daemon = True
    t1.start()
    
def disconnect():
    """ 
    This function is for disconnecting and quitting the application.
    Sometimes the application throws a couple of errors while it is being shut down, the fix isn't out yet
    but will be pushed to the repo once done.
    simple GUI.quit() calls.
    """
    try:
        serial_object.close() 
    
    except AttributeError:
        print "Closed without Using it -_-"

    gui.quit()

def get_data():
    global serial_object
    global filter_data
    while(1):   
        try:
            serial_data = serial_object.readline().strip('\n').strip('\r')
            
            filter_data = serial_data.split(',')
            print filter_data        
        except TypeError:
            pass

        
def update_gui():
    global filter_data
    global update_period

    t.place(x = 3, y = 425)
    Bat_1.place(x = 60, y = 100)
    Bat_2.place(x = 60, y = 130)
    Pitch.place(x = 60, y = 160)
    Roll.place(x = 60, y = 190)
    Throttle.place(x = 60, y = 220)
    new = time.time()


    varBat1=StringVar()
    varBat2=StringVar()

    varflightmode=StringVar()
    varSat=StringVar()
    varlon=StringVar()
    varlat=StringVar()
    varerror=StringVar()
    
    Bat1__ = Label(textvariable=varBat1).place(x = 160, y= 100)
    while(1):
        if filter_data:

            #text.insert(END, filter_data) <-- the text box text
            #text.insert(END,"\n")
            try:
                Bat_1["value"] = filter_data[0]
                Bat_2["value"] = filter_data[1]
                Pitch["value"] = filter_data[2]
                Roll["value"] = filter_data[3]
                Throttle["value"] = filter_data[4]
                #Alti["value"] = filter_data[5]

                varBat1.set(filter_data[0])
                varBat2.set(filter_data[1])
                
                #varflightmode.set(filter_data[6])
                #varSat.set(filter_data[7])
                #varlon.set(filter_data[8])
                #varlat.set(filter_data[9])
                #varerror.set(filter_data[10])
                
                
                
            
            except :
                pass

            
            if time.time() - new >= update_period:
                #text.delete("1.0", END)
                Bat_1["value"] = 0
                Bat_2["value"] = 0
                Pitch["value"] = 0
                Roll["value"] = 0
                Throttle["value"] = 0
                Alti["value"] = filter_data[5]

                
                new = time.time()


def send():
    send_data = data_entry.get()
    
    if not send_data:
        print "Sent Nothing"
    
    serial_object.write(send_data)



                                    #Main Loop

if __name__ == "__main__":


    #frames   430x770
    frame_1 = Frame(height = 207, width = 378, bd = 3, relief = 'groove').place(x = 5, y = 5)
    frame_2 = Frame(height = 207, width = 378, bd = 3, relief = 'groove').place(x = 383, y = 5)
    frame_3 = Frame(height = 207, width = 378, bd = 3, relief = 'groove').place(x = 5, y = 212)
    frame_4 = Frame(height = 207, width = 378, bd = 3, relief = 'groove').place(x = 383, y = 212)
    t = Text(width = 1, height = 1)
    #text = None 
    
    #threads
    t2 = threading.Thread(target = update_gui)
    t2.daemon = True
    t2.start()

    
    #Labels
    Bat1_ = Label(text = "Bat 1:").place(x = 15, y= 100)
    Bat2_ = Label(text = "Bat 2:").place(x = 15, y= 130)
    Pitch_ = Label(text = "Pitch:").place(x = 15, y= 160)
    Roll_ = Label(text = "Roll:").place(x = 15, y= 190)
    Throttle_ = Label(text = "Throttle:").place(x = 15, y= 220)

    
    
    #progress_bars
    Bat_1 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    Bat_2 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    Pitch = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    Roll = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)
    Throttle = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)

    
   
    
    #Entry
    data_entry = Entry()
    data_entry.place(x = 100, y = 255)




    #radio button
    button_var = IntVar()
    #button
    connect = Button(text = "Connect", command = connect).place(x = 15, y = 360)
    disconnect = Button(text = "Disconnect", command = disconnect).place(x =300, y = 360)
    #mainloop
    gui.geometry('770x430+0+0')
    gui.mainloop()
    
