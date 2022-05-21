import eel
import pyowm

# api ключ
owm = pyowm.OWM("***")


@eel.expose
def get_weather(place):
    mrg = owm.weather_manager()

    observation = mrg.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return 'В городе ' + place + ' сейчас ' + str(temp) + ' градусов!'


eel.init("web")
eel.start('main.html', size=(700, 700))
