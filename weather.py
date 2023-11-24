from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk, Image

root = Tk()
root.title("Weather Application")
root.geometry("700x400+300+200")
root.resizable(False, False)

def getweather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time= local_time.strftime("%I:%M %P")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        api = "https://api.openweathermap.org/data/2.5/weather?"+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("weather App","Invalid Entry!")

img1 = Image.open("C:/Users/raraf/OneDrive/Desktop/programming/tkinter/Peraduxshort/search.png")
img2 = Image.open("C:/Users/raraf/OneDrive/Desktop/programming/tkinter/Peraduxshort/bar.png")
img3 = Image.open("C:/Users/raraf/OneDrive/Desktop/programming/tkinter/Peraduxshort/what.png")
img4 = Image.open("C:/Users/raraf/OneDrive/Desktop/programming/tkinter/Peraduxshort/logo.png")

search_image = ImageTk.PhotoImage(img1)
search_icon = ImageTk.PhotoImage(img2)

myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=13, font=("poppins", 25, "bold"), bg="#2E2E2E", border=0, fg="white")
textfield.place(x=40, y=40)
textfield.focus()

search_image_reference = search_image
search_icon_reference = search_icon

resized_image = img2.resize((30, 30), Image.ANTIALIAS)
resized_search_icon = ImageTk.PhotoImage(resized_image)

myimage_icon = Button(image=resized_search_icon, borderwidth=0, cursor="hand2", bg="#2E2E2E", command=getweather)
myimage_icon.place(x=310, y=45)

resized_image1 = img4.resize((170, 170), Image.ANTIALIAS)
resized_logo_icon = ImageTk.PhotoImage(resized_image1)

logo = Label(image=resized_logo_icon)
logo.place(x=200, y=100)

resized_image2 = img3.resize((600, 100), Image.ANTIALIAS)
resized_box_img = ImageTk.PhotoImage(resized_image2)

frame_myimg = Label(image=resized_box_img)
frame_myimg.pack(padx=5, pady=5, side=BOTTOM)

name= Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

label1 = Label(root, text="WIND", font=("Helvetica", 10, "bold"), fg="white", bg="#0CC0DF")
label1.place(x=85, y=307)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 10, "bold"), fg="white", bg="#0CC0DF")
label2.place(x=210, y=307)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 10, "bold"), fg="white", bg="#0CC0DF")
label3.place(x=360, y=307)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 10, "bold"), fg="white", bg="#0CC0DF")
label4.place(x=545, y=307)

t = Label(font=("arial", 70, "bold"), fg="#0CC0DF")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#0CC0DF")
w.place(x=90, y=325)
h = Label(text="...", font=("arial", 20, "bold"), bg="#0CC0DF")
h.place(x=225, y=325)
d = Label(text="...", font=("arial", 20, "bold"), bg="#0CC0DF")
d.place(x=385, y=325)
p = Label(text="...", font=("arial", 20, "bold"), bg="#0CC0DF")
p.place(x=565, y=325)

root.mainloop()
