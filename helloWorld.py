import subprocess

name = "Alonza"
names = ["Alonza", "John", "Micheal", "Kelly", "Marlon"]
sayNames = False

if sayNames:
    for name in names:
        greeting = f"Hello, {name}!"
        print(greeting)
        subprocess.run(["say", greeting])

stoneSoupStory = """
A hungry traveler arrived at a village with nothing but an empty pot.
He filled it with water, dropped in a stone, and began to boil it.
Curious villagers asked what he was making. Stone soup, he said, but it needs a little garnish.
One by one, villagers contributed carrots, potatoes, meat, and spices.
Soon, a delicious soup was ready for everyone to share.
The traveler taught them that by working together, they could create something wonderful from nothing.
"""

voice = "Alex"

print(stoneSoupStory)
subprocess.run(["say", "-v", voice, stoneSoupStory])
