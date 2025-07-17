"""
self keyword provides connection with the object
__init__ is the contructor method that is defining the initial attributes
"""


# class Araba:
#     def __init__(self, marka:str, model:str):
#         self.marka = marka
#         self.model = model

#     def bilgi(self):
#         print(f"Araba bilgisi {self.marka} {self.model}")

# araba1 = Araba("BMW", "A5")
# araba2 = Araba("Audi", "X3")

# araba1.bilgi()

# class Book1:
#     def __init__(self, author:str, book_name:str, pub_year:int):
#         self.author = author
#         self.book_name = book_name
#         self.pub_year = pub_year
    
#     # def info(self, pub_year=None):#info() waits for an argument if pub_year is not declared with 'None'
#     #     if pub_year == None:
#     #         pub_year = self.pub_year
#     #     print(f"{self.author} has published {self.book_name} in {pub_year}")
    
#     def info(self):
#         print(f"{self.author} has published {self.book_name} in {self.pub_year}")

# harry_potter = Book1("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
# harry_potter.info()


# class Book2:
#     def __init__(self, author:str, book_name:str, pub_year:int):
#         self.author = author
#         self.book_name = book_name
#         self.pub_year = pub_year
    
#     def __str__(self):
#         return f"{self.author} has published {self.book_name} in {self.pub_year}"

# print(harry_potter)

# defined object could be redesigned with eval(repl(obj))
# #if __repl__ defined in class, the class information of created object can be seen later 

"""
class Coffee_Machine:
    def __init__(self):
        self.status = "Ready"
        self.status_functions = {"Ready":self.to_infusion}
                                #  "Infusion":self.ended}
    
    def handle(self, command):
        handler = self.status_functions.get(self.status)
        if handler:
            handler(command)
        else:
            return "Unknown command"
        
    def to_infusion(self, command):
        if command == "start":
            self.status = "Infusion"
        else:
            return "Invalid command"
        
coffee = Coffee_Machine()
coffee.handle("start")
"""

"""
class KahveMakinesi:
    def __init__(self):
        self.durum = "hazir"
        self.durum_fonksiyonlari = {
            "hazir": self.hazir_durumu,
            "demleniyor": self.demleniyor_durumu,
            "hazir_bekliyor": self.hazir_bekliyor_durumu
        }

    def olay(self, komut):
        handler = self.durum_fonksiyonlari.get(self.durum)
        if handler:
            handler(komut)
        else:
            print(f"❓ Bilinmeyen durum: {self.durum}")

    def hazir_durumu(self, komut):
        if komut == "baslat":
            print("☕ Kahve demleniyor...")
            self.durum = "demleniyor"
        else:
            print("❌ Sadece 'baslat' komutu geçerli.")

    def demleniyor_durumu(self, komut):
        if komut == "tamam":
            print("✅ Kahve hazır, alınabilir.")
            self.durum = "hazir_bekliyor"
        else:
            print("❌ Sadece 'tamam' komutu geçerli.")

    def hazir_bekliyor_durumu(self, komut):
        if komut == "al":
            print("🎉 Afiyet olsun! Yeni kahve için hazır.")
            self.durum = "hazir"
        else:
            print("❌ Sadece 'al' komutu geçerli.")

    def durum_ver(self):
        print(f"🔄 Şu anki durum: {self.durum}")

makine = KahveMakinesi()
makine.durum_ver()
makine.olay("baslat")
makine.olay("tamam")
makine.olay("al")
       
"""

"""
#state chain
class State:
    def handle(self, machine, cmd):
        raise NotImplementedError

class Ready(State):
    def handle(self, machine, cmd):
        if cmd == "start":
            print("☕ Coffee is preparing...")
            machine.durum = Infusion()
        else:
            print("❌ You can command 'start' in this situation.")

class Infusion(State):
    def handle(self, machine, cmd):
        if cmd == "okay":
            print("✅ Coffee is ready to take.")
            machine.durum = Waiting()
        else:
            print("❌ You can command 'okay' in this situation.")


class Waiting(State):
    def handle(self, machine, cmd):
        if cmd == "take":
            print("🎉 Bona apetite.")
            machine.durum = Ready()
        else:
            print("❌ You can command 'take' in this situation.")

class CoffeMachine:
    def __init__(self):
        self.durum = Ready()

    def init(self, cmd):
        self.durum.handle(self, cmd)

coffee = CoffeMachine()
coffee.init("start")
coffee.init("okay")
coffee.init("take")
"""

"""
from transitions import Machine

class KahveMakinesi:
    def __init__(self):
        self.durumlar = ['hazir', 'demleniyor', 'hazir_bekliyor']
        self.gecisler = [
            {'trigger': 'baslat', 'source': 'hazir', 'dest': 'demleniyor'},
            {'trigger': 'tamamla', 'source': 'demleniyor', 'dest': 'hazir_bekliyor'},
            {'trigger': 'al', 'source': 'hazir_bekliyor', 'dest': 'hazir'}
        ]

        self.makine = Machine(model=self, 
                              states=self.durumlar, 
                              transitions=self.gecisler, 
                              initial='hazir')

    def durum_ver(self):
        print(f"🔄 Şu anki durum: {self.state}")

makine = KahveMakinesi()

makine.durum_ver()     # 🔄 Şu anki durum: hazir
makine.baslat()        # hazir → demleniyor
makine.durum_ver()     # 🔄 Şu anki durum: demleniyor
makine.tamamla()       # demleniyor → hazir_bekliyor
makine.al()            # hazir_bekliyor → hazir
"""

"""
class KahveMakinesi:
    def __init__(self):
        self.durum = "Hazır"

        # Geçiş tablosu: (mevcut_durum, komut): (yeni_durum, çıktı)
        self.gecis_haritasi = {
            ("Hazır", "baslat"): ("Demleniyor", "☕ Kahve demleniyor..."),
            ("Demleniyor", "tamam"): ("HazırBekliyor", "✅ Kahve hazır, lütfen alın."),
            ("HazırBekliyor", "al"): ("Hazır", "🎉 Afiyet olsun! Yeni kahve yapılabilir.")
        }

    def olay(self, komut):
        anahtar = (self.durum, komut)
        if anahtar in self.gecis_haritasi:
            yeni_durum, mesaj = self.gecis_haritasi[anahtar]
            self.durum = yeni_durum
            print(mesaj)
        else:
            print(f"❌ '{komut}' komutu '{self.durum}' durumunda geçerli değil.")

    def durum_ver(self):
        print(f"🔄 Şu anki durum: {self.durum}")

makine = KahveMakinesi()
makine.durum_ver()
makine.olay("baslat")
makine.olay("tamam")
makine.olay("al")
"""