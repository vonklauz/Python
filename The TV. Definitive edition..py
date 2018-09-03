#симулятор телевизора(почти)

class Zombiebox(object):
    """Виртуальный телевизор"""
    def __init__(self,  channel=0  , volume=0 ):
        
        self.volume = volume
        self.channel = channel

    def channels(self, choice_to_watch = None):
        try:
            self.channel = ["Вечно не работающий канал","Пропаганда киселёва","Пропаганда госдепа","Либеральная пропаганда","Иллюминаты и жидомасоны","Т(лишняя хромосома)НТ-ТВ","Вырвиглаз-ТВ(российский футбол 24x7!)","Страх и ненависть в Тропарёво(21+)","Канал, запрещённый в РФ","Канал, на который всем насрать"]
            print("Доступен следующий список каналов(всего 10): ")
            print(self.channel[0:3])
            print(self.channel[3:7])
            print(self.channel[7:10])
            choice_to_watch = int(input("Выберите канал: "))
            print("Вы включили канал: ", self.channel[choice_to_watch])
            self.channel = self.channel[choice_to_watch]
        except (ValueError, IndexError):
            if choice_to_watch not in range(0 , 10):
                print("У телевизора нет канала под этой цифрой! Пожалуйста, выберите канал из доступного диапазона.")
                choice_to_watch = 0
                self.channel = self.channel[choice_to_watch]
          
        

    def sound(self, regulir = None):
        regulir = input("Введите + или - для увеличения\уменьшения громкости: ")
        if regulir == "-":
            self.volume -= 1
            if self.volume <0:
                print("Вы полностью выключили звук")
                self.volume = 0
        elif regulir == "+":
            self.volume += 1
            if self.volume > 15:
                print("Вы включили максимальную громкость")
                self.volume = 15
        else:
            print("Такой кнопки нет")
            regulir = input("Введите + или - для увеличения\уменьшения громкости: ")
        

    def __str__(self):
        rep = "На данный момент у вас включён: " +str(self.channel) +".\n"
        rep += "Уровень громкости телевизора сейчас составляет: " +str(self.volume) +" единиц."
        return rep

def main_part():
    print("Вы включили телевизор")
    zombiebox_name = input("Кстати, какая марка у вашего телевизора? ")
    if zombiebox_name == "":
        print("Так и скажите, что китайский")
    tvisor = Zombiebox(zombiebox_name)
    turn = None
    while turn != "0":
        print \
        ("""
         Симулятор телевизора
         0 - Выключить
         1 - Выбрать канал
         2 - Изменить громкость
         3 - Узнать, какой канал и громкость на данный момент
         """)
        turn = input("Ваш выбор: ")
        if turn == "1":
            tvisor.channels()
        elif turn == "2":
            tvisor.sound()
        elif turn == "3":
            print(tvisor)
        elif turn == "0":
            print("Выключение...")
        else:
            print("В меню нет такого пункта")


main_part()
input("Press Enter key to exit")



            
            
    
    

    
        

        
