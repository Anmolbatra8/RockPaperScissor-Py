class Participant:
    def __init__(self):
        self.name = " "
        self.choice = ""
        
    
    def makechoice(self):
            self.name = input("Player Name: ")
            self.choice = input(f"Hi {self.name} , select r,p or s: ")
        
        
    
class GameRound:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
        
    def game(self):
        choices = {"r": "rock", "p": "paper", "s": "scissors"}
        if(self.p1.choice == self.p2.choice):
            print(f"DRAW b/w both {choices[self.p1.choice]} ")
        
        elif (self.p1.choice == 'r' and self.p2.choice == 's') or \
            (self.p1.choice == 'p' and self.p2.choice == 'r') or \
            (self.p1.choice == 's' and self.p2.choice == 'p'):
                print(f"{self.p1.name} WINS ! {choices[self.p1.choice]} beats {choices[self.p2.choice]}")
        
        else:
             print(f"{self.p2.name} WINS ! {choices[self.p2.choice]} beats {choices[self.p1.choice]}")
            
        
        
        
Anmol = Participant()
Ansh =  Participant()
Anmol.makechoice()
Ansh.makechoice()
g1 = GameRound(Anmol,Ansh)
g1.game()
