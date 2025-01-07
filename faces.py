#requesting a text inpur from user.
def main():
    text=input("write any text that includes :) or :( ")
    print("here is your text modified")
    facy(text)
#defining a function called "facy" that replaces any :) or :( with emojis.
def facy(t):
    t = t.replace(":)","🙂")
    t = t.replace(":(","🙁")
    print(t)
main()
