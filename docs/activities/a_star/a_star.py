# Guillermo José Cervera Cervera

from operator import attrgetter
import pygame
from os import path
import math

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def transform_maze():
    src = pygame.image.load(path.join(*['docs', 'activities', 'a_star', 'maze_org.bmp']))
    dst = pygame.Surface((61,61))

    src.lock()
    dst.lock()
    for x in range(5,615,10):
        for y in range(5,615,10):
            c = src.get_at((x,y))
            dst.set_at((int((x - 5)/10), int((y-5)/10)), c)

    src.unlock()
    dst.unlock()

    pygame.image.save(dst, path.join(*['docs', 'activities', 'a_star', 'maze.bmp']))

def read_maze():
    maze_img = pygame.image.load(path.join(*['docs', 'activities', 'a_star', 'maze.bmp']))
    maze = []
    maze_size = maze_img.get_size()

    maze_img.lock()
    for y in range(maze_size[1]):
        row = []
        for x in range(maze_size[0]):
            color = maze_img.get_at((x,y))
            if color == (255, 255, 255, 255):   #stepable
                row.append(0)
            else:
                row.append(1)       #wall
        maze.append(row)
    maze_img.unlock()

    return maze

def build_maze_image(maze_matrix, zoom):
    rows, cols = get_maze_size(maze_matrix)
    maze_img = pygame.Surface((cols* zoom, rows * zoom))
    maze_img.lock()
    for row in range(rows):
        for col in range(cols):
            color = (255,255,255,255) if maze_matrix[row][col] == 0 else (0,0,0,255)
            for x in range(zoom):
                for y in range(zoom):
                    maze_img.set_at(((col* zoom) + x,(row * zoom) + y), color)
    maze_img.unlock()

    return maze_img

def get_maze_size(maze_matrix):
    return len(maze_matrix), len(maze_matrix[0])

def point_to_maze_coord(zoom, point):  # returns row, col
    return int(point[1] / zoom), int(point[0] / zoom)

def maze_coord_to_point(zoom, coord):  # returns x,y
    return coord[1] * zoom, coord[0] * zoom

def maze_coord_is_stepable(maze_matrix, coord):
    return maze_matrix[int(coord[0])][int(coord[1])] == 0

def calc_path(maze_matrix, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    
    current_node = start_node
    
    #Tu codigo aqui
    list1=[]
    list2=[]
    list1.append(start_node)
    is_not_in_list1=1
    is_not_in_list2=1
    while (len(list1)>=1):
        current_node=max(list1,key=attrgetter('f'))
        
        # test if goal is reached or not, if yes then return the path
        if(current_node == end_node):
            return return_path(current_node,maze_matrix)
        
        #Tu codigo aqui
        list1.pop(list1.index(current_node))
        list2.append(current_node)
        for pos in[(-1,0),(0,-1),(0,1),(1,0)]:
            pos=(pos[0]+current_node.position[0],pos[1]+current_node.position[1])
            if(pos[1]>(len(maze_matrix[len(maze_matrix)-1])-1)):
                continue
            if(maze_matrix[pos[0]][pos[1]]>=1):
                continue
            n_node=Node(current_node,pos)
            for node in list2:
                if(n_node.__eq__(node)):
                    is_not_in_list2=0
                    continue
            if(not is_not_in_list2):
                is_not_in_list2=1
                continue
            if(is_not_in_list1):
                list1.append(n_node)
            for node in list1:
                if n_node.__eq__(node):
                    if (node.g<n_node.g):
                        break

def euclidean_distance(src, dst):
    x_dist = abs(src[0] - dst[0])
    y_dist = abs(src[1] - dst[1])
    return 10 * math.sqrt((x_dist * x_dist) + (y_dist * y_dist))
    return ((src[0] - dst[0]) ** 2) + ((src[1] - dst[1]) ** 2)

def manhattan_distance(src, dst):
    x_dist = abs(src[0] - dst[0])
    y_dist = abs(src[1] - dst[1])
    return 10 * (x_dist + y_dist)

def diagonal_distance(src, dst):
    x_dist = abs(src[0] - dst[0])
    y_dist = abs(src[1] - dst[1])
    return (10 * (x_dist + y_dist)) + (-6 * min(x_dist, y_dist))

def return_path(current_node,maze):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    # Return reversed path as we need to show from start to end path
    path = path[::-1]

    return path

def path_to_img(maze_matrix, zoom, path):
    rows, cols = get_maze_size(maze_matrix)
    maze_img = pygame.Surface((cols* zoom, rows * zoom), pygame.SRCALPHA, 32).convert_alpha()

    if path:
        for coord in path:
            point = maze_coord_to_point(zoom, coord)
            rect = pygame.Rect(point,(zoom, zoom))
            pygame.draw.rect(maze_img, (0,0,255,255), rect)

    return maze_img

pygame.init()

zoom = 10
maze = read_maze()
maze_img = build_maze_image(maze, zoom)

screen_size = maze_img.get_size()
screen = pygame.display.set_mode(screen_size, 0, 32)

running = True
clock = pygame.time.Clock()

start_coord = (-1.0, -1.0)
end_coord = (-1.0, -1.0)
click_to_start = True

path_img = pygame.Surface(maze_img.get_size(), pygame.SRCALPHA, 32).convert_alpha()

start_img = pygame.Surface((zoom, zoom))
start_img.fill((0,255,0,255))
end_img = pygame.Surface((zoom, zoom))
end_img.fill((255,0,0,255))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if click_to_start:
                    coord = point_to_maze_coord(zoom, event.pos)
                    if maze_coord_is_stepable(maze, coord):
                        start_coord = coord
                        click_to_start = False
                else:
                    coord = point_to_maze_coord(zoom, event.pos)
                    if maze_coord_is_stepable(maze, coord):
                        end_coord = coord
                        new_path = calc_path(maze, start_coord, end_coord)
                        path_img = path_to_img(maze, zoom, new_path)
                        click_to_start = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    delta_time = clock.tick(30)

    screen.fill((200, 200, 200))

    screen.blit(maze_img, (0,0))
    screen.blit(path_img, (0,0))

    screen.blit(start_img, maze_coord_to_point(zoom, start_coord))
    screen.blit(end_img, maze_coord_to_point(zoom, end_coord))

    pygame.display.update()

pygame.quit()
