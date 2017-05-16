import random
dungeon = "...$$$....G...b.....D...W.b......D........"

level = list(dungeon)

class Monster():
    number = 0
    zoo = {}
    chars = ""
    

    def __init__(self, posx=0, char="ß",name="monster", hp=20,
             tohit = 0.6, evade = 0.2, maxdamage=5):

         self.x = posx
         self.char = char
         self.name = name
         self.hp = hp
         self.tohit = tohit
         self.evade = evade
         self.maxdamage = maxdamage
         self.number = Monster.number
         Monster.number +=1
         Monster.zoo[self.number] = self
         if self.char not in Monster.chars:
            Monster.chars += self.char 
             
             
    def report(self):
        return "{} hp: {} tohit: {} evade: {} maxdamage: {}" .format(
        self.name,self.hp,self.tohit,self.evade,self.maxdamage)
        
class Hero(Monster):    
   def __init__(self):             
            Monster. __init__ (self, 0,"@","demon", 20, 0.7, 0.4, 5)
            self.hunger = 0
            self.gold = 0
            
class Dragon(Monster):
    def __init__(self, posx):
        Monster.__init__(self,  posx, "D" ,"Dragon", 50, 0.8, 0.1, 7)
        
class Goblin(Monster):
    def __init__(self, posx):
        Monster.__init__(self,  posx, "G" ,"goblin", 10, 0.4, 0.5, 3)
 
class Wolf(Monster):
    def __init__(self, posx):
        Monster.__init__(self,  posx, "W" ,"wolf", 8, 0.6, 0.6, 2) 
        
        
                       
                

                
# generate monsters

hero = Hero() # hero always start at x_position 0

for x , char in enumerate(level):
    if char in Monster.chars:
        level[x] = "."
        if char == "§":
            Dragon(x)
        elif char == "&":
            Goblin(x)
        elif char == "!":
            Wolf(x)
        
    
    
                
                
while True :
  
  
  
  
   
    for x, char in enumerate(level):
        #print(x, char)
        for monster in Monster.zoo.values():
            if monster.x == x:
                print(monster.char, end="")
                break
                
            else:
                    print(level[x],end="")
                
                
        
    print()
    command = input("$: {} hunger {} hp: {} was jetzt?".format(
    hero.gold,hero.hunger,hero.hp))
    if command == "quit" or command == "exit":        
        break
    elif command == "a":
        hero.x -= 1
    elif command == "d":
        hero.x += 1
    elif command == "A":
        hero.x -= 3
    elif command == "D":
        hero.x += 3
    else:
        print("Drücke eine andere Taste")
    stuff = level[hero.x]
    if stuff == "$":
        hero_gold +=1   
        level[hero.x] = "."
    elif stuff == "b":
        hero_hunger -=1    
        level[hero.x] = "."
    # check monsters
    for monster in Monster.zoo.values():
        if monster.x == hero.x:
            print("epic fight againist"+monster.report())
            print("Hero wins, monster is kaputt")
            #kill monster
            del Monster.zoo[monster.number]
            break
            
            
        
        
        
        
        
        
        
   
