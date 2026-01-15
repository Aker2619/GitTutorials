import pyttsx3

name = "Alonza"
names = ["Alonza", "John", "Micheal", "Kelly", "Marlon"]

for name in names:
    engine = pyttsx3.init()
    greeting = f"Hello, {name}!"
    print(greeting)
    engine.say(greeting)
    engine.runAndWait()
    engine.stop()
