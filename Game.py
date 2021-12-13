from events import *
import base_config


class Game:

    def __init__(self):
        self.map_arr = self.createMapArrayFromString(base_config.map)
        self.visual_map = self.createMapArrayFromString(base_config.visual_map)
        self.legende = base_config.legende
        self.inventar = base_config.inventar
        self.x = base_config.x
        self.y = base_config.y
        self.runde = base_config.runde
        self.lebens_energie = base_config.lebens_energie
        self.optionen = base_config.optionen
        self.inventar_optionen = base_config.inventar_optionen

    # static
    @staticmethod
    def createMapArrayFromString(map):
        map_tmp = map.splitlines()
        map_arr = []
        for i in range(1, len(map_tmp)):
            new = []
            for j in map_tmp[i]:
                new.append(j)
            map_arr.append(new)
        return map_arr

    def printMapArr(self):
        map_arr = self.visual_map
        x = self.x
        y = self.y

        print("\nKarte:")
        output = ""
        for i in range(0, len(map_arr)):
            for j in range(0, len(map_arr[i])):
                if(x == j and y == i):
                    output += 'X'
                else:
                    output += map_arr[i][j]
            output += "\n"
        print(output)

    def showMap(self):

        self.printMapArr()
        self.printStatusBar()
        # print("Deine Position:" + str(x)+"/"+str(y))

    def printStatusBar(self):
        for i, j in self.legende.items():
            print(i, " : ", j, sep="")
        print("\nLebens-Energie: ", self.lebens_energie)

    def printEvents(self):
        # print(f"runde: {self.runde}")
        if(self.runde in events):
            e = events[self.runde]
            print("\n", e, "\n")
            self.breakInput()

    def handleOutOfBounds(self):
        self.current_event = "Die Erde ist keine Scheibe!"

        if(self.y < 0):
            self.y = len(self.visual_map)-1
        elif(self.y > len(self.visual_map)-1):
            self.y = 0
        elif(self.x < 0):
            self.x = len(self.visual_map[0])-1
        elif(self.x > len(self.visual_map[0])-1):
            self.x = 0
        else:
            self.current_event = ''

    def handleEndOfRound(self):
        self.lebens_energie -= 1
        self.runde += 1
        if(self.lebens_energie < 1):
            print("\n† Du bist gestorben †\n")
            exit()

    def getCurrentOptions(self):
        return self.optionen

    def zeigeInventar(self):
        inventar = "inventar:\n"
        count = 1
        for i in self.inventar:
            inventar += f"{count} : {i},"
            inventar = inventar.rstrip(",")
            count += 1
        print(inventar)
        self.userInput(self.inventar_optionen)

    def userInput(self, options=None):
        print("\n-- Deine Möglichkeiten")
        if(not options):
            current_options = self.getCurrentOptions()
        else:
            current_options = options

        count = 1
        for i, j in current_options.items():
            if count % 4:
                end = "\t\t"
            else:
                end = "\n"

            print(i, ":", j, end=f"{end}")
            count += 1
        print()
        richtung = input("=> ")

        if(richtung == "n"):
            self.y -= 1
        elif(richtung == "o"):
            self.x += 1
        elif(richtung == "s"):
            self.y += 1
        elif(richtung == "w"):
            self.x -= 1
        elif(richtung == 'z'):
            self.zeigeInventar()
        elif(richtung == 'q'):
            print("Spiel wurde beendet")
            exit()
        self.handleOutOfBounds()

    def breakInput(self):
        input("<Drücke RETURN um fortzufahren> ")
