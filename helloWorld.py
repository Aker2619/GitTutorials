import pyttsx3

name = "Alonza"
names = ["Alonza", "John", "Micheal", "Kelly", "Marlon"]

engine = pyttsx3.init()

for name in names:
    greeting = f"Hello, {name}!"
    print(greeting)
    engine.say(greeting)
    engine.runAndWait()
