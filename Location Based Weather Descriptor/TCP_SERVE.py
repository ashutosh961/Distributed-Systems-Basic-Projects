import urllib.request
import requests
import datetime
import time
import json
import tkinter
from tkinter import *
TCP_PORT = 8080
BUFFER_SIZE = 4096
struct = {}

global information
global lat
global lon

#NAME:ASHUTOSH UPADHYE
#ID:1001581542

#lat = float(input('Please Enter any latitude: '))
#lon = float(input('Please Enter any longitude: '))

top = tkinter.Tk()#Tkinter Frame initialisation
top.title("Client")
text = tkinter.Text(top)

text.pack()
input_variable = StringVar(top)#Input latitude
input_variable2 = StringVar(top)#Input longitude
L1 = tkinter.Label(top, text="Enter Latitude:")#Label for latitude
L2 = tkinter.Label(top, text="Enter Longitude:")#Label for longitude
L1.pack(side=tkinter.LEFT)
E1 = Entry(top,textvariable=input_variable,bd=2,bg="lightblue")
E1.pack(side=tkinter.LEFT)#Entry Boxes for latitude

L2.pack(side=tkinter.LEFT)

E2 = Entry(top,textvariable=input_variable2,bd=2,bg="lightblue")
E2.pack(side=tkinter.LEFT)#Entry Boxes for longitude

#Establish Connection after lat and lon parameters are inserted

def getplace():
   # url = 'http://forecast.weather.gov/MapClick.php?'+'lat='+str(lat)+'&'+'lon='+str(lon)
    lat = input_variable.get()#Get longitude
    lon = input_variable2.get()#Get latitude
    print("lat:" + lat)
    print("lon:" + lon)
    url1 = 'https://api.weather.gov/points/'+str(lat)+','+str(lon)+'/forecast'
    url = 'https://api.weather.gov/points/' + str(lat) + ',' + str(lon)
    print('Date Executed:'+str(datetime.datetime.now()))#Print execution Data
    print("URL:"+url1)
    request = requests.get(url1)#Establish socket connection with the given url1
    text.insert(tkinter.INSERT, "Connection Established" "\n")#print connection established
    ReadData = json.loads(request.content)#load response into json contentloader
    print(ReadData)#print the json data
    request1 = requests.get(url)#ping url to get state name and city name
    ReadData1 = json.loads(request1.content)#Load it into json content loader
    temperature = (ReadData['properties']['periods'][0]['temperature'])#Temperature factor from the json content
    windSpeed = (ReadData['properties']['periods'][0]['windSpeed'])#Windspeed factor from the json content
    shortForecast = (ReadData['properties']['periods'][0]['shortForecast'])#shortforecast from the json content
    detailedForecast = (ReadData['properties']['periods'][0]['detailedForecast'])#detailedForecast from the json content
    windDirection = (ReadData['properties']['periods'][0]['windDirection'])#winddirection from the json content
    city = (ReadData1['properties']['relativeLocation']['properties']['city'])#City from the json content
    state = (ReadData1['properties']['relativeLocation']['properties']['state'])#state from the json content
    print("Temperature is:"+str(temperature)+"F")
    print("WindSpeed is:" + str(windSpeed))
    print("ShortForeCast is:" + str(shortForecast))
    print("WindDirection is:" + str(windDirection))
    print("City is:"+city)
    print("State is:"+state)
    print("Detailed Forecast is:"+detailedForecast)

#Insert Text Data in the Tkinter Frame
    text.insert(tkinter.INSERT, "Fetching Data""\n")
    text.insert(tkinter.INSERT, "Latitude is:" + str(lat) + "\n")
    text.insert(tkinter.INSERT, "Longitude is:" + str(lon) + "\n")
    text.insert(tkinter.INSERT,"City is:"+str(city)+"\n")
    text.insert(tkinter.INSERT, "State is:" + str(state) + "\n")
    text.insert(tkinter.INSERT, "Temperature is:" + str(temperature)+"F"+"\n")
    text.insert(tkinter.INSERT, "windspeed is:" + str(windSpeed) + "\n")
    text.insert(tkinter.INSERT, "windDirection is:" + str(windDirection)+"\n")
    text.insert(tkinter.INSERT, "ShortForecast is:" + str(shortForecast) + "\n")
    text.insert(tkinter.INSERT, "DetailedForecast is:" + str(detailedForecast) + "\n")

    if ReadData:#if response is got then explicitly close the socket and close the connection
        request.close()#Close the socket connection on url1
        request1.close()#Close the socket connection on url
        print("Connection Socket Closed")
        text.insert(tkinter.INSERT, "Connection Socket Closed.""\n")


#Refresh the connection manually
def refresh():
   # url = 'http://forecast.weather.gov/MapClick.php?'+'lat='+str(lat)+'&'+'lon='+str(lon)
    lat = input_variable.get()#Get Input latitude
    lon = input_variable2.get()#Get input longitude
    print("lat:" + lat)
    print("lon:" + lon)
    url1 = 'https://api.weather.gov/points/'+str(lat)+','+str(lon)+'/forecast'#Re-establish connection to the url1
    url = 'https://api.weather.gov/points/' + str(lat) + ',' + str(lon)#Re -establish connection to the url
    print('Date Executed:'+str(datetime.datetime.now()))
    print("URL:"+url1)
    request = requests.get(url1)
    text.insert(tkinter.INSERT, "Connection Re-Established" "\n")
    ReadData = json.loads(request.content)#Get JSON Response for url1
    request1 = requests.get(url)
    ReadData1 = json.loads(request1.content)#Get JSON Response for url
    temperature = (ReadData['properties']['periods'][0]['temperature'])#Temperature record from JSON Response
    windSpeed = (ReadData['properties']['periods'][0]['windSpeed'])#Windspeed record
    shortForecast = (ReadData['properties']['periods'][0]['shortForecast'])#ShortForecast record
    detailedForecast = (ReadData['properties']['periods'][0]['detailedForecast'])#DetailedForecast record
    windDirection = (ReadData['properties']['periods'][0]['windDirection'])#WindDirection record
    city = (ReadData1['properties']['relativeLocation']['properties']['city'])
    state = (ReadData1['properties']['relativeLocation']['properties']['state'])
    print("Temperature is:"+str(temperature)+"F")
    print("WindSpeed is:" + str(windSpeed))
    print("ShortForeCast is:" + str(shortForecast))
    print("WindDirection is:" + str(windDirection))
    print("City is:"+city)
    print("State is:"+state)
    print("DetailedForecast is:"+detailedForecast)
 #Print Details to the GUI
    text.insert(tkinter.INSERT, "Refreshing Data" "\n")
    text.insert(tkinter.INSERT, "Latitude is:" + str(lat) + "\n")
    text.insert(tkinter.INSERT, "Longitude is:" + str(lon) + "\n")
    text.insert(tkinter.INSERT,"City is:"+str(city)+"\n")
    text.insert(tkinter.INSERT, "State is:" + str(state) + "\n")
    text.insert(tkinter.INSERT, "Temperature is:" + str(temperature)+"F"+"\n")
    text.insert(tkinter.INSERT, "windspeed is:" + str(windSpeed) + "\n")
    text.insert(tkinter.INSERT, "windDirection is:" + str(windDirection)+"\n")
    text.insert(tkinter.INSERT, "ShortForecast is:" + str(shortForecast) + "\n")
    text.insert(tkinter.INSERT, "detailedForecast is:" + str(detailedForecast) + "\n")

    if ReadData:#IF response is read then explicitly close the connection sockets
       request.close()#Close socket to url1
       request1.close()#Close socket to url
       print("Connection Socket Closed")
       text.insert(tkinter.INSERT, "Connection Socket Closed.""\n")


submit = Button(top,text="Submit",width=5,height=1,bg="green",command = getplace)
submit.pack(side=tkinter.RIGHT)#Place submit button
refresh = Button(top,text="Refresh",width=5,height=1,bg="green",command = refresh)
refresh.pack(side=tkinter.RIGHT)#Place refresh button

top.mainloop()#GUI Display













