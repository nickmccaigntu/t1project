import pickle
import Const
import tkinter as tk
class Player():
    def __init__(self,name,inventory, pets = [], balance = 1000):
        self._name = name
        self._pets = pets
        self._inventory = inventory
        self._balance = balance
    def newPet(self, name):
        self._pets.append(Pet(name))
class Compets():
    def __init__(self, pets = []):
        self.pets = pets
    def addPet(self,pet):
        self.pets.append(pet)
class Pet():
    species = 'Doggo'
    def __init__(self, name, speed = 1, strength = 1, endurance = 1, hunger = 50, thirst = 50, joy = 50):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst
        self.joy = joy 
        self.speed = speed
        self.strength = strength
        self.endurance = endurance
    def __pass_time(self):
        self.hunger += 1
        self.thirst += 1
        self.joy += 1
    ### Maintaince ###
    # automatic quality is 3 unless user uses a item to improve
    def drink(self, quality = 3):
        self.thirst -= quality
        if self.thirst <= 0:
            self.thirst = 0
        else:
            self.__pass_time()
    def eat(self,quality  = 3):
        self.hunger -= quality
        if self.hunger <= 0:
            self.hunger = 0
        else:
            self.__pass_time()
    def play(self, quality = 3):
        self.joy -= quality
        if self.joy <= 0:
            self.joy = 0
        else:
            self.__pass_time()
    def trainSpeed(self, improvment):
        self.speed += improvment
        if self.speed > 50:
            self.speed = 50
        else:
            self.hunger += 15
            self.thirst += 15
            self.joy += 15
    def trainStrength(self, improvment):
        self.strength += improvment
        if self.strength > 50:
            self.strength = 50
        else:
            self.hunger += 15
            self.thirst += 15
            self.joy += 15
    def trainEndurance(self, improvment):
        self.endurance += improvment
        if self.endurance > 50:
            self.endurance = 50
        else:
            self.hunger += 15
            self.thirst += 15
            self.joy += 15 
    def compete(self):
        self.hunger += 15
        self.thirst += 15
        self.joy += 15          
    @property
    def checkAble(self):
        if self.hunger >= 90:
            return False
        elif self.thirst >= 90:
            return False
        elif self.joy >= 90:
            return False
        return True

class Item():
    def __init__(self,name,itype,quality,price):
        self.name = name
        self.itype = itype
        self.quality = quality
        self.price = price
class Inventory():
    def __init__(self, name):
        self.name = name
        self.inven = []
    def addItem(self,item):
        if item in self.inven:
            return False
        else:
            self.inven.append(item)
            return True
    def delItem(self,item):
        if item in self.inven:
            self.inven.remove(item)
            return True
        else:
            return False
    def getItem(self, itemName):
        for itemx in self.inven:
            if itemName == itemx.name:
                return itemx
        return False
    def returnItems(self):
       return self.inven
    def getitemoftypes(self, type):
        items = []
        for i in self.inven:
            if i.itype == type:
                items.append(i)
        return items   
def getitemstypes(inven, type):
    items = []
    for i in inven.returnItems():
        if i.itype == type:
            items.append(i)
    return items
def pickitem(inven):
    itemList = []
    for i in inven:
        print(i.name)
        itemList.append(i)
    return itemList
def BuyItem(player, shopinv, item):
    try:
        playerinv = player._inventory
        player._balance -= item.price
        playerinv.addItem(item)
        shopinv.delItem(item)
        print("worked")
        return True
    except:
        return False
def windowselectpetlookafter(player):
    pets = player._pets
    rowx = 0
    colx = 0
    winselect = tk.Tk()
    winselect.title("Select pet")
    def startgui(petx):
        LookafterGUI(petx,player)
    for pet in pets:
        tk.Label(winselect, text = "PetName").grid(row = rowx, column = colx)
        tk.Label(winselect, text = pet.name).grid(row = rowx + 1, column = colx)
        petbtn = tk.Button(winselect, text = "Select me!", command = lambda: startgui(pet))
        petbtn.grid(row = rowx + 2 , column = colx)
        if colx == 0:
            colx = 1
        else:
            colx = 0
            rowx += 3  
def windowselectpettraining(player):
    pets = player._pets
    rowx = 0
    colx = 0
    winselect = tk.Tk()
    winselect.title("Select pet")
    for pet in pets:
        tk.Label(winselect, text = "PetName").grid(row = rowx, column = colx)
        tk.Label(winselect, text = pet.name).grid(row = rowx + 1, column = colx)
        tk.Button(winselect, text = "Select me!", command = lambda: traingui(pet, player)).grid(row = rowx + 2 , column = colx)
        if colx == 0:
            colx = 1
        else:
            colx = 0
            rowx += 3   
def savegamegui(player, shopinventory,):
    windowsave = tk.Tk()
    windowsave.title("Save")
    tk.Label(windowsave, text = "Save name:").grid(row = 0 , column = 0)
    filenameenty = tk.Entry(windowsave)
    filenameenty.grid(row = 1, column = 0)
    savebtn = tk.Button(windowsave, text= "Save", command = lambda: saveGame(player,shopinventory, filenameenty.get(),windowsave))
    savebtn.grid(row = 2, column = 0)  
def saveGame(player, shopinventory, filename, windowsave):
    filename = filename + ".dat"
    savefile = open(filename, "wb")
    pickle.dump(player, savefile)
    pickle.dump(shopinventory,savefile)
    savefile.close()
    windowsave.destroy()
def createpet(player):
    petName = input("Name for your pet? ")
    player.newPet(petName)
    print("Pet created.")
def LookafterGUI(pet,player):
    remove = []
    hunger = str(pet.hunger) + "/100"
    joy = str(pet.joy) + "/100"
    thirst = str(pet.thirst) + "/100"
    window = tk.Tk()
    window.title("Look After!")
    def testing(selected):
        if selected == "Feed":
            type = Const.Food
        elif selected == "Drink":
            type = Const.Water
        else:
            type = Const.Toy
        irow = 4
        icol = 0
        for itemx in remove:
            itemx.destroy()
        def objcts(qual, type):
            print(str(qual) + type)
            if type == Const.Food:
                pet.eat(qual)
            if type == Const.Water:
                pet.drink(qual)
            if type == Const.Toy:
                pet.play(qual)
            hunger = str(pet.hunger) + "/100"
            joy = str(pet.joy) + "/100"
            thirst = str(pet.thirst) + "/100"
            hungerlbl.config(text=str(hunger))
            joylbl.config(text=str(joy))
            thirstlbl.config(text=str(thirst))
        for item in player._inventory.getitemoftypes(type):
            namelbl = tk.Label(window, text = "Name:")
            namelbl.grid(row = irow, column = icol)
            remove.append(namelbl)
            quallbl = tk.Label(window, text = "qal:")
            quallbl.grid(row = irow + 1, column = icol)
            remove.append(quallbl)      
            icol += 1
            namelblc = tk.Label(window, text = item.name)
            namelblc.grid(row = irow, column = icol)
            remove.append(namelblc)
            quallblc = tk.Label(window, text = item.quality)
            quallblc.grid(row = irow +1, column = icol)
            remove.append(quallblc)
            btn = tk.Button(window, text = "Use me!", command =lambda: objcts(item.quality, item.itype))
            btn.grid(row = irow +2, column = icol, columnspan = 2)
            remove.append(btn)
            icol += 1
            if icol == 4:
                icol = 0
                irow += 3  
    tk.Label(window, text = "Pet-").grid(row = 0, column = 0)
    tk.Label(window, text = pet.name).grid(row = 0, column = 1)
    tk.Label(window,text = "Hunger:").grid(row = 0, column = 3)
    
    hungerlbl = tk.Label(window ,text = hunger)
    hungerlbl.grid(row = 0, column = 4)
    tk.Label(window,text = "Joy:").grid(row = 1, column = 0)
    joylbl = tk.Label(window,text = joy)
    joylbl.grid(row = 1, column = 1)
    tk.Label(window, text = "Thirst:").grid(row = 1, column = 3)
    thirstlbl = tk.Label(window,text = thirst)
    thirstlbl.grid(row = 1, column = 4)
    tk.Label(window,text = "Action:" ).grid(row = 3, column = 0)
    actbtn = tk.Button(window,
                    text = "Feed",
                    command =lambda: testing("Feed")
                    )
    actbtn.grid(row = 3, column = 1)
    actbtn2 = tk.Button(window,
                    text = "Drink",
                    command =lambda: testing("Drink")
                    )
    actbtn2.grid(row = 3, column = 2)
    actbtn3 = tk.Button(window,
                    text = "Play",
                    command =lambda: testing("Play")
                    )
    actbtn3.grid(row = 3, column = 3)
    window.mainloop()
def startwindow():
    windowstart = tk.Tk()
    windowstart.title("Start!")
    tk.Label(windowstart, text = "Welcome!").grid(row = 0, column = 0)
    newbtn = tk.Button(windowstart, text = "NewGame", command =lambda: newgamewindow(windowstart))
    newbtn.grid(row = 0, column = 1)
    tk.Label(windowstart, text ="File name:").grid(row = 1, column = 0)
    filenameent = tk.Entry(windowstart)
    filenameent.grid(row = 1, column = 1)
    opensavebtn = tk.Button(windowstart, text = "Continue!", command =lambda: opensave(filenameent.get()))
    opensavebtn.grid(row = 3, column = 0, columnspan = 2)
    windowstart.mainloop()
def createpetfun(player,name,windownewpet):
    player.newPet(name)
    windownewpet.destroy()
def traingui(pet, player):
    speed = str(pet.speed) + "/50"
    strength = str(pet.strength) + "/50"
    endurance = str(pet.endurance) + "/50"
    def speedaction():
        if pet.checkAble == True:
            pet.trainSpeed(3)
            speed = str(pet.speed) + "/50"
            strength = str(pet.strength) + "/50"
            endurance = str(pet.endurance) + "/50"
            speedlbl.config(text = speed)
            strengthlbl.config(text = strength)
            endurancelbl.config(text = endurance)
    def enduranceaction():
        if pet.checkAble == True:
            pet.trainEndurance(3)
            speed = str(pet.speed) + "/50"
            strength = str(pet.strength) + "/50"
            endurance = str(pet.endurance) + "/50"
            speedlbl.config(text = speed)
            strengthlbl.config(text = strength)
            endurancelbl.config(text = endurance)    
    def strengthaction():
        if pet.checkAble == True:
            pet.trainStrength(3)
            speed = str(pet.speed) + "/50"
            strength = str(pet.strength) + "/50"
            endurance = str(pet.endurance) + "/50"
            speedlbl.config(text = speed)
            strengthlbl.config(text = strength)
            endurancelbl.config(text = endurance)    
    window = tk.Tk()
    window.title("Train")
    tk.Label(window, text = "Pet").grid(row = 0, column = 0)
    namelbl = tk.Label(window, text = pet.name)
    namelbl.grid(row = 0, column = 1)
    tk.Label(window, text = "Speed").grid(row = 0, column = 2)
    speedlbl = tk.Label(window, text = speed)
    speedlbl.grid(row = 0, column = 3)
    tk.Label(window, text = "Endurance").grid(row = 1, column = 0)
    endurancelbl = tk.Label(window, text = endurance)
    endurancelbl.grid(row = 1, column = 1)
    tk.Label(window, text = "Strength").grid(row = 1, column = 2)
    strengthlbl = tk.Label(window, text = strength)
    strengthlbl.grid(row = 1, column = 3)
    actbtn =tk.Button(window,
                    text = "Endurance",
                    command = enduranceaction
                    )
    actbtn.grid(row = 3, column = 1)
    actbtn2 =tk.Button(window,
                    text = "Strength",
                    command = strengthaction
                    )
    actbtn2.grid(row = 3, column = 2)
    actbtn3 =tk.Button(window,
                    text = "Speed",
                    command = speedaction
                    )
    actbtn3.grid(row = 3, column = 3)
def createpetgui(player):
    windownewpet = tk.Tk()
    windownewpet.title("Create a new Pet!")
    tk.Label(windownewpet, text = "What would you like to name the pet?").grid(row = 0, column = 0)
    nameentry = tk.Entry(windownewpet)
    nameentry.grid(row = 1, column = 0)
    createpetbtn = tk.Button(windownewpet,text = "Create Pet", command =lambda: createpetfun(player, nameentry.get(),windownewpet))
    createpetbtn.grid(row = 2, column =0)
def competepets(player, Playerpet, comppet, skill):
    if skill == "Strength":
        playerscore = Playerpet.strength
        compscore = comppet.strength
    elif skill == "Speed":
        playerscore = Playerpet.speed
        compscore = comppet.speed
    else:
        playerscore = Playerpet.endurance
        compscore = comppet.endurance
    if Playerpet.checkAble == True:
        Playerpet.compete()
        if playerscore > compscore:
            return True
        elif compscore > playerscore:
            return False
        else:
            return "Draw"
def newgamewindow(oldwin):
    oldwin.destroy()
    windownewgame = tk.Tk()
    windownewgame.title("New game!")
    tk.Label(windownewgame, text = "What is your name:").grid(row = 0, column = 0)
    tk.Label(windownewgame, text = "Pet name:").grid(row = 1, column = 0)
    usernameentry = tk.Entry(windownewgame)
    usernameentry.grid(row = 0, column = 1)
    petnameentry = tk.Entry(windownewgame)
    petnameentry.grid(row = 1, column = 1)
    submitbtn = tk.Button(windownewgame, text = "Start!", command =lambda: newgame(usernameentry.get(), petnameentry.get(),windownewgame))
    submitbtn.grid(row = 2, column = 0, columnspan = 2)
    windownewgame.mainloop()
def competeGui(player, compets):
    window = tk.Tk()
    window.title("Compete")
    def fight(player, compets, winselec, type):
        try:
            for pet in player._pets:
                if pet.name == petname['text']:
                    petplayer = pet
            for pet in compets.pets:
                if pet.name == compname['text']:
                    petcomp = pet
            if type == "Strength":
                playerscorelbl.config(text = "You:" + str(petplayer.strength))
                compscorelbl.config( text = "Comp:" + str(petcomp.strength))
            elif type == "Speed":
                playerscorelbl.config(text = "You:" + str(petplayer.speed))
                compscorelbl.config( text = "Comp:" + str(petcomp.speed))
            else:
                playerscorelbl.config(text = "You:" + str(petplayer.endurance))
                compscorelbl.config( text = "Comp:" + str(petcomp.endurance))
            result = competepets(player,petplayer,petcomp, type)
            if result == True:
                resultlbl.config(text = "You Win!")
                player._balance += 200
                balancelbl.config(text = "Bal: " + str(player._balance))
            elif result == "Draw":
                resultlbl.config(text = "You Draw.")
            else:
                resultlbl.config(text = "You Lost.")
        except:
            resultlbl.config(text = "Please select the pets!")
    def getpet(pets, petname):
        winselec = tk.Tk()
        winselec.title("Select pet")
        listbox = tk.Listbox(winselec)
        listbox.grid(row = 0 , column = 0)
        startbtn = tk.Button(winselec, text = "Choose", command = lambda: returnpet(listbox.get(tk.ACTIVE),petname,winselec))
        startbtn.grid(row = 1, column = 0)
        for pet in pets:
            listbox.insert(tk.END, pet.name)
    def returnpet(petx,petname, window):
        petname.config(text = petx)
        window.destroy() 
    tk.Label(window, text = "Pet:").grid(row = 0, column = 0)
    petname = tk.Label(window, text = "Select one!")
    petname.grid(row = 0, column = 1)
    tk.Label(window, text = "Against:").grid(row = 0, column = 3)
    compname = tk.Label(window, text = "Select one!")
    compname.grid(row = 0, column = 4)
    petselectbtn = tk.Button(window, text = "Select", command = lambda: getpet(player._pets, petname))
    petselectbtn.grid(row = 1, column = 0, columnspan = 2)
    compselectbtn = tk.Button(window, text ="Select", command = lambda: getpet(compets.pets, compname))
    compselectbtn.grid(row = 1, column = 3, columnspan = 2) 
    tk.Label(window, text = "Compete in?").grid(row = 2, column = 0) 
    strengthbtn = tk.Button(window, text = "Strength", command = lambda: fight(player, compets, window, "Strength"))
    strengthbtn.grid(row = 2, column = 1)
    speedbtn = tk.Button(window, text = "Speed", command = lambda: fight(player, compets, window, "Speed"))
    speedbtn.grid(row = 2, column = 2)  
    endurancebtn = tk.Button(window, text = "Endurance", command = lambda: fight(player, compets, window, "Endurance"))
    endurancebtn.grid(row = 2, column = 3)
    playerscorelbl = tk.Label(window, text = "You: xx")
    playerscorelbl.grid(row = 3, column = 0, columnspan = 2)
    compscorelbl = tk.Label(window, text = "Comp: xx")
    compscorelbl.grid(row = 4, column = 0, columnspan = 2)
    resultlbl = tk.Label(window, text = "Begin above!")
    resultlbl.grid(row = 3, column = 2, columnspan = 2)
    balancelbl = tk.Label(window, text = "Bal: "+ str(player._balance))
    balancelbl.grid(row = 4, column = 2, columnspan =2)
def newgame(name, petName, oldwin):
    try:
        player = None
        #player inven
        inventory = Inventory("Player Inventory")
        for id, contents in Const.NewPlayerInv.items():
            inventory.addItem(Item(id,contents['itype'],contents['quality'],contents['price']))
        #player creation
        player = Player(name, inventory)
        # shop creation
        shopinventory = Inventory("Main store")
        for idx, contentsx in Const.NewStore.items():
            shopinventory.addItem(Item(idx,contentsx['itype'],contentsx['quality'],contentsx['price']))  
        player.newPet(petName)
        pet = player._pets[0]
        print(pet.__str__())
        compets = Compets()
        for idx, content in Const.CompPlayer.items():
            compets.addPet(Pet(idx,content['speed'],content['strength'],content['endurance']))
        oldwin.destroy()
        mainmenu(player, shopinventory, compets)
    except:
        print("No")
def mainmenu(player, shop, compets):
    windowmenu = tk.Tk()
    windowmenu.title("Main menu!")
    tk.Label(windowmenu, text = "Please select what you would like to do!").grid(row = 0, column = 0)
    trainbtn = tk.Button(windowmenu, text = "Train My pets", command = lambda: windowselectpettraining(player))
    trainbtn.grid(row = 1, column = 0)
    lookafterbtn = tk.Button(windowmenu,text = "Look after My pets", command = lambda: windowselectpetlookafter(player))
    lookafterbtn.grid(row = 2, column = 0)
    shopbtn = tk.Button(windowmenu, text = "Visit the shop!", command = lambda: shoppingGui(player,shop))
    shopbtn.grid(row = 3, column =  0)
    workbtn = tk.Button(windowmenu, text = "Go to work!", command = lambda: competeGui(player, compets))
    workbtn.grid(row = 4, column = 0)
    newpetbtn = tk.Button(windowmenu, text = "New pet", command = lambda: createpetgui(player))
    newpetbtn.grid(row = 5, column = 0)
    savebtn = tk.Button(windowmenu, text = "SAVE", command = lambda: savegamegui(player,shop))
    savebtn.grid(row = 6, column = 0)
def shoppingGui(player, shop):
    list = pickitem(shop.inven)
    window = tk.Tk()
    window.title("STORE!")
    tk.Label(window, text = "Welcome to the store please buy anything you would like!").grid(row = 0, column = 0, columnspan = 4)
    tk.Label(window, text = "Bal:").grid(row = 0, column = 5)
    ballbl = tk.Label(window, text = str(player._balance))
    ballbl.grid(row = 0, column = 6)
    rowx = 2
    colx = 0
    def buyitem(item, player, shop):
        BuyItem(player, shop, item)
        window.destroy()
    for item in list:
        tk.Label(window, text ="Name:").grid(row  = rowx, column = colx)
        tk.Label(window, text = item.name).grid(row = rowx, column = colx + 1)
        tk.Label(window, text ="Quality:").grid(row  = rowx + 1, column = colx)
        tk.Label(window, text = str(item.quality)).grid(row  = rowx + 1, column = colx + 1)
        tk.Label(window, text ="Price:").grid(row  = rowx + 2, column = colx)
        tk.Label(window, text = str(item.price)).grid(row  = rowx + 2, column = colx + 1)
        btn = tk.Button(window, text = "Buy me!", command =lambda: buyitem(item, player, shop))       
        btn.grid(row = rowx +3, column = colx, columnspan = 2)
        if colx == 0:
            colx = 3
        else:
            colx = 0
            rowx += 5
def opensave(filename):
    player = None    
    filename = filename + ".dat"
    try:
        gameFile = open(filename, "rb")
        player = pickle.load(gameFile)
        shopinventory = pickle.load(gameFile)
        gameFile.close()
        pet = player._pets[0]
        print(pet.__str__())
        compets = Compets()
        for idx, content in Const.CompPlayer.items():
            compets.addPet(Pet(idx,content['speed'],content['strength'],content['endurance']))    
        mainmenu(player,shopinventory, compets)
    except:
        print("Error. File does not exist")
startwindow()