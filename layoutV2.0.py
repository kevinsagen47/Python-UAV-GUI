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
    Bat_1.place(x = 45, y = 28)
    Bat_2.place(x = 235, y = 28)

    Pitch.place(x = 45, y = 48)
    Roll.place(x = 235, y = 48)

    Alti.place(x = 45, y = 88)
    Throttle.place(x = 235, y = 88)
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
    varYaw=StringVar()
    varThrot=StringVar()
    
    Bat1__ = Label(textvariable=varBat1).place(x = 50, y= 8)
    Bat2__ = Label(textvariable=varBat2).place(x = 250, y= 8)

    alti__ = Label(textvariable=varAlti).place(x = 50, y= 68)
    Throt__=Label(textvariable=varThrot).place(x = 250, y= 68)
    
    error__ = Label(textvariable=varerror).place(x = 45, y= 108)
    Sat__=Label(textvariable=varSat).place(x = 235, y= 108)

    lon__=Label(textvariable=varlon).place(x = 45, y= 128)
    lat__=Label(textvariable=varlat).place(x = 235, y= 128)

    Exec__=Label(textvariable=varExec).place(x = 45, y= 148)
    flightm__ = Label(textvariable=varflightmode).place(x = 235, y= 148)
    Start__= Label(textvariable=varStart).place(x = 235, y= 168)
    #Start__= Label(textvariable=varRTH).place(x = 322, y= 108)
    Yaw__= Label(textvariable=varYaw).place(x = 45, y= 168)
    
    
    while(1):
        """
        if(vStop==1):
            varRTH=69
            vStop=0
        else:
            varRTH=40
            vStop=1"""
        #send_datas="<0,"+str(varRTH)+','+"2"+","+"3"+","+"4"+ ","+"1"+","+"2"+","+"3"+","+"4"+">"   
        #serial_object.write(send_datas)
        
        
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
                varThrot.set(filter_data[4])
                
                varflightmode.set(filter_data[6])
                varSat.set(filter_data[7])
                varlon.set(filter_data[8])
                varlat.set(filter_data[9])
                varerror.set(filter_data[10])
                varStart.set(filter_data[11])
               # varStart.set(varRTH)
                varExec.set(filter_data[12])
                varYaw.set(filter_data[13])
            
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
    #varRTH+=1
    #return varRTH

def RTHon(event):
    global varRTH
    varRTH=1


def RTHoff(event):
    global varRTH
    varRTH=0


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
    Bat1_ = Label(text = "Bat 1:").place(x = 8, y= 18)
    Volt1_=Label(text = "x0.01 Volts").place(x=80,y=8)

    Bat2_ = Label(text = "Bat 2:").place(x = 190, y= 18)
    Volt2_=Label(text = "x0.01 Volts").place(x=280,y=8)
    
    Pitch_ = Label(text = "Pitch:").place(x = 8, y= 48)
    Roll_ = Label(text = "Roll:").place(x = 190, y= 48)

    Alti_ = Label(text = "Alti:").place(x = 8, y= 78)
    DM_=Label(text = "x0.1 Meters").place(x=100,y=68)
    
    Throttle_ = Label(text = "Throt:").place(x = 190, y= 78)

    error_=Label(text = "Error:").place(x = 8, y= 108)
    Sat_=Label(text = "Sat :").place(x = 190, y= 108)

    lon_=Label(text = "lon :").place(x = 8, y= 128)
    lat_=Label(text = "lat :").place(x = 190, y= 128)
        
    exec_=Label(text = "Exec:").place(x = 8, y= 148)
    mode_=Label(text = "Mode:").place(x = 190, y= 148)
    #start_=Label(text = "Start:").place(x =285, y= 168)
    Yaw_=Label(text = "Yaw:").place(x = 8, y= 168)

    degree_sign=u"\N{DEGREE SIGN}"
    degree_=Label(text=degree_sign).place(x = 70, y= 168)

    start_=Label(text = "Start:").place(x =190, y= 168)
    #progress_bars
    Bat_1 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 1680)
    Bat_2 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 840)
    Pitch = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 2000)
    Roll = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 2000)
    Throttle = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 2000)
    Alti = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 145, max = 255)
    
   
    
    #Entry
    data_entry = Entry()
    data_entry.place(x = 1, y = 430)




    #radio button
    button_var = IntVar()
    #button
    connect = Button(text = "Connect", command = connect,bg='green').place(x = 15, y = 385)
    disconnect = Button(text = "Disconnect", command = disconnect,bg='coral').place(x =390, y = 385)

    #varRTH=0
    #RTHb=Button(text="RTH",command=lambda *args:RTH(1),width=6).place(x=15,y=315)
    #RTHb=Button(text="RTH",command=RTH,width=6).place(x=15,y=315)
    RTHb=Button(text="RTH",width=20)
    RTHb.place(x=395,y=8)
    RTHb.bind('<ButtonPress-1>',RTHon)
    RTHb.bind('<ButtonRelease-1>',RTHoff)

    Stopb=Button(text="STOP",width=20,bg='red')
    Stopb.place(x=580,y=8)

    takeoffb=Button(text="^ Take Off ^",width=20)
    takeoffb.place(x=395,y=38)

    landingb=Button(text="v Landing v",width=20)
    landingb.place(x=580,y=38)

    Loc1_=Label(text = "Set Location 1:").place(x = 395, y= 88)
    Lon1_=Label(text = "Lon 1:").place(x = 385, y= 108)
    lon1 = Entry()
    lon1.place(x = 425, y = 108)

    Lat1_=Label(text = "Lat 1 :").place(x = 385, y= 128)
    lat1 = Entry()
    lat1.place(x = 425, y = 128)

    Loc2_=Label(text = "Set Location 2:").place(x = 572, y= 88)
    Lon2_=Label(text = "Lon 2:").place(x = 572, y= 108)
    lon2 = Entry()
    lon2.place(x = 612, y = 108)

    Lat2_=Label(text = "Lat 2 :").place(x = 572, y= 128)
    lat2 = Entry()
    lat2.place(x = 612, y = 128)

    Gob=Button(text="Execute Mission!!!",width=20,height=2,bg='lawngreen')
    Gob.place(x=508,y=158)


    altupb=Button(text="^ alt ^",height=4,bg='dodgerblue')
    altupb.place(x=87,y=220)

    altdownb=Button(text="v alt v",height=4,bg='dodgerblue')
    altdownb.place(x=87,y=300)

    yawleftb=Button(text="< Yaw",width=5,height=2,bg='dodgerblue')
    yawleftb.place(x=20,y=275)

    yawrightb=Button(text="Yaw >",width=5,height=2,bg='dodgerblue')
    yawrightb.place(x=150,y=275)

    

    pitchupb=Button(text="^Pitch^",height=4,bg='dodgerblue')
    pitchupb.place(x=607,y=220)

    pitchdownb=Button(text="vPitchv",height=4,bg='dodgerblue')
    pitchdownb.place(x=607,y=300)

    rollleftb=Button(text="< Roll",width=5,height=2,bg='dodgerblue')
    rollleftb.place(x=535,y=275)

    rollrightb=Button(text="Roll >",width=5,height=2,bg='dodgerblue')
    rollrightb.place(x=680,y=275)
    
    #landingb=Button(text="v Landing v",width=20)
    #landingb.place(x=580,y=38)
    



    #mainloop
    gui.geometry('770x430+0+0')
    gui.mainloop()
    
