from tkinter import *
import requests
def test_func(entry1):
    print("Entry: ", entry1)
#e41b9acc43d589420ab1aefb15476381
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}


def form_res(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = "City: "+str( name) + "\n  " +"Conditions: "+str(desc)+ " \n " +"Temp: "+str( temp)
    except:
        final_str = 'There was a problem \n retrieving the data'
    return final_str
def get_weather(city):
    weather_key = 'e41b9acc43d589420ab1aefb15476381'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}                                  #sending the request to the server
    response = requests.get(url, params=params)
    weather = response.json()                                                  #will convert to python dictionary that we can work with

    label2['text'] = form_res(weather)

root1 = Tk()

canvas = Canvas(root1, height=400,width=500)
canvas.pack()

background_img = PhotoImage(file='./aurora.png')
bk_label = Label(root1,image=background_img)
bk_label.place(relwidth=1,relheight=1)

frame1 = Frame(root1, bd=5, bg='#80c1ff')
frame1.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

entry1 = Entry(frame1,font=40)
entry1.place(relheight=1,relwidth=0.65)

button3 = Button(frame1,text='Get weather', command=lambda: get_weather(entry1.get()))
button3.place(relx=0.7,relheight=1,relwidth=0.30)

frame2 = Frame(root1, bd=10,bg = '#80c1ff')
frame2.place(relx=0.5,rely=0.25,relheight=0.6,relwidth=0.75,anchor='n')

label2 = Label(frame2, font=('Courier',14))
label2.place(relwidth=1,relheight=1)

root1.mainloop()
