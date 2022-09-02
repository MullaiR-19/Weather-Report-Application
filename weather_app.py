from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    status.configure(text = "Searching...........")
    
    city=city.replace(" ","+")
    
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google......\n")
    try:
        soup = BeautifulSoup(res.text,'html.parser')   
        location = soup.select('#wob_loc')[0].getText().strip()  
        time = soup.select('#wob_dts')[0].getText().strip()       
        info = soup.select('#wob_dc')[0].getText().strip() 
        weather = soup.select('#wob_tm')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
    except:
        status.configure(text = "City or Place not Found")    
    
    print(location)
    print(time)
    print(info)
    print(weather+"°C")
    print(humidity)

    status.configure(text="")
    
    weather_status = 'Location: '+location+'\n'+'Time: '+time+'\n'+'Forcast: '+info+'\n'+'Temperature: '+weather+'°C\n'+'Humidity: '+humidity
    messagebox.showinfo("Weather Status", weather_status)
    status.config(text = "Search More!")

    

def search():
    city= text_box.get()
    city=city+" weather"
    weather(city)

win = Tk()
win.geometry('360x180')
win.resizable(0,0)
win.title('Weather Station')
win.config(bg='gray')

heading = Label(win, text = 'Local Weather Station',font = ("Times New Roman", 14,"bold"), fg = 'magenta',bg='#444444',width=40,height=2)
heading.place(relx = .5, rely = .13, anchor=CENTER)

text_box = Entry(win, font=('Times New Roman', 12),justify='center', width = 30)
text_box.place(relx=.5, rely=.4, anchor=CENTER)

search_button = Button(win, text="Search",font=('Times New Roman', 12), command=search, bg = '#aaffaa', height=1,width=10)
search_button.place(relx=.5, rely=.65, anchor=CENTER)

status = Label(win, text = "",font=('Times New Roman', 12), bg = 'gray',fg='Black')
status.place(relx=.5,rely=.8,anchor=CENTER)

version_spe = Label(win, text = "Version 1.0.1",bg = 'gray',fg='white').place(relx=.5,rely=.95,anchor=CENTER)
