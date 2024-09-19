class Direction:
   UP = 0
   RIGHT = 1
   DOWN = 2
   LEFT = 3
  
lives = 3
score = 0
player_position = [0,0]
end_position = [4,4]
direction = Direction.RIGHT

def display_status():
    print (f"Lives: {lives}, Score: {score}")
    
def check_reach_end():
    global score
    if player_position == end_position:
     score+= 100
    print("You have reached the end of the maze! :D")
    display_status()
    
def lose_life():
    global lives
    lives -= 1
    
def move_player(direction):
    global player_position
   
    if direction == Direction.DOWN:
        player_position[1] += 1
    elif direction == Direction.UP:
        player_position[1] -= 1
    elif direction == Direction.RIGHT:
        player_position[0] += 1
    elif direction == Direction.LEFT:
        player_position[0] -= 1
        
    print (player_position)
   
if __name__ == "__main__":
    display_status()  
    move_player(Direction.RIGHT)  
    move_player(Direction.DOWN)
    move_player(Direction.DOWN)  
    move_player(Direction.RIGHT)  
    move_player(Direction.DOWN)   
    move_player(Direction.RIGHT)  
    move_player(Direction.RIGHT)
    move_player(Direction.DOWN)
    check_reach_end()
    lose_life()    