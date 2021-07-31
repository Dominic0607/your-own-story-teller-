from tkinter import *
from tkinter import messagebox
import random
import pyttsx3
root = Tk()


def myClick():


    if len(e1.get()) == 0:
        messagebox.showwarning("Story Generator", "Noun field empty")
    if len(e2.get()) == 0:
        messagebox.showwarning("Story Generator", "Adjective field empty")

    if len(e1.get()) != 0:
        k = random.randint(1, 2)
        k2 = str(random.randint(1, 8))

        Noun = ["is a good person ", "is a brave person ", "lives in New Delhi ", "lives in Bihar ", "lives in Shimla "]

        Setup = ["There was a cruel Ork King", "A Red dragon was terrorizing the kingdom",
                 "A princess was trapped in magical kingdom by a Red Dragon",
                 "The enemy of Orks were at kingdom's door", "The kings army were desperate for a hope!",
                 "Kingdom was fighting a loosing battle"]

        Noun2 = {
            "1": " struggling to get by ",
            "2": " the proud owner of a small textile mill ",
            "3": " who worked as a small tailor ",
            "4": " tending to his farm ",
            "5": " a common man ",
            "6": " and was a successful student ",
            "7": " a middle class salaryman ",
            "8": " a son to a small bussinessman "
        }

        Noun3 = {
            "1": " but on a quest to become the richest person!",
            "2": " and on a quest to save their village against drought",
            "3": " on an impossible mission of getting her daughter into a college",
            "4": " However on a mission of getting the dam built for their village",
            "5": " with a buring desire to become a highly respectable memeber of the society",
            "6": " with a goal of becoming successful in life!",
            "7": " with a deep desire of breakingfree from his monotonous job and finally travel the world!",
            "8": " hoping to open his own bussiness one day"
        }

    if k == 2 and len(e2.get()) != 0:
        ran1= random.choice(Setup)
        myLabel4 = Label(root, text="Once upon a time, " + ran1 + " and " + e1.get() + Noun2[
            k2] + "magically summoned to the rescue!",font = "Times 16 italic")
        myLabel4.pack()
        txt = ["Once upon a time, " + ran1 + " and " + e1.get() + Noun2[
            k2] + "magically summoned to the rescue!"]




    if k == 1 and len(e2.get()) != 0:
        myLabel4 = Label(root, text=e1.get() + " " + Noun[k] + Noun2[
            k2] + "Suddenly, all went away when they were summoned to the magical kingdom!",font = "Times 16 italic")
        myLabel4.pack()
        txt=[e1.get() + " " + Noun[k] + Noun2[k2] + "Suddenly, all went away when they were summoned to the magical kingdom!"]





    if len(e2.get()) == 0:
        myLabel4 = Label(root, text=e1.get() + " " + Noun[k] + Noun2[k2] + Noun3[
            k2] + ". All was changed forever when they won a lottery worth crores!",font = "Times 16 italic")
        myLabel4.pack()
        txt=[e1.get() + " " + Noun[k] + Noun2[k2] + Noun3[
            k2] + ". All was changed forever when they won a lottery worth crores!"]






    if k > 0:
        Adjective = ["However didnt let go of their ", "was great confusion and they let go of ",
                     " were mesmerised and felt ", " However felt nothing like a hero should, "]



    # monologue

    if k > 0 and len(e2.get()) != 0:
        MonologueIntro = ["Upon reaching the kingdom, ", "Upon reaching the kingdom's court, ",
                          "Upon being summoned to the kingdom, ",
                          "Upon being summoned in the middle of dark winter night to the kingdom, ",
                          "Upon being summoned to the kingdom's church ",
                          "It was warm sunny morning when our hero appeared ",
                          "Warm sun shinning on the vast green grassland when our hero touched the soil of magic kingdom the first time"]

        MonologueResponsible = ["The King was thrilled.", "The King's Court was thrilled.",
                                "The King Kingdom was filled with up hope.",
                                "The king asked them to help them with fighting the dragon.",
                                "The King pleaded them to join them in conquest against the dragon.",
                                "The Kingdom was rejoyed with arrival of the new hero.",
                                "Suddenly the whole kingdom was filled with joy for now they had a fighting chance"]

        MonologueHero = ["To be the hero of the story,", "The hero of our story,", "Once a common mam now hero,",
                         "Our hero,", " Magic Kingdom last hero", ]

        MonologueFight = ["went into the deep redwood forest", "Our hero went deep to save the day",
                          "Charged the battle that was knocking at the kingdom's door",
                          "Our now hero listening to the problem found the courage and charged the battle!",
                          "Our hero went out to the battle on the Great Mount Volca",
                          "Our common man now hero lead the kingdom army to the warfield of King Doom",
                          "air was warm and night dark but hero feared none and charged the Dargon Mount"]

        MonologueEnd = ["Hero passing through dense kingdom forest to the battlefield was suddenly attacked",
                        "Suddenly the hero was attacked by magic casters with fireballs",
                        "The oracks surrounded our hero", "The dragon flew over our hero",
                        "Enemies hidden in thick forest surrounded our hero passing by to the battlefield",
                        "enemies arhers shot some arrows at our hero",
                        "Our hero party shot their warning shot at the dragon lair"]

        MonologueEnd1 = ["Our hero fought bravely and was victorious", "Our hero at the end saved this kingdom",
                         "Our hero fought the war and kingdom was saved",
                         "Everyone was happy when out hero returned from the conquest victorious!"]

        ran2=random.choice(MonologueIntro)
        ran3=random.choice(MonologueResponsible)
        ran4=random.choice(Adjective)

        myLabel5 = Label(root, text=ran2 + " " + ran3,font = "Times 16 italic")
        myLabel5.pack()
        txt2=[ran2 + " " + ran3]

        myLabel5 = Label(root, text=e1.get() + " " + ran4 + e2.get() + " in their heart",font = "Times 16 italic")
        myLabel5.pack()
        txt3=[e1.get() + " " + ran4 + e2.get() + " in their heart"]


        ran5 = random.choice(MonologueHero)
        ran6 = random.choice(MonologueFight)
        ran7 = random.choice(MonologueEnd)
        ran8 = random.choice(MonologueEnd1)
        myLabel6 = Label(root, text=ran5 + " " + ran6,font = "Times 16 italic")
        myLabel6.pack()

        myLabel6 = Label(root, text=ran7,font = "Times 16 italic")
        myLabel6.pack()

        myLabel6 = Label(root, text=ran8,font = "Times 16 italic")
        myLabel6.pack()
        txt4=[ran5 + " " + ran6+" "+ran7+" " + ran8]

        speaker = pyttsx3.init()
        speaker.say ("Welcome to Your Own Story Teller")
        speaker.say(txt)
        speaker.say(txt2)
        speaker.say(txt3)
        speaker.say(txt4)
        speaker.runAndWait()

        myLabel6 = Label(root, text="x---------x",font = "Times 18 bold")
        myLabel6.pack()



myLabel1 = Label(root, text="YOUR OWN STORY TELLER!",fg = "red",
		 font = "Times 24 bold")
myLabel1.pack()

myLabel2 = Label(root, text="Enter a Character Name",fg = "blue",
		 font = "Times 18 bold")
myLabel2.pack()

e1 = Entry(root, width=24)
e1.pack()

myLabel3 = Label(root, text="Enter an Character Trait",fg = "blue",
		 font = "Times 18 bold")
myLabel3.pack()

e2 = Entry(root, width=24)
e2.pack()

myButton = Button(root, text="GENERATE",fg = "orange",
		 font = "Times 18 bold", command=myClick)
myButton.pack()

myLabel1.pack(padx=(30), pady=(20))
myLabel2.pack(padx=(30), pady=(5))
myLabel3.pack(padx=(30), pady=(5))
myButton.pack(padx=(30), pady=(20))

root.configure(bg='green')


root.mainloop()