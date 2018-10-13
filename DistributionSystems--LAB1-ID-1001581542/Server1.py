import socket
from threading import Thread
import os
import pandas as pd
import  tkinter
import sys
from tkinter import messagebox as tkMessageBox
from string import whitespace

TCP_IP = 'localhost'  #keeping localHost or loopback address:127.0.0.1
TCP_PORT = 9001    #Port no 9001
BUFFER_SIZE = 4096 #buffer size has been kept to 4096

#CREATED BY ASHUTOSH UPADHYE

"""Citations for Tkinter: 1.http://zetcode.com/gui/tkinter/layout/ 
2.http://python-  textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
3.https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-  alongside-tkinters-event-loop
4.https://stackoverflow.com/questions/10727131/why-is-tkinter-entrys-get-  function-returning-nothing
5.https://www.python-course.eu/tkinter_entry_widgets.php """


"""For Socket-Programming and data flow over sockets
1.https://stackoverflow.com/questions/18310152/sending-binary-data-over-  sockets-with-python
2.https://stackoverflow.com/questions/1472876/why-is-host-aborting-  connection
3.http://www.geeksforgeeks.org/socket-programming-python/
4.http://www.bogotobogo.com/python/python_network_programming_server_client_  file_transfer.php
5.https://www.tutorialspoint.com/python/python_networking.htm
6.http://www.bogotobogo.com/python/python_network_programming_server_client.  php
7.http://www.bogotobogo.com/python/python_network_programming_server_client.  php

For Pandas API dataframe
1.https://stackoverflow.com/questions/42269166/how-to-convert-to-convert-    pandas-dataframe-into-bytes-and-vice-versa
2.https://stackoverflow.com/questions/33957720/how-to-convert-column-with-    dtype-as-object-to-string-in-pandas-dataframe
3.https://pandas.pydata.org/pandas-  docs/stable/generated/pandas.DataFrame.html
4.https://stackoverflow.com/questions/11285613/selecting-columns-in-a-  pandas-dataframe """

class ClientThread(Thread):


    global Received_word
    global Received_string
    global keywords
    global found_row
    global found_row1
    global window1
    global T


    def __init__(self,ip,port,sock): # Thread Executes and object passed via "self" parameter takes ip,port,socket information
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))
        #New Thread Starts and Info is printed in the UI or python shell

    def run(self):
        Received_word = conn.recv(1024)#Connection Starts and Server looks for incoming buffer as in the form of words to search
        Received_string = str(Received_word, encoding='utf-8')#utf-8 encoding should be decoding in order to process string

        #tkMessageBox.showinfo("Information"," New thread started for "+ip+":"+str(port))
        window1 = tkinter.Tk() #Initilize Window
        T = tkinter.Text(window1, height=760, width=1000)
        window1.title("Server")
        T.pack()
        T.insert(tkinter.END, "waiting for incoming connections........."+"\n")
        T.insert(tkinter.END, "Got Connection from:" + "IP:" + str(ip) + "\tPort:" + str(port)+"\n")
        ThreadInfo = "New Thread started for "+ip+":"+str(port)+"\n"#ThreadInformation
        T.insert(tkinter.INSERT, ThreadInfo) #Setting ThreadInfo in the UI
        window1.geometry("1024x768")#Setting Resolution for the window

        filename = "PythonServerFile.csv"#File to be used on local Server
        directory = os.path.normpath("C:/Users/Ashutosh/Desktop")
        f = open(os.path.join(directory, filename), 'r')
        df = pd.read_csv("../DistributionSystems--LAB1-ID-1001581542/PythonServerFile.csv", header=None)#Reading file and passing data in data frame using pandas
        print(df.head())#printing first 10 records of the frame if available

       #Printing Dimensions of Data Frame

        rows = df.shape[0]#Printing rows of dataframe
        columns = df.shape[1]#Printing columns of dataframe

        print("rows of dataframe:%s", rows)
        print("cols of dataframe:%s", columns)

        rowString = "Row Dimension of Data Frame:"+ str(rows)+"\n"
        rowColumns = "Row Dimension of Data Frame:" + str(columns)+"\n"


        #Printing Rows and Columns in GUI
        T.insert(tkinter.END, rowString)
        T.insert(tkinter.END, rowColumns)

        for index in range(columns):#Searching Data frame for the required word
            for index1 in range(rows):
                print("DF.icolINDICES:" + str(df.icol(index)))
                print("Received string:" + str(Received_string))
                if (Received_string  in  str(df.icol(index))) and (Received_string in str(df.irow(index1))):#if word is found in corresponding row and column
                    print(df.irow(index1))
                    found_row = (df.irow(index1).astype('str'))#found row with the query word
                    print("found")
                #elif(Received_string not in  str(df.icol(index))) and (Received_string not in str(df.irow(index1))):#if word not found in corresponding row and columns
                 #   found_row="word not found.Please enter another word"
        found_row1 = (str(found_row).strip()).translate((None,whitespace))#Remove whiteSpaces from the found string
        print('found_row1:' + found_row1)
        T.insert(tkinter.END,"\n"+str(found_row1)+"\n")#Print String to GUI


        while True:
            l = bytes(str(found_row1).encode('utf-8'))#Encode found string to UTF-8
          #  l1=l[BUFFER_SIZE]
            print("size L:",sys.getsizeof(l))
            print(l)
            l1 = f.read(BUFFER_SIZE).encode('utf-8')
            while (l):
               if(self.sock.send(l)):#Send String via socket from the Server to the Client
                 print('Sent ',repr(l))
                 T.insert(tkinter.END, "Sent Data is:"+repr(l)+"\n")
                 window1.mainloop()#Generate Window for the GUI
                 break
                #l1 = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()#Close Connection

                break


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))#Bind Server with the Given localhost and port
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")#Wait for incoming Connections
    (conn, (ip,port)) = tcpsock.accept()
    print('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)#Assign a new Thread for each seperate Connection and operate concurrently
    newthread.start()
    threads.append(newthread)#Append the new thread with the old existing Thread

for t in threads:
    t.join()

