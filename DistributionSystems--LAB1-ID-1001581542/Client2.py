

import socket
import tkinter
from tkinter import *
import re

global flag
global data
global data1
global input_word
global top
global all_entries
flag = False
all_entries=[]
global root
global text
global TextWidget
global E1
global li
global TCP_IP
global port
global s
#window = tki


#s = socket.socket()             # Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()     #  Get local machine name
TCP_IP = 'localhost'
port = 9001              # Reserve a port for your service.

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#  s.bind((TCP_IP,port))
s.connect((TCP_IP, port))
# er.Tk()
#window.title("Client")
#window.geometry("1024x768")
#window.mainloop()


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

input_word = input('Please Enter any word: ')

top = tkinter.Tk()
top.title("Client")
text = tkinter.Text(top)
#text.insert(tkinter.INSERT,"Sending Data to the Server"+"\n")
#text.insert(tkinter.INSERT, "section\n")
#text.insert(tkinter.END, "blessed")
text.pack()

input_variable = StringVar()
L1 = tkinter.Label(top, text="Enter Input Word:")

L1.pack(side=tkinter.LEFT)
E1 = Entry(top,textvariable=input_variable,bd=2,bg="lightblue")
E1.pack(side=tkinter.LEFT)
#li = E1.get()


def GetData():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((TCP_IP, port))
    input_variable2=input_variable.get()
    if input_variable2 != None and input_variable2 != "PY_VAR0":
       text.insert(tkinter.INSERT, "Sending Data to the Server" + "\n")

       print('Sending Data')
       s.sendall((str(input_variable2.lower()).encode('utf-8')))
       flag = True
    while True:
     if(flag):
         text.insert(tkinter.INSERT, "Input_word:\n" + str(input_word)+"\n")#Print Input word to GUI
         print('receiving data...')
         text.insert(tkinter.INSERT, "Receiving Data\n")
         type="Name"
         data = s.recv(1024)
         print('data=', (data))
         text.insert(tkinter.INSERT, "Actual Data found:\n" + str(data))#Print actual matching row  Data found to tbe GUI
        # text.insert(tkinter.INSERT, "Data=\n"+str(data))

         data1=str(data,encoding='utf-8')# Removing whitespaces and other redundant information such as "Name Record" using string.split
         data2=data1.split("\n")
         for i in range(len(data2)-1):
             if(input_word in str(data2[i])) :
                print("found name and word")#if word is found in the given string print given word
                text.insert(tkinter.INSERT, "found name and word\n" )#Delete the input word and print synonyms
                del data2[i]
                if(type in str(data2[i])):
                    del data2[i]#Delete another redundant info such as record "Name="
                print('data2=',(data2))
                text.insert(tkinter.INSERT, "Synonyms are:\n" + str(data2))
                # Display main client Window
     break



submit = Button(top,text="Submit",width=5,height=1,bg="green",command=GetData)
submit.pack(side=tkinter.RIGHT)

while input_word:#Wait for an input word from the shell
    text.insert(tkinter.INSERT, "Sending Data to the Server" + "\n")

    print('Sending Data')
    s.sendall((input_word.lower().encode('utf-8')))#Send the input word to the Server
    flag = True #Set Flag true after getting input word
    break #Get out of loop
#s.close()






while True:

#If we get the input word
        if(flag):
         text.insert(tkinter.INSERT, "Input_word:\n" + str(input_word)+"\n")#Print Input word to GUI
         print('receiving data...')
         text.insert(tkinter.INSERT, "Receiving Data\n")
         type="Name"
         data = s.recv(1024)
         print('data=', (data))
         text.insert(tkinter.INSERT, "Actual Data found:\n" + str(data))#Print actual matching row  Data found to tbe GUI
        # text.insert(tkinter.INSERT, "Data=\n"+str(data))

         data1=str(data,encoding='utf-8')# Removing whitespaces and other redundant information such as "Name Record" using string.split
         data2=data1.split("\n")
         for i in range(len(data2)-1):
             if(input_word in str(data2[i])) :
                print("found name and word")#if word is found in the given string print given word
                text.insert(tkinter.INSERT, "found name and word\n" )#Delete the input word and print synonyms
                del data2[i]
                if(type in str(data2[i])):
                    del data2[i]#Delete another redundant info such as record "Name="
                print('data2=',(data2))
                text.insert(tkinter.INSERT, "Synonyms are:\n" + str(data2))
                # Display main client Window
         break
        #if not data:#if no data found in the buffer get out of the loop
         #   break
        # write data to a file
        #f.write(data)

top.mainloop()
#f.close()
print("Successfully get the file")
s.close()#Close Connection
print("connection closed")