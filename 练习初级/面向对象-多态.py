class dongwu:
    def speak(self):
        pass
class Dog(dongwu):
    def speak(self):
        print("汪汪叫")
class Cat(dongwu):
    def speak(self):
        print("喵喵叫")


dog=Dog()
cat=Cat()

dongwu.speak(dog)#?????
dongwu.speak(cat)###????