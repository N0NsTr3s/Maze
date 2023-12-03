import random
import os
#Generateing and printing the maze
latime=28
lungime=28
i_start=0
i_stop=0
maze = [[0 for x in range(lungime)] for y in range(latime)]
for i in range(lungime):
    for j in range(latime):
        if i==0 or i==latime-1 or j==0 or j==lungime-1:
            maze[i][j]='█'
        else:
            maze[i][j]='█' 
def print_maze(maze):
     for row in maze:
        row_str = ''
        for cell in row:
            if cell == '█':
                row_str += '█'
            elif cell==' ':
                row_str+=' '
            elif cell=='M':
                row_str+='M'
            elif cell=='*':
                row_str+='*'
        print(row_str)

def is_too_close(position, maze):

    #Check if a given position is too close to an already existing path in the maze.

    i, j = position
    if maze[i-1][j]==maze[i+1][j] and (maze[i+1][j]=='█' or maze[i-1][j]=='█') or maze[i][j+1]==maze[i][j-1] and (maze[i][j+1]=='█' or maze[i][j-1]=='█'):
        return True
    elif maze[i][j+1]==maze[i][j-1] and (maze[i][j+1]=='█' or maze[i][j-1]=='█'):
        return True
    else:
        return False

#Generateing a start point
I=random.randrange(1, lungime-2)
maze[I][0]=' '
I=random.randrange(1, latime-2)
maze[I][latime-1]=' '

for i in range(lungime):
    if  maze[i][0]==' ':
        i_start=i
j_start=1
#Generateing an end point
for i in range(lungime):
    if  maze[i][latime-1]==' ':
        i_stop=i     
j_stop=latime-1



#Generate a random path to the end of the maze          
def sts(maze, start_pos, end_pos):
    i_start, j_start = start_pos
    i_stop, j_stop = end_pos

    while i_start != i_stop or j_start != j_stop:
        maze[i_start][j_start] = ' '
        if random.random() < 0.25:
            if i_start < i_stop:
                i_start += 1
            elif i_start > i_stop:
                i_start -= 1
            elif j_start < j_stop:
                j_start += 1
            elif j_start > j_stop:
                j_start -= 1
        else:
            directions = ["up", "down", "left", "right"]
            direction = random.choice(directions)
            if direction == "up" and i_start > 1 and is_too_close((i_start, j_start), maze) == True:
                i_start -= 1
            elif direction == "down" and i_start < len(maze) - 2 and is_too_close((i_start, j_start), maze) == True:
                i_start += 1
            elif direction == "left" and j_start > 1 and is_too_close((i_start, j_start), maze) == True:
                j_start -= 1
            elif direction == "right" and j_start < len(maze[0]) - 2 and is_too_close((i_start, j_start), maze) == True:
                j_start += 1

            
    maze[i_start][j_start] = ' '


  
sts(maze, (i_start, j_start), (i_stop, j_stop))

fake_routes=[]
mainpath = [(i, j) for i in range(lungime) for j in range(latime) if maze[i][j] == ' ']

def add_fake_route(maze, start_pos, end_pos, fake_routes):
    i_start, j_start = start_pos
    i_stop, j_stop = end_pos
    main_route = [(i, j) for i in range(lungime) for j in range(latime) if maze[i][j] == ' ']
    if len(main_route) < 2:
        return
    # Choose one random point on an existing main route
    paths = [(i, j) for i in range(lungime) for j in range(latime) if maze[i][j] == ' ']
    start_pos = random.choice(main_route)
    
    
    # Number of intersections with other fake routes
    num_intersections = 0
    # Choose a random direction to start fake route
    directions = ["up", "down", "left", "right"]
    direction = random.choice(directions)

    # Generate fake route
    for k in range(random.randrange(lungime*4,lungime**3)):
        maze[i_start][j_start] = " "
        
        # Choose a new random direction every 3 movements
        if random.random() < 0.66:
            directions = ["up", "down", "left", "right"]
            directions.remove(direction)
            direction = random.choice(directions)
            
        # Check if current position is already occupied by another fake route
        while (i_start, j_start) in fake_routes or any([(i_start+1, j_start) in fake_routes, (i_start-1, j_start) in fake_routes, (i_start, j_start+1) in fake_routes, (i_start, j_start-1) in fake_routes]):
            # If fake route intersects with another fake route, discard it and try again with a new random starting point
            paths.remove(start_pos)
            if not paths:
                return
            start_pos = random.choice(paths)
            directions = ["up", "down", "left", "right"]
            direction = random.choice(directions)
            num_intersections = 0
            k = 0

        # If current position is not occupied by another fake route, continue in chosen direction
        if direction == "up" and i_start > 1 and is_too_close((i_start,j_start),maze)==True:
            i_start -= 1
            maze[i_start][j_start] = ' '
        if direction == "down" and i_start < i_stop-1 and is_too_close((i_start,j_start),maze)==True:
            i_start += 1
            maze[i_start][j_start] = ' '
        if direction == "left" and j_start > 1 and is_too_close((i_start,j_start),maze)==True:
            j_start -= 1
            maze[i_start][j_start] = ' '
        if direction == "right" and j_start < j_stop-1 and is_too_close((i_start,j_start),maze)==True:
            j_start += 1
            maze[i_start][j_start] = ' '

        # Update intersection count with other fake routes
        if (i_start, j_start) in fake_routes:
            num_intersections += 1
            
        # If fake route intersects with another fake route more than once, discard it and try again with a new random starting point
        if num_intersections == 1:
            paths.remove(start_pos)
            if not paths:
                return
            start_pos = random.choice(paths)
            directions = ["up", "down", "left", "right"]
            direction = random.choice(directions)
            num_intersections = 0
            k = 0
            fake_routes.append((i_start, j_start))
    fake_routes.append((i_start, j_start))
#Randomly select how many fake routes are in the maze
for m in range(random.randrange(lungime//2, lungime)):
    add_fake_route(maze, (random.randrange(1,lungime-2), random.randrange(1,latime-2)),(random.randrange(1,lungime-2), random.randrange(1,latime-2)),fake_routes)



def get_neighbors(row, col, maze, visited, i_stop, j_stop):
    #Returns a list of unvisited neighbor cells of the given cell, sorted by increasing distance to the end point.
    neighbors = []
    if row > 0 and maze[row-1][col] != '█' and (row-1, col) not in visited:
        distance = abs(row-1-i_stop) + abs(col-j_stop)
        neighbors.append((distance, row-1, col))
    if row < len(maze)-1 and maze[row+1][col] != '█' and (row+1, col) not in visited:
        distance = abs(row+1-i_stop) + abs(col-j_stop)
        neighbors.append((distance, row+1, col))
    if col > 0 and maze[row][col-1] != '█' and (row, col-1) not in visited:
        distance = abs(row-i_stop) + abs(col-1-j_stop)
        neighbors.append((distance, row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] !='█' and (row, col+1) not in visited:
        distance = abs(row-i_stop) + abs(col+1-j_stop)
        neighbors.append((distance, row, col+1))
    neighbors.sort()
    #Printing neightbors its optional
    #print(neighbors)
    return [(r, c) for _, r, c in neighbors]
# Initialize the visited positions
visited = set()

def solve_maze(maze,i,j, i_stop, j_stop):
    #Storing in queue position of the player
    queue = [(i,j, [])]
    while queue:
        
        # Dequeue the first position and its path
        i, j, path = queue.pop(0)
        
        #If the player gets to the end stop
        if (i, j) == (i_stop, j_stop):
            print("You won!")
            print(path + [(i, j)])
            for i,j in path+[(i,j)]:
                # Here you can change the mark left on the path
                maze[i][j]='*'#<-
            return
        #Marking every visited position
        if (i, j) not in visited:
            visited.add((i, j))
            #Getting every possible way of the player
            neighbors = get_neighbors(i, j, maze, visited, i_stop, j_stop)

            # Enqueue each valid neighbor with its path
            for neighbor in neighbors:
                if neighbor not in visited:
                     # Remove the last element from the path before enqueueing the neighbor
                    queue.append((neighbor[0], neighbor[1], path[:-1] + [(i, j), neighbor]))
       
    print("There is no path to the exit.")


# The monster is not always generated (Jesus knows why)
def add_monster(maze, main_route):
    # Shuffle the main route to select a random position for the monster
    random.shuffle(main_route)

    for pos in main_route:
        i_start, j_start = pos
        free_cells_around = 0

        # Check if there are 8 free cells around the current position
        for i in range(i_start - 1, i_start + 2):
            for j in range(j_start - 1, j_start + 2):
                if 1 < i <= len(maze) - 1 and 1 < j <= len(maze[0]) - 1 and maze[i][j] == ' ':
                    free_cells_around += 1

        if free_cells_around > 7:
            maze[i_start][j_start] = 'M'  # Place the monster
            return

# After generating the main path
add_monster(maze, mainpath)


for i in range(lungime):
    if maze[i][0]==' ':
        i_start=i
def play(maze):
    i, j = i_start,0
    maze[i][j] = '*'

    while True:
        os.system("clear")  # clear the terminal
        print_maze(maze)

        if i == i_stop and j == j_stop:
            print("You won!")
            return

        maze[i][j] = '*'

        direction = input("Which direction do you want to move (u/d/l/r)? Or you give up? (Yes)")

        if direction == "u" and maze[i-1][j] == " ":
            maze[i][j]=' '
            i -= 1
            maze[i][j]="*"
        elif direction == "d" and maze[i+1][j] == " " :
            maze[i][j]=' '
            i += 1
            maze[i][j]="*"
        elif direction == "l" and maze[i][j-1] == " ":
            maze[i][j]=' '
            j -= 1
            maze[i][j]="*"
        elif direction == "r" and maze[i][j+1] == " ":
            maze[i][j]=' '
            j += 1
            maze[i][j]="*"
        elif direction == "u" and maze[i-1][j] == "M":
            print("You`ve died")
            break
        elif direction == "d" and maze[i+1][j] == "M":
            print("You`ve died")
            break
        elif direction == "l" and maze[i][j-1] == "M":
            print("You`ve died")
            break
        elif direction == "r" and maze[i][j+1] == "M":
            print("You`ve died")
            break
        elif direction=="Yes":
            solve_maze(maze,i,j,i_stop,j_stop)
            break
        
        

play(maze)
print_maze(maze)