import time
from typing import Dict

class FlashlightController:
    def __init__(self):
        # Таблица кодов Морзе
        self.morseCode: Dict[str, str] = {
            'S': "...",
            'O': "---"
        }

    def sendMorseMessage(self, message: str) -> None:
        """Метод для передачи сообщения в коде Морзе"""
        for char in message.upper():
            if char in self.morseCode:
                self.sendMorseSymbol(self.morseCode[char])
                self.pause(2000)  # Пауза между буквами

    def sendMorseSymbol(self, symbol: str) -> None:
        """Метод для передачи последовательности точек и тире"""
        for char in symbol:
            if char == '.':
                self.dot()
            elif char == '-':
                self.dash()
            self.pause(300)  # Пауза между элементами символа

    def dot(self) -> None:
        """Включает фонарь на 350 мс"""
        self.turnOn(350)

    def dash(self) -> None:
        """Включает фонарь на 1000 мс"""
        self.turnOn(1000)

    def turnOn(self, duration: int) -> None:
        """Включает фонарь, ждёт указанное время и затем выключает фонарь"""
        workshop.turnLightOn()
        time.sleep(duration / 1000)  # Конвертируем миллисекунды в секунды
        workshop.turnLightOff()

    def pause(self, duration: int) -> None:
        """Метод для паузы. Duration — длительность паузы"""
        time.sleep(duration / 1000)  # Конвертируем миллисекунды в секунды

flashlight = FlashlightController()
flashlight.sendMorseMessage("SOS")
