import json

class State:
    def __init__(self):
        self.read()
       
        # configure default state
        if not hasattr(self, 'isOpen'):
            self.isOpen = False
        if not hasattr(self, 'musicHours'):
            self.musicHours = 0.0
        if not hasattr(self, 'meditationDays'):
            self.meditationDays = 0
        if not hasattr(self, 'meditatedToday'):
            self.meditatedToday = False
        if not hasattr(self, 'drinkDays'):
            self.drinkDays = 0
        if not hasattr(self, 'cheatDays'):
            self.cheatDays = 0
        if not hasattr(self, 'cheatToday'):
            self.cheatToday = False
        self.save()
    
    # FUNCTIONS
   
    def open(self):
        self.isOpen = True
        self.save()

    def close(self):
        self.isOpen = False
        self.save()

    def addMusic(self, amount, unit):
        hrs = 0.0
        if unit == 'min':
            hrs += amount/60.0
        elif unit == 'hrs':
            hrs += amount
        else:
            print('ERROR: unknown time unit: '+ unit)
        
        print("adding hours: " + str(hrs))

        self.musicHours += hrs
        self.save()

    def addMeditationDay(self):
        self.meditationDays += 1
        self.meditatedToday = True
        self.save()

    def addDrinkDay(self):
        self.drinkDays += 1
        self.save()

    def addCheatDay(self):
        self.cheatDays += 1
        self.cheatToday = True
        self.save()

    def toJson(self):
        return self.__dict__

    # FILE INTERACTIONS
    
    def save(self):
        print('saving file with state:')
        print(self.__dict__)

        with open('data.json', 'w+') as f:
            json.dump(self.__dict__, f)
    
    def read(self):
        try:
            with open('data.json', 'r') as f:
                self.__dict__ = json.load(f)
        except IOError:
            print "No data file exists. Creating new..."

