# Name : Imtiaz Adar
# Project Name : Weather App
# Phone : +8801778767775

import requests, datetime
from tkinter import Tk, Label, Entry, StringVar, Button
from time import strftime

class Weather:
    # Constructor
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x700+400+50')
        self.root.title('Weather Application - Imtiaz Adar')
        self.root.resizable(0, 0)
        self.root.iconbitmap('cloudy2.ico')
        self.root.configure(background="#202020")
        # Text Entry
        self.city_name = Entry(self.root, textvariable=None, bg='white', width=30, cursor='spider',
                        borderwidth=5, font='ds-digital 20 bold', justify='left')
        self.city_name.place(x=20, y=12)
        # Buttons
        self.weatherbutton = Button(self.root, text='Check Weather', bg="#660033", fg="white",
                        font=("ds-digital", 20, "bold"),
                        activebackground='white', activeforeground="#660033", cursor='spider', bd=2,
                        command=lambda: self.extract_weather())
        self.weatherbutton.place(x=480, y=10)
        self.checkanother = Button(self.root, text='Check Another', bg="#003333", fg="white",
                        font=("ds-digital", 20, "bold"),
                        activebackground='white', activeforeground="#003333", cursor='spider', bd=2,
                        command=lambda: self.check_another())
        self.checkanother.place(x=480, y=60)
        # Labels
        self.introLabel = Label(self.root, text='WEATHER APP BY IMTIAZ ADAR', fg='cyan', bg='#202020',
                        font=('ds-digital', 20, 'bold'), anchor='center')
        self.introLabel.place(x=190, y=640)
        self.clLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'), anchor='center')
        self.clLabel.place(x=12, y=100)
        self.celLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.celLabel.place(x=12, y=150)
        self.flLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.flLabel.place(x=12, y=200)
        self.hLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.hLabel.place(x=12, y=250)
        self.minLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.minLabel.place(x=12, y=300)
        self.maxLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.maxLabel.place(x=12, y=350)
        self.wLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.wLabel.place(x=12, y=400)
        self.wdLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.wdLabel.place(x=12, y=450)
        self.sunrLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.sunrLabel.place(x=12, y=500)
        self.sunsLabel = Label(self.root, text='', fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.sunsLabel.place(x=12, y=550)
        # Run
        self.root.mainloop()

    # Normalize All Texts
    def normalize(self):
        self.city_name.delete(0, len(self.city_name.get()))
        self.clLabel.configure(text='')
        self.celLabel.configure(text='')
        self.flLabel.configure(text='')
        self.hLabel.configure(text='')
        self.minLabel.configure(text='')
        self.maxLabel.configure(text='')
        self.wLabel.configure(text='')
        self.wdLabel.configure(text='')
        self.sunrLabel.configure(text='')
        self.sunsLabel.configure(text='')

    # Check Another Button
    def check_another(self):
        self.normalize()

    # Extract Weather
    def extract_weather(self):
        # print(self.city_name.get())
        # print(type(self.city_name.get()))
        # clLabel, celLabel, flLabel, hLabel, minLabel, maxLabel, wLabel, wdLabel, sunrLabel, sunsLevel
        api_link = f'https://api.api-ninjas.com/v1/weather?city={self.city_name.get()}'
        check_response = requests.get(api_link, headers={'X-Api-Key': 'KWnXN4S78zGjMzmnYgP0qQ==9nAv3HfgMvYnjefF'})
        if requests.codes.ok == check_response.status_code:
            self.print_informations(check_response.text)
        else:
            print("City Not Found !!")

    # Print Or Visualize The Informations
    def print_informations(self, text):
        chars = ['{', '}', '"', ':', ' ', 'cloud_pct', 'temp', 'feels_like', 'humidity', 'min_temp', 'max_temp',
                 'wind_speed', 'wind_degrees', 'sunrise', 'sunset']
        print('\nWEATHER OF {}'.format(self.city_name.get().upper()))
        for ch in chars:
            if ch in text:
                text = text.replace(ch, '')
        condition_list = text.split(',')

        dic = {}
        dic['Cloud Cover Percentage'] = condition_list[0] + '%'
        dic['Temperature'] = condition_list[1] + ' Degree Celsius'
        dic['Feels Like'] = condition_list[2] + ' Degree Celsius'
        dic['Humidity'] = condition_list[3] + ' Degree Celsius'
        dic['Minimum Temperature'] = condition_list[4].replace('min_', '') + ' Degree Celsius'
        dic['Maximum Temperature'] = condition_list[5].replace('max_', '') + ' Degree Celsius'
        dic['Wind Speed'] = condition_list[6]
        dic['Wind Degrees'] = condition_list[7] + ' Degrees'
        dic['Sunrise Time'] = datetime.datetime.fromtimestamp(int(condition_list[8])).strftime("%I:%M:%S %p")
        dic['Sunset Time'] = datetime.datetime.fromtimestamp(int(condition_list[9])).strftime("%I:%M:%S %p")
        # clLabel, celLabel, flLabel, hLabel, minLabel, maxLabel, wLabel, wdLabel, sunrLabel, sunsLevel

        self.clLabel = Label(self.root, text='Cloud Cover Percentage -> ' + dic['Cloud Cover Percentage'], fg='cyan', bg='#202020',
                         font=('ds-digital', 20, 'bold'), anchor='center')
        self.clLabel.place(x=12, y=100)
        self.celLabel = Label(self.root, text='Temperature -> ' + dic['Temperature'], fg='cyan', bg='#202020', font=('ds-digital', 20, 'bold'))
        self.celLabel.place(x=12, y=150)
        self.flLabel = Label(self.root, text='Feels Like -> ' + dic['Feels Like'], fg='cyan', bg='#202020',
                         font=('ds-digital', 20, 'bold'))
        self.flLabel.place(x=12, y=200)
        self.hLabel = Label(self.root, text='Humidity -> ' + dic['Humidity'], fg='cyan', bg='#202020',
                         font=('ds-digital', 20, 'bold'))
        self.hLabel.place(x=12, y=250)
        self.minLabel = Label(self.root, text='Minimum Temperature -> ' + dic['Minimum Temperature'], fg='cyan', bg='#202020',
                         font=('ds-digital', 20, 'bold'))
        self.minLabel.place(x=12, y=300)
        self.maxLabel = Label(self.root, text='Maximum Temperature -> ' + dic['Maximum Temperature'], fg='cyan', bg='#202020',
                         font=('ds-digital', 20, 'bold'))
        self.maxLabel.place(x=12, y=350)
        self.wLabel = Label(self.root, text='Wind Speed -> ' + dic['Wind Speed'], fg='cyan', bg='#202020',
                         font=('ds-digital', 20, 'bold'))
        self.wLabel.place(x=12, y=400)
        self.wdLabel = Label(self.root, text='Wind Degrees -> ' + dic['Wind Degrees'], fg='cyan', bg='#202020',
                       font=('ds-digital', 20, 'bold'))
        self.wdLabel.place(x=12, y=450)
        self.sunrLabel = Label(self.root, text='Sunrise Time -> ' + dic['Sunrise Time'], fg='cyan', bg='#202020',
                        font=('ds-digital', 20, 'bold'))
        self.sunrLabel.place(x=12, y=500)
        self.sunsLabel = Label(self.root, text='Sunset Time -> ' + dic['Sunset Time'], fg='cyan', bg='#202020',
                          font=('ds-digital', 20, 'bold'))
        self.sunsLabel.place(x=12, y=550)

        for condition, degrees in dic.items():
            print(f'{condition}: {degrees}')

# Main
if __name__ == '__main__':
    # city = input('Enter City Name : ')
    weather_class_object = Weather()