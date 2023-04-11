
#classlar-start

#scenario1

class Human:
    def talk(self):
        #class içerisinde fonksiyon kullanıyorsak bir parametre kullanmalıyız.(genellikle bu self olur.)
        print("Human is talking..")
    def walk(self):
        print("Human is walking..")

#instance=örnek
human1=Human()
human1.talk()
human1.walk()

#scenario-2

class Human:
    def talk(self,sentence): #self parametresi reserve bir parametre.Reserveyi yokmuş gibi algıladı ve sentence a atadı.
        #class içerisinde fonksiyon kullanıyorsak bir parametre kullanmalıyız.(genellikle bu self olur.)
        print(f"Human:{sentence}")
    def walk(self):
        print("Human is walking..")

#instance=örnek
human1=Human()
human1.talk("Merhaba")
human1.walk()

#scenario-3

class Human:
    name="Ezgi"
    def talk(self,sentence,name): #self parametresi reserve bir parametre.Reserveyi yokmuş gibi algıladı ve sentence a atadı.
        #class içerisinde fonksiyon kullanıyorsak bir parametre kullanmalıyız.(genellikle bu self olur.)
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walking")

#instance=örnek
human1=Human()
human1.name="Mehmet"
human1.talk("Merhaba","Samet")
human1.walk()

human2=Human()
human2.name="Nur"
human2.talk("Selam","Mevlüt")
human2.walk()

#scenario-4

class Human:
    name="Ezgi"
    def talk(self,sentence): #self parametresi reserve bir parametre.Reserveyi yokmuş gibi algıladı ve sentence a atadı.
        #class içerisinde fonksiyon kullanıyorsak bir parametre kullanmalıyız.(genellikle bu self olur.)
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walking")

#instance=örnek
human1=Human()
human1.name="Mehmet"
human1.talk("Merhaba")
human1.walk()

human2=Human()
#human2.name="Nur"(buradaki alanı silersek default olarak name="ezgi" gelir)
human2.talk("Selam")
human2.walk()

#scenario-5
#built-in hazır fonksiyonu
#constructor
class Human:
    name="Ezgi"
    def __init__(self):
        print("Bir human instance'i üretildi")
    def talk(self,sentence): #self parametresi reserve bir parametre.Reserveyi yokmuş gibi algıladı ve sentence a atadı.
        #class içerisinde fonksiyon kullanıyorsak bir parametre kullanmalıyız.(genellikle bu self olur.)
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walking")

#instance=örnek
human1=Human()
human1.name="Mehmet"
human1.talk("Merhaba")
human1.walk()

human2=Human()
#human2.name="Nur"(buradaki alanı silersek default olarak name="ezgi" gelir)
human2.talk("Selam")
human2.walk()

#scenario-6

class Human:
    def __init__(self,name):
        self.name=name
        print("Bir human instance'i üretildi")
    def__str__(self)
        return f"STR fonksiyonundan dönen değer:{self.name}"
    def talk(self,sentence): #self parametresi reserve bir parametre.Reserveyi yokmuş gibi algıladı ve sentence a atadı.
        #class içerisinde fonksiyon kullanıyorsak bir parametre kullanmalıyız.(genellikle bu self olur.)
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walking")

#instance=örnek
human1=Human()
human1.name="Mehmet"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2=Human()
#human2.name="Nur"(buradaki alanı silersek default olarak name="ezgi" gelir)
human2.talk("Selam")
human2.walk()
print(human2)

#classlar-end