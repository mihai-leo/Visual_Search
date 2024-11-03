import pygame
import math
import random
from queue import PriorityQueue,Queue

from colors import WHITE, RED, GREEN, BLUE, YELLOW, BLACK, PURPLE, ORANGE, GREY, TURQUOISE, red_intensity_list, intensity_list # type: ignore
WIDTH = 1000
WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("Finding Algorithms")
pygame.font.init()
info = "Keys function :\n> SPACE: Info Window\n> R: New Matrix\n> C: Clear\n> B: Breadth-First Search\n> D: Depth-First Search\n> A: A* Search\n> U: Uniform Cost Search\n> J: Dijkstra's Algorithm\n\n\n\n-- the distance between 2 nodes is --\n-- the absolute value between their values --"

class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*width
        self.color=WHITE #Using WHITE from colors.py
        self.neighbors= []
        self.width=width
        self.total_rows=total_rows
        self.drawn = False
        self.number = random.randint(2, 10)

    def get_pos(self):
        return self.row,self.col
    
    def is_closed(self):
        return (self.color == RED or self.color in red_intensity_list or self.color in intensity_list)
    
    def id_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == BLUE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color=WHITE
        self.drawn = False

    def make_start(self):
        self.color = BLUE
        self.drawn = False
        
    def make_closed(self):
        self.color = RED
        self.drawn = False

    def make_closed2(self,i):
        i=i+180
        i = max(0, min(i, len(intensity_list) - 1))  
        self.color = intensity_list[i]
        self.drawn = False

    def make_open(self):
        self.color = GREEN
        self.drawn = False

    def make_barrier(self):
        self.color = BLACK
        self.drawn = False

    def make_end(self):
        self.color = TURQUOISE
        self.drawn = False

    def make_path(self):
        self.color = PURPLE
        self.drawn = False

    def draw(self,win):
        if not self.drawn:
            pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
            font = pygame.font.SysFont(None, self.width) 
            text_surface = font.render(str(self.number), True, (0, 0, 0))  
            text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.width // 2))
            win.blit(text_surface, text_rect)
            self.drawn=True

    def update_neighbors(self,grid):
        self.neighbors = []
        if self.row <self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self,other):
        return False
    
def h(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)

def reconstruct_path(came_from,current,draw):
    print("Path")
    print("Start:")
    x=0
    y=0
    while current in came_from:
        print(f" ({current.row} , {current.col}),")
        draw()
        x=x+1
        y=y+abs(current.number-came_from[current].number)
        current = came_from[current]
        current.make_path()
    print("Goal")
    print(f"Lenght: {x} steps   {x+y} 3D")
    

def dfs(draw,grid,start,end):
    stack = [start]
    came_from = {}
    i=254
    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
        current = stack.pop()
        
        if current == end:
            reconstruct_path(came_from,end,draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            if neighbor not in came_from and neighbor != start:
                stack.append(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()
        
        draw()

        if current != start:
            current.make_closed2(i)
            i=i-1
        
    return False

def bfs(draw,grid,start,end):
    open_set = Queue()
    open_set.put(start)
    i=254
    came_from = {}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
        current = open_set.get()
        
        if current == end:
            reconstruct_path(came_from,end,draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            if neighbor not in came_from and neighbor != start:
                open_set.put(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()
        
        draw()

        if current != start:
            current.make_closed2(i)
            i=i-1
        
    return False

def ucs(draw,grid,start,end):
    open_set = PriorityQueue()
    open_set.put((0, start)) 
    came_from = {}
    cost_so_far = {start: 0}  
    i = 254 

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[1]  

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            new_cost = cost_so_far[current] + 1 + abs(neighbor.number - current.number)  
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost 
                open_set.put((new_cost, neighbor))  
                came_from[neighbor] = current 
                neighbor.make_open()
        
        draw()

        if current != start:
            current.make_closed2(i)
            i -= 1  

    return False

def dij(draw,grid,start,end):
    open_set = PriorityQueue()
    open_set.put((0, start)) 
    came_from = {}
    score = {spot:float("inf") for row in grid for spot in row }
    score[start] = 0
    i = 254 

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[1]  

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            new_score= score[current] + 1 + abs(neighbor.number - current.number)  
            
            if  new_score < score[neighbor]:
                score[neighbor] = new_score
                open_set.put((new_score, neighbor))  
                came_from[neighbor] = current 
                neighbor.make_open()
        
        draw()

        if current != start:
            current.make_closed2(i)
            i -= 1  

    return False



def a_star(draw,grid,start,end):
    count = 0
    i=254
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score = {spot:float("inf") for row in grid for spot in row }
    g_score[start] = 0
    f_score = {spot:float("inf") for row in grid for spot in row }
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from,end,draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 + abs(neighbor.number - current.number)

            if temp_g_score  < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] =temp_g_score + h (neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set_hash.add(neighbor)
                    open_set.put((f_score[neighbor],count,neighbor))
                    neighbor.make_open()
        
        draw()

        if current != start:
            current.make_closed2(i)
            i=i-1
        
    return False


def make_grid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,gap,rows)
            grid[i].append(spot)    
    return grid

def copy_grid(grid_source,rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,gap,rows)
            spot.number=grid_source[i][j].number
            if grid_source[i][j].is_barrier():
                spot.make_barrier()
            grid[i].append(spot)    
    return grid

def remake_grid(grid_source,rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = grid_source[i][j]
			spot.drawn=False
			grid[i].append(spot)

	return grid
def drow_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
        for j in range(rows):
            pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width))

def draw(win, grid, rows, width):

    for row in grid:
        for spot in row:
            spot.draw(win)

    drow_grid(win, rows, width)
    pygame.display.update()

def get_cliked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col =x // gap

    return row, col
def show_popup(message, win):
    d=WIDTH//4
    fs=d//10
    popup_rect = pygame.Rect(d,d,WIDTH-2*d,WIDTH-2*d)

    overlay = pygame.Surface((WIDTH, WIDTH), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))  
    win.blit(overlay, (0, 0))

    # Draw the popup background
    pygame.draw.rect(win, WHITE, popup_rect)
    pygame.draw.rect(win, BLACK, popup_rect, 2)  # Black border for the popup

    # Display message in the popup
    font = pygame.font.SysFont(None, fs)
    lines = message.splitlines()  # Split message into lines if multiline
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, BLACK)
        text_rect = text_surface.get_rect(center=(d + (WIDTH-2*d) // 2, d + 2*fs + i * fs))
        win.blit(text_surface, text_rect)

    # Display "Press any key to close"
    hint_text = font.render("Press any key to close", True, GREY)
    hint_rect = hint_text.get_rect(center=(d + (WIDTH-2*d) // 2, WIDTH-d-2*fs))
    win.blit(hint_text, hint_rect)

    pygame.display.update()

    # Wait for a key press to close the popup
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                waiting = False

def main(win,width):
    ROWS = 20 
    print(len(intensity_list))
    grid = make_grid(ROWS, width)
    start = None
    end = None

    run = True
    
    win.fill(WHITE)
    show_popup(info, win)
    while run:
        draw(win,grid,ROWS,width)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_popup(info, win)
                grid = remake_grid(grid,ROWS, width)
                draw(win,grid,ROWS,width)
            if pygame.mouse.get_pressed()[0]: #left
                pos =pygame.mouse.get_pos()
                row, col = get_cliked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()
                
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #right
                pos = pygame.mouse.get_pos()
                row, col = get_cliked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end =None
            elif event.type == pygame.KEYDOWN:
                if start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    if event.key == pygame.K_b:
                        bfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    if event.key == pygame.K_d:
                        dfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    if event.key == pygame.K_a:
                        a_star(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    if event.key == pygame.K_u:
                        ucs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    if event.key == pygame.K_j:
                        dij(lambda: draw(win, grid, ROWS, width), grid, start, end)
                
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = copy_grid(grid,ROWS, width)
    pygame.quit()
main (WIN,WIDTH)


