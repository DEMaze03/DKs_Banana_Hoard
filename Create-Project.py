import csv
import os

def valid_csv(filename):
    if os.path.isfile(filename):
        if filename.endswith('.csv'):
            return True
        else:
            return 'exists, not csv'
    else:
        if filename.endswith('.csv'):
            return 'csv does not exist'
        else:
            return 'file does not exist nor is csv'

def addFile(old,new):
    with open(old, 'r') as oldfile:
        oldReader = csv.reader(oldfile, delimiter = ',')
        for rows in oldReader:
            if rows:
                with open(new, 'a') as newfile:
                    newfileWriter = csv.writer(newfile)
                    newfileWriter.writerow(rows)

inMenu = True
rightfile = False
menuLevel = 0
newfilename = 'a'
print('   ___  __ ___        ___                             __ __                 __')
print('  / _ \/ //_( )___   / _ )___ ____  ___ ____  ___ _  / // /__  ___ ________/ /')
print(' / // / ,<  |/(_-<  / _  / _ `/ _ \/ _ `/ _ \/ _ `/ / _  / _ \/ _ `/ __/ _  / ')
print('/____/_/|_|  /___/ /____/\_,_/_//_/\_,_/_//_/\_,_/ /_//_/\___/\_,_/_/  \_,_/ ')
                                                                                              
print("Welcome to DK's Banana Hoard! The interactive video game collection program!")
prevFileCheck = input("Before we begin, have you used this program before? (Y/N)\n")
prevFileCheck = prevFileCheck.lower()

if prevFileCheck[0] == 'y':
    while rightfile == False:
        filename = input("Please enter the name of the .csv file generated last time.\nIf you do not remember, the file will be stored in the same location as this program.\n")
        if valid_csv(filename) == True:
            rightfile = True
        elif valid_csv(filename) == 'exists, not csv':
            print(f"Uh oh! {filename} exists, but it's not a .csv file! Please enter a valid .csv file")
        elif valid_csv(filename) == 'csv does not exist':
            print(f"Uh oh! {filename} does not exist! Please enter a valid .csv file")
        elif valid_csv(filename) == 'file does not exist nor is csv':
            print(f"Uh oh! {filename} does not exist! Please enter a valid .csv file")
    while newfilename.endswith('.csv') == False:       
        newfilename = input("Now enter the name you would like to save this .csv file as:\n")
        if newfilename.endswith('.csv') == False:
            print("Uh oh! Please end your file name with '.csv'")
    addFile(filename,newfilename)
elif prevFileCheck[0] == 'n':
    newfilename = 'DKBH_01.csv'
    print("The .csv file will be saved as 'DKBH_01.csv' for this first time. You may change this when using the program again.")

def add_game(name, physical, platform, DOP, purchasePrice):
    physical = physical.lower()
    if physical[0] == 'p':
        physical = 'Physical'
    else:
        physical = 'Digital'
    addList = ['Game', name, physical, platform, DOP, purchasePrice]
    with open(newfilename, 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(addList)
        
def add_accessory(name,platform,manufacturer,DOP,purchasePrice):
    addList = ['Accessorie', name, platform, manufacturer, DOP, purchasePrice]
    with open(newfilename, 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(addList)

def add_console(name, manufacturer, DOP, purchasePrice):
    addList = ['Console', name, manufacturer, DOP, purchasePrice]
    with open(newfilename, 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(addList)

def add_collectible(name, manufacturer, DOP, purchasePrice):
    addList = ['Collectible', name, manufacturer, DOP, purchasePrice]
    with open(newfilename, 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow(addList)

def sort_csv(category):
    items_in_cat = []
    with open(newfilename,'r') as newFile:
        fileReader = csv.reader(newFile, delimiter = ',')
        for rows in fileReader:
            if rows:
                if rows[0] == category:
                    items_in_cat.append(rows[1:])
    if len(items_in_cat)>0:
        return items_in_cat
    else:
        return f"You don't have any {category}s on file! Try adding some!"

def print_games():
    game_list = sort_csv('Game')
    loop = 1
    if game_list != "You don't have any Games on file! Try adding some!":
        for item in game_list:
            name = item[0]
            physical = item[1]
            platform = item[2]
            DOP = item[3]
            purchasePrice = item[4]
            print(f"({loop}) - {name}, {physical} edition, for the {platform}. Purchased on {DOP} for {purchasePrice}")
            loop += 1
    else:
        print(game_list)

def print_consoles():
    console_list = sort_csv('Console')
    loop = 1
    if console_list != "You don't have any Consoles on file! Try adding some!":
        for item in console_list:
            name = item[0]
            manufacturer = item[1]
            DOP = item[2]
            purchasePrice = item[3]
            print(f"({loop}) - {manufacturer} {name}. Purchased on {DOP} for {purchasePrice}")
            loop += 1
    else:
        print(console_list)

def print_accessory():
    acc_list = sort_csv('Accessorie')
    loop = 1
    if acc_list != "You don't have any Accessories on file! Try adding some!":
        for item in acc_list:
            name = item[0]
            platform = item[1]
            manufacturer = item[2]
            DOP = item[3]
            purchasePrice = item[4]
            print(f"({loop}) - {manufacturer} {name} for the {platform}. Purchased on {DOP} for {purchasePrice}")
            loop += 1
    else:
        print(acc_list)

def print_collectible():
    col_list = sort_csv('Collectible')
    loop = 1
    if col_list != "You don't have any Collectibles on file! Try adding some!":
        for item in col_list:
            name = item[0]
            manufacturer = item[1]
            DOP = item[2]
            purchasePrice = item[3]
            print(f"({loop}) - {name}, made by {manufacturer}. Purchased on {DOP} for {purchasePrice}")
            loop += 1
    else:
        print(col_list)

def printMenu(level):
    if level == 0:
        print('\n\n+-----------------------------------------------+')
        print('|            Please Select an option:		|')
        print('|				    		|')
        print('|(1) - Add an item to your collection		|')
        print('|				    		|')
        print('|(2) - View your collection			|')
        print('|				    		|')
        print('|(3) - Exit the Program				|')
        print('|		    				|')
        print('+-----------------------------------------------+  ')
    if level == 1:
        print('\n\n+-----------------------------------------------+')
        print('|            Please Select an option:		|')
        print('|					    	|')
        print('|(1) - Add a video game				|')
        print('|					    	|')
        print('|(2) - Add a console				|')
        print('|					    	|')
        print('|(3) - Add an accessory 	     		|')
        print('|					    	|')
        print('|(4) - Add a collectible			|')
        print('|					    	|')
        print('|(5) - Back					|')
        print('|					    	|')
        print('+-----------------------------------------------+')
    if level == 2:
        print('\n\n+-----------------------------------------------+')
        print('|            Please Select an option:		|')
        print('|					    	|')
        print('|(1) - View video games				|')
        print('|						|')
        print('|(2) - View consoles				|')
        print('|					    	|')
        print('|(3) - View accessories 	     	        |')
        print('|				    		|')
        print('|(4) - View collectibles	    		|')
        print('|		    				|')
        print('|(5) - View all	    				|')
        print('|						|')
        print('|(6) - Back			    		|')
        print('|						|')
        print('+-----------------------------------------------+')

while inMenu:
    if menuLevel == 0:
        printMenu(0)
        choice = int(input('Please enter your choice here >'))
        if choice == 1:
            menuLevel = 1
        elif choice == 2:
            menuLevel = 2
        elif choice == 3:
            inMenu = False
        else:
            print('Please enter a valid choice')
    if menuLevel == 1:
        printMenu(1)
        choice = int(input('Please enter your choice here >'))
        if choice == 1:
            name = input("Enter the name of your game:\n")
            physical = input("Enter whether your game is a digital copy or a physical copy:\n")
            platform = input("Enter the platform your game is for (i.e. Nintendo Switch, Xbox One, etc.):\n")
            DOP = input("Enter the date of purchase of your game (MM/DD/YYYY):\n")
            purchasePrice = input("Enter the price you paid for this game:\n")
            confirm = input(f"Are you sure you want to add {name} for the {platform} purchased on {DOP} for {purchasePrice}? (Y/N)\n")
            confirm = confirm.lower()
            if confirm[0] == 'y':
                add_game(name,physical,platform,DOP,purchasePrice)
                print(f'Game successfully added to {newfilename}!')
        elif choice == 2:
            name = input("Enter the name of your console:\n")
            manufacturer = input("Enter the name of the console's manfacturer:\n")
            DOP = input("Enter the date of purchase of your console (MM/DD/YYYY):\n")
            purchasePrice = input("Enter the price you paid for this console:\n")
            confirm = input(f"Are you sure you want to add the {manufacturer} {name} purchased on {DOP} for {purchasePrice}? (Y/N)\n")
            confirm = confirm.lower()
            if confirm[0] == 'y':
                add_console(name,manufacturer,DOP,purchasePrice)
                print(f'Console successfully added to {newfilename}!')
        elif choice == 3:
            name = input("Enter the name of your accessory:\n")
            platform = input("Enter the system your accessory was made for\n")
            manufacturer = input("Enter the name of the accessory's manfacturer:\n")
            DOP = input("Enter the date of purchase of your accessory (MM/DD/YYYY):\n")
            purchasePrice = input("Enter the price you paid for this accessory:\n")
            confirm = input(f"Are you sure you want to add the {manufacturer} {name} for the {platform} purchased on {DOP} for {purchasePrice}? (Y/N)\n")
            confirm = confirm.lower()
            if confirm[0] == 'y':
                add_accessory(name,platform,manufacturer,DOP,purchasePrice)
                print(f'Accessory successfully added to {newfilename}!')
        elif choice == 4:
            name = input("Enter the name of your collectible:\n")
            manufacturer = input("Enter the name of the collectible's manfacturer:\n")
            DOP = input("Enter the date of purchase of your collectible (MM/DD/YYYY):\n")
            purchasePrice = input("Enter the price you paid for this collectible:\n")
            confirm = input(f"Are you sure you want to add the {name} made by {manufacturer} purchased on {DOP} for {purchasePrice}? (Y/N)\n")
            confirm = confirm.lower()
            if confirm[0] == 'y':
                add_console(name,manufacturer,DOP,purchasePrice)
                print(f'Collectible successfully added to {newfilename}!')
        elif choice == 5:
            menuLevel = 0
        else:
            print('Please enter a valid choice')
    if menuLevel == 2:
        printMenu(2)
        choice = int(input('Please enter your choice here >'))
        if choice == 1:
            print_games()
        elif choice == 2:
            print_consoles()
        elif choice == 3:
            print_accessory()
        elif choice == 4:
            print_collectible()
        elif choice == 5:
            print('Games:')
            print_games()
            print('\nConsoles:')
            print_consoles()
            print('\nAccessories:')
            print_accessory()
            print('\nCollectibles:')
            print_collectible()
        elif choice == 6:
            menuLevel = 0
        else:
            print('Please enter a valid choice')
