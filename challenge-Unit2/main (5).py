'''Implement a class called Player that represents a cricet player the class should have a
method called play() which prints "the plyer is playing cricet"Derive two classes,Batsman and
Bowler,from the Player class.Override the play() method derived class to print "The batsman
is batting" and "the bowler is bowling",respectively.Write a program to create objects of both the 
Batsman and Bowler classes and call the play() method for each objects.'''


class Player:
  def play(self):
    print("the player is playing cricket.")

class Batsman(Player):
  def play(self):
    print("the batsman  is bating.")
    
class Bowler(Player):
  def play(self):
    print("the bowler is bowling.")

batsman = Batsman()
bowler = Bowler()
player = Player()
player.play()
batsman.play()
bowler.play()


      
      
    