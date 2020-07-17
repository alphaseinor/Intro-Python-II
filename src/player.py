# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
                
        if(direction != "xxx"):
          room = getattr(self.current_room, f"{direction}_to")
          if room != None:
              self.current_room = room
          else:
              print("That way drops off a cliff into a bit bucket, try another path")
        else:
          print("---------\n\ninvalid key stroke\n\n---------")

    def __str__(self):
        return f"{self.name} is currently {self.current_room}"
