"""
Application: 
- Dynamic
- Real Time Update

Observer Design Pattern is a behavioral pattern that creates a one-to-many 
relationship between a subject and its observers. When the subject's state
changes, all dependent observers are notified and updated automatically, 
ensuring synchronized communication.

Enables automatic updates to multiple objects when one object changes.
Promotes loose coupling between the subject and its observers.
Useful for implementing event-driven or publish-subscribe systems.
"""

from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self,weather:str):
        pass

class Subject(ABC):
    @abstractmethod
    def add_observer(self,observer:Observer):
        pass

    @abstractmethod
    def remove_observer(self,observer:Observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

class WeatherStation(Subject):
    def __init__(self):
        self.observers: List[Observer]=[]
        self.weather=""

    def add_observer(self,observer:Observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer:Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.weather)
            
    def set_weather(self, new_weather: str):
        self.weather = new_weather
        self.notify_observers()

class PhoneDisplay(Observer):
    def __init__(self):
        self.weather=""
    
    def update(self,weather:str):
        self.weather=weather
        self.display()

    def display(self):
        print(f'Phone Display: Weather updated - {self.weather}')

class TvDisplay(Observer):
    def __init__(self):
        self.weather=""
    
    def update(self,weather:str):
        self.weather=weather
        self.display()

    def display(self):
        print(f'Tv Display: Weather updated - {self.weather}')

if __name__=="__main__":
    weather_station=WeatherStation()

    phone_display=PhoneDisplay()
    tv_display=TvDisplay()

    weather_station.add_observer(phone_display)
    weather_station.add_observer(tv_display)

    weather_station.set_weather('Sunny')



