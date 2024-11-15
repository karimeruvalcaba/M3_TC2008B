optionMap = {
    (8, 0): {'down': 1, 'right': 1}, #beg
    (9, 0): {'down': 1, 'right': 1, 'left': 1}, #beg
    (10, 0): {'down': 1, 'left': 1}, #beg
    (12, 0): {'up': 1, 'right': 1}, #dest
    (13, 0): {'up': 1, 'right': 1, 'left': 1}, #dest
    (14, 0): {'up': 1, 'left': 1}, #dest
    (8, 1): {'down': 1, 'right': 1},
    (9, 1): {'down': 1, 'right': 1, 'left': 1},
    (10, 1): {'down': 1, 'left': 1},
    (12, 1): {'up': 1, 'right': 1},
    (13, 1): {'up': 1, 'right': 1, 'left': 1},
    (14, 1): {'up': 1, 'left': 1},
    (8, 2): {'down': 1, 'right': 1},
    (9, 2): {'down': 1, 'right': 1, 'left': 1},
    (10, 2): {'down': 1, 'left': 1},
    (12, 2): {'up': 1, 'right': 1},
    (13, 2): {'up': 1, 'right': 1, 'left': 1},
    (14, 2): {'up': 1, 'left': 1},
    (8, 3): {'down': 1, 'right': 1},
    (9, 3): {'down': 1, 'right': 1, 'left': 1},
    (10, 3): {'down': 1, 'left': 1},
    (12, 3): {'up': 1, 'right': 1},
    (13, 3): {'up': 1, 'right': 1, 'left': 1},
    (14, 3): {'up': 1, 'left': 1},
    (8, 4): {'down': 1, 'right': 1},
    (9, 4): {'down': 1, 'right': 1, 'left': 1},
    (10, 4): {'down': 1, 'left': 1},
    (12, 4): {'up': 1, 'right': 1},
    (13, 4): {'up': 1, 'right': 1, 'left': 1},
    (14, 4): {'up': 1, 'left': 1},
    (8, 5): {'down': 1, 'right': 1},
    (9, 5): {'down': 1, 'right': 1, 'left': 1},
    (10, 5): {'down': 1, 'left': 1},
    (12, 5): {'up': 1, 'right': 1},
    (13, 5): {'up': 1, 'right': 1, 'left': 1},
    (14, 5): {'up': 1, 'left': 1},
    (8, 6): {'down': 1, 'right': 1},
    (9, 6): {'down': 1, 'right': 1, 'left': 1},
    (10, 6): {'down': 1, 'left': 1},
    (12, 6): {'up': 1, 'right': 1},
    (13, 6): {'up': 1, 'right': 1, 'left': 1},
    (14, 6): {'up': 1, 'left': 1},
    (8, 7): {'down': 1, 'right': 1},
    (9, 7): {'down': 1, 'right': 1, 'left': 1},
    (10, 7): {'down': 1, 'left': 1},
    (12, 7): {'up': 1, 'right': 1},
    (13, 7): {'up': 1, 'right': 1, 'left': 1},
    (14, 7): {'up': 1, 'left': 1},
    (0, 8): {'right': 1, 'up': 1}, 
    (1, 8): {'right': 1, 'up': 1},
    (2, 8): {'right': 1, 'up': 1},
    (3, 8): {'right': 1, 'up': 1},
    (4, 8): {'right': 1, 'up': 1},
    (5, 8): {'right': 1, 'up': 1},
    (6, 8): {'right': 1, 'up': 1},
    (7, 8): {'right': 1, 'up': 1},
    (8, 8): {'right': 1, 'up': 1, 'down': 1},
    (9, 8): {'right': 1, 'up': 1, 'down': 1},
    (10, 8): {'right': 1, 'up': 1, 'down': 1},
    (11, 8): {'right': 1, 'up': 1},
    (12, 8): {'right': 1, 'up': 1},
    (13, 8): {'right': 1, 'up': 1},
    (14, 8): {'right': 1, 'up': 1},
    (15, 8): {'right': 1, 'up': 1},
    (16, 8): {'right': 1, 'up': 1},
    (17, 8): {'right': 1, 'up': 1},
    (18, 8): {'right': 1, 'up': 1},
    (19, 8): {'right': 1, 'up': 1},
    (20, 8): {'right': 1, 'up': 1},
    (21, 8): {'right': 1, 'up': 1},
    (22, 8): {'right': 1, 'up': 1}, 
    (0, 9): {'right': 1, 'down': 1, 'up': 1}, 
    (1, 9): {'right': 1, 'down': 1, 'up': 1},
    (2, 9): {'right': 1, 'down': 1, 'up': 1},
    (3, 9): {'right': 1, 'down': 1, 'up': 1},
    (4, 9): {'right': 1, 'down': 1, 'up': 1},
    (5, 9): {'right': 1, 'down': 1, 'up': 1},
    (6, 9): {'right': 1, 'down': 1, 'up': 1},
    (7, 9): {'right': 1, 'down': 1, 'up': 1},
    (8, 9): {'right': 1, 'down': 1, 'up': 1},
    (9, 9): {'right': 1, 'down': 1, 'up': 1},
    (10, 9): {'right': 1, 'down': 1, 'up': 1},
    (11, 9): {'right': 1, 'down': 1, 'up': 1},
    (12, 9): {'right': 1, 'down': 1, 'up': 1},
    (13, 9): {'right': 1, 'down': 1, 'up': 1},
    (14, 9): {'right': 1, 'down': 1, 'up': 1},
    (15, 9): {'right': 1, 'down': 1, 'up': 1},
    (16, 9): {'right': 1, 'down': 1, 'up': 1},
    (17, 9): {'right': 1, 'down': 1, 'up': 1},
    (18, 9): {'right': 1, 'down': 1, 'up': 1},
    (19, 9): {'right': 1, 'down': 1, 'up': 1},
    (20, 9): {'right': 1, 'down': 1, 'up': 1},
    (21, 9): {'right': 1, 'down': 1, 'up': 1},
    (22, 9): {'right': 1, 'down': 1, 'up': 1},
    (0, 10): {'right': 1, 'down': 1},
    (1, 10): {'right': 1, 'down': 1},
    (2, 10): {'right': 1, 'down': 1},
    (3, 10): {'right': 1, 'down': 1},
    (4, 10): {'right': 1, 'down': 1},
    (5, 10): {'right': 1, 'down': 1},
    (6, 10): {'right': 1, 'down': 1},
    (7, 10): {'right': 1, 'down': 1},
    (8, 10): {'right': 1, 'down': 1},
    (9, 10): {'right': 1, 'down': 1},
    (10, 10): {'right': 1, 'down': 1},
    (11, 10): {'right': 1, 'down': 1},
    (12, 10): {'right': 1, 'down': 1, 'up': 1},
    (13, 10): {'right': 1, 'down': 1, 'up': 1},
    (14, 10): {'right': 1, 'down': 1, 'up': 1},
    (15, 10): {'right': 1, 'down': 1},
    (16, 10): {'right': 1, 'down': 1},
    (17, 10): {'right': 1, 'down': 1},
    (18, 10): {'right': 1, 'down': 1},
    (19, 10): {'right': 1, 'down': 1},
    (20, 10): {'right': 1, 'down': 1},
    (21, 10): {'right': 1, 'down': 1},
    (22, 10): {'right': 1, 'down': 1}, 
    (8, 11): {'down': 1, 'right': 1},
    (9, 11): {'down': 1, 'right': 1, 'left': 1},
    (10, 11): {'down': 1, 'left': 1},
    (12, 11): {'up': 1, 'right': 1},
    (13, 11): {'up': 1, 'right': 1, 'left': 1},
    (14, 11): {'up': 1, 'left': 1},
    (0, 12): {'left': 1, 'up': 1}, 
    (1, 12): {'left': 1, 'up': 1},
    (2, 12): {'left': 1, 'up': 1},
    (3, 12): {'left': 1, 'up': 1},
    (4, 12): {'left': 1, 'up': 1},
    (5, 12): {'left': 1, 'up': 1},
    (6, 12): {'left': 1, 'up': 1},
    (7, 12): {'left': 1, 'up': 1},
    (8, 12): {'left': 1, 'up': 1, 'down': 1},
    (9, 12): {'left': 1, 'up': 1, 'down': 1},
    (10, 12): {'left': 1, 'up': 1, 'down': 1},
    (11, 12): {'left': 1, 'up': 1},
    (12, 12): {'left': 1, 'up': 1},
    (13, 12): {'left': 1, 'up': 1},
    (14, 12): {'left': 1, 'up': 1},
    (15, 12): {'left': 1, 'up': 1},
    (16, 12): {'left': 1, 'up': 1},
    (17, 12): {'left': 1, 'up': 1},
    (18, 12): {'left': 1, 'up': 1},
    (19, 12): {'left': 1, 'up': 1},
    (20, 12): {'left': 1, 'up': 1},
    (21, 12): {'left': 1, 'up': 1},
    (22, 12): {'left': 1, 'up': 1}, 
    (0, 13): {'left': 1, 'down': 1, 'up': 1}, 
    (1, 13): {'left': 1, 'down': 1, 'up': 1},
    (2, 13): {'left': 1, 'down': 1, 'up': 1},
    (3, 13): {'left': 1, 'down': 1, 'up': 1},
    (4, 13): {'left': 1, 'down': 1, 'up': 1},
    (5, 13): {'left': 1, 'down': 1, 'up': 1},
    (6, 13): {'left': 1, 'down': 1, 'up': 1},
    (7, 13): {'left': 1, 'down': 1, 'up': 1},
    (8, 13): {'left': 1, 'down': 1, 'up': 1},
    (9, 13): {'left': 1, 'down': 1, 'up': 1},
    (10, 13): {'left': 1, 'down': 1, 'up': 1},
    (11, 13): {'left': 1, 'down': 1, 'up': 1},
    (12, 13): {'left': 1, 'down': 1, 'up': 1},
    (13, 13): {'left': 1, 'down': 1, 'up': 1},
    (14, 13): {'left': 1, 'down': 1, 'up': 1},
    (15, 13): {'left': 1, 'down': 1, 'up': 1},
    (16, 13): {'left': 1, 'down': 1, 'up': 1},
    (17, 13): {'left': 1, 'down': 1, 'up': 1},
    (18, 13): {'left': 1, 'down': 1, 'up': 1},
    (19, 13): {'left': 1, 'down': 1, 'up': 1},
    (20, 13): {'left': 1, 'down': 1, 'up': 1},
    (21, 13): {'left': 1, 'down': 1, 'up': 1},
    (22, 13): {'left': 1, 'down': 1, 'up': 1}, 
    (0, 14): {'left': 1, 'down': 1}, 
    (1, 14): {'left': 1, 'down': 1},
    (2, 14): {'left': 1, 'down': 1},
    (3, 14): {'left': 1, 'down': 1},
    (4, 14): {'left': 1, 'down': 1},
    (5, 14): {'left': 1, 'down': 1},
    (6, 14): {'left': 1, 'down': 1},
    (7, 14): {'left': 1, 'down': 1},
    (8, 14): {'left': 1, 'down': 1},
    (9, 14): {'left': 1, 'down': 1},
    (10, 14): {'left': 1, 'down': 1},
    (11, 14): {'left': 1, 'down': 1},
    (12, 14): {'left': 1, 'down': 1, 'up': 1},
    (13, 14): {'left': 1, 'down': 1, 'up': 1},
    (14, 14): {'left': 1, 'down': 1, 'up': 1},
    (15, 14): {'left': 1, 'down': 1},
    (16, 14): {'left': 1, 'down': 1},
    (17, 14): {'left': 1, 'down': 1},
    (18, 14): {'left': 1, 'down': 1},
    (19, 14): {'left': 1, 'down': 1},
    (20, 14): {'left': 1, 'down': 1},
    (21, 14): {'left': 1, 'down': 1},
    (22, 14): {'left': 1, 'down': 1}, 
    (8, 15): {'down': 1, 'right': 1},
    (9, 15): {'down': 1, 'right': 1, 'left': 1},
    (10, 15): {'down': 1, 'left': 1},
    (12, 15): {'up': 1, 'right': 1},
    (13, 15): {'up': 1, 'right': 1, 'left': 1},
    (14, 15): {'up': 1, 'left': 1},
    (8, 16): {'down': 1, 'right': 1},
    (9, 16): {'down': 1, 'right': 1, 'left': 1},
    (10, 16): {'down': 1, 'left': 1},
    (12, 16): {'up': 1, 'right': 1},
    (13, 16): {'up': 1, 'right': 1, 'left': 1},
    (14, 16): {'up': 1, 'left': 1},
    (8, 17): {'down': 1, 'right': 1},
    (9, 17): {'down': 1, 'right': 1, 'left': 1},
    (10, 17): {'down': 1, 'left': 1},
    (12, 17): {'up': 1, 'right': 1},
    (13, 17): {'up': 1, 'right': 1, 'left': 1},
    (14, 17): {'up': 1, 'left': 1},
    (8, 18): {'down': 1, 'right': 1},
    (9, 18): {'down': 1, 'right': 1, 'left': 1},
    (10, 18): {'down': 1, 'left': 1},
    (12, 18): {'up': 1, 'right': 1},
    (13, 18): {'up': 1, 'right': 1, 'left': 1},
    (14, 18): {'up': 1, 'left': 1},
    (8, 19): {'down': 1, 'right': 1},
    (9, 19): {'down': 1, 'right': 1, 'left': 1},
    (10, 19): {'down': 1, 'left': 1},
    (12, 19): {'up': 1, 'right': 1},
    (13, 19): {'up': 1, 'right': 1, 'left': 1},
    (14, 19): {'up': 1, 'left': 1},
    (8, 20): {'down': 1, 'right': 1},
    (9, 20): {'down': 1, 'right': 1, 'left': 1},
    (10, 20): {'down': 1, 'left': 1},
    (12, 20): {'up': 1, 'right': 1},
    (13, 20): {'up': 1, 'right': 1, 'left': 1},
    (14, 20): {'up': 1, 'left': 1},
    (8, 21): {'down': 1, 'right': 1},
    (9, 21): {'down': 1, 'right': 1, 'left': 1},
    (10, 21): {'down': 1, 'left': 1},
    (12, 21): {'up': 1, 'right': 1},
    (13, 21): {'up': 1, 'right': 1, 'left': 1},
    (14, 21): {'up': 1, 'left': 1},
    (8, 22): {'down': 1, 'right': 1}, 
    (9, 22): {'down': 1, 'right': 1, 'left': 1},
    (10, 22): {'down': 1, 'left': 1}, 
    (12, 22): {'up': 1, 'right': 1},
    (13, 22): {'up': 1, 'right': 1, 'left': 1},
    (14, 22): {'up': 1, 'left': 1}
}

startList = [(12, 0), (13, 0), (14, 0), (0, 8), (0, 9), (0, 10), 
             (22, 12), (22, 13), (22, 14), (8, 22), (9, 22), (10, 22)]

endList = [(8, 0), (9, 0), (10, 0), (22, 8), (22, 9), (22, 10), 
           (0, 12), (0, 13), (0, 14), (12, 22), (13, 22), (14, 22)]

#Semaphores = [ (( 9, 15), "red"), (( 15, 13), "red"), ((7, 9), "red"), (( 13, 7), "red") ]
Semaphores = [  (( 9, 15), "red"), (( 15, 13), "red"), ((7, 9), "red"), (( 13, 7), "red")]
#   izquierda arriba, derecha arriba, izquierda abajo, derecha abajo,