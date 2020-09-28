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
serial_object = serial.Serial('/dev/tty' + 'ACM0', 115200)
gui = Tk()
gui.title("UAV Command Software")

varRTH=0
vStop=0

def connect():
    global serial_object
    port = 'ACM0'
   # port = 'AMA0'
    baud = '115200'   
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
    global vStop
    global varRTH
    
    t.place(x = 3, y = 425)
    Bat_1.place(x = 45, y = 8)
    Bat_2.place(x = 235, y = 8)

    Pitch.place(x = 45, y = 28)
    Roll.place(x = 235, y = 28)

    Alti.place(x = 45, y = 48)
    Throttle.place(x = 235, y = 48)
    new = time.time()


    varBat1=StringVar()
    varBat2=StringVar()
    varAlti=StringVar()
    
    varflightmode=StringVar()
    varSat=StringVar()
    varlon=StringVar()
    varlat=StringVar()
    varerror=StringVar()
    varStart=StringVar()
    varExec=StringVar()
    
    Bat1__ = Label(textvariable=varBat1).place(x = 50, y= 8)
    Bat2__ = Label(textvariable=varBat2).place(x = 250, y= 8)

    alti__ = Label(textvariable=varAlti).place(x = 170, y= 48)

    error__ = Label(textvariable=varerror).place(x = 45, y= 68)
    Sat__=Label(textvariable=varSat).place(x = 235, y= 68)

    lon__=Label(textvariable=varlon).place(x = 45, y= 88)
    lat__=Label(textvariable=varlat).place(x = 235, y= 88)

    Exec__=Label(textvariable=varExec).place(x = 45, y= 108)
    flightm__ = Label(textvariable=varflightmode).place(x = 235, y= 108)
    Start__= Label(textvariable=varStart).place(x = 322, y= 108)
    #Start__= Label(textvariable=varRTH).place(x = 322, y= 108)


    
    while(1):
        """
        if(vStop==1):
            varRTH=69
            vStop=0
        else:
            varRTH=40
            vStop=1"""
        send_datas="<0,"+str(varRTH)+','+"2"+","+"3"+","+"4"+ ","+"1"+","+"2"+","+"3"+","+"4"+">"   
        serial_object.write(send_datas)
        
        
        if filter_data:

            #text.insert(END, filter_data) <-- the text box text
            #text.insert(END,"\n")
            try:
                Bat_1["value"] = filter_data[0]
                Bat_2["value"] = filter_data[1]
                Pitch["value"] = filter_data[2]
                Roll["value"] = filter_data[3]
                Throttle["value"] = filter_data[4]
                Alti["value"] = filter_data[5]

                varBat1.set(filter_data[0])
                varBat2.set(filter_data[1])
                varAlti.set(filter_data[5])
                
                varflightmode.set(filter_data[6])
                varSat.set(filter_data[7])
                varlon.set(filter_data[8])
                varlat.set(filter_data[9])
                varerror.set(filter_data[10])
                varStart.set(filter_data[11])
               # varStart.set(varRTH)
                varExec.set(filter_data[12])
            
            except :
                pass

            
            if time.time() - new >= update_period:
                #text.delete("1.0", END)
                Bat_1["value"] = 0
                Bat_2["value"] = 0
                Pitch["value"] = 0
                Roll["value"] = 0
                Throttle["value"] = 0
                Alti["value"] = 0

                
                new = time.time()


def send():
    send_data = data_entry.get()
    
    if not send_data:
        print "Sent Nothing"
    
    serial_object.write(send_data)

def RTH():
    global varRTH
    varRTH+=1
    #return varRTH

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
    Bat1_ = Label(text = "Bat 1:").place(x = 8, y= 8)
    Bat2_ = Label(text = "Bat 2:").place(x = 190, y= 8)
    
    Pitch_ = Label(text = "Pitch:").place(x = 8, y= 28)
    Roll_ = Label(text = "Roll:").place(x = 190, y= 28)

    Alti_ = Label(text = "Alti:").place(x = 8, y= 48)
    Throttle_ = Label(text = "Throt:").place(x = 190, y= 48)

    error_=Label(text = "Error:").place(x = 8, y= 68)
    Sat_=Label(text = "Sat :").place(x = 190, y= 68)

    lon_=Label(text = "lon :").place(x = 8, y= 88)
    lat_=Label(text = "lat :").place(x = 190, y= 88)
        
    exec_=Label(text = "Exec:").place(x = 8, y= 108)
    mode_=Label(text = "Mode:").place(x = 190, y= 108)
    start_=Label(text = "Start:").place(x =285, y= 108)
    #progress_bars
    Bat_1 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 1680)
    Bat_2 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 840)
    Pitch = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 2000)
    Roll = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 2000)
    Throttle = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 2000)
    Alti = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 255)
    
   
    
    #Entry
    data_entry = Entry()
    data_entry.place(x = 100, y = 255)




    #radio button
    button_var = IntVar()
    #button
    connect = Button(text = "Connect", command = connect).place(x = 15, y = 360)
    disconnect = Button(text = "Disconnect", command = disconnect).place(x =300, y = 360)

    #varRTH=0
    #RTHb=Button(text="RTH",command=lambda *args:RTH(1),width=6).place(x=15,y=315)
    RTHb=Button(text="RTH",command=RTH,width=6).place(x=15,y=315)
    
    #mainloop
    gui.geometry('770x430+0+0')
    gui.mainloop()
    
