# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Define some colors
WHITE    = ( 255, 255, 255)
MISTYROSE = (255,228,225)
LAVENDERBLUSH = (255,240,245)

size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe Tum")
print("Let's get jiggy with it!")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def drawX(screen, x, y):
    pygame.draw.line(screen, WHITE, [y*100, x*100], [y*100+100, x*100+100], 5)
    pygame.draw.line(screen, WHITE, [y*100+100, x*100], [y*100, x*100+100], 5)

def drawO(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [10 + y*100, 10 + x*100, 80, 80])    

Xarr = []
Oarr = []
total = []
symbol = True
gameOver = False

def won(arr):
    count = 0
    n0 = 0
    n1 = 0
    n2 = 0
    for (x, y) in arr:
        if x == 0: n0 += 1
        elif x == 1: n1 += 1
        else: n2 += 1
        if (x, y) == (0, 0) or (x, y) == (1, 1) or (x, y) == (2, 2):
            count += 1
    if n0 == 3 or n1 == 3 or n2 == 3 or count == 3:
        return True
    count = 0
    n0 = 0
    n1 = 0
    n2 = 0
    for (m, x) in arr:
        if x == 0: n0 += 1
        elif x == 1: n1 += 1
        else: n2 += 1
        if (m, x) == (2, 0) or (m, x) == (1, 1) or (m, x) == (0, 2):
            count += 1
    if n0 == 3 or n1 == 3 or n2 == 3 or count == 3:
        return True

def spotTaken(x, y):
    for (m, n) in total:
        if x == m and y == n:
            return True
    return False

# -------- Main Program Loop -----------
while not done and not gameOver:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            print("See ya!")
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if spotTaken(int(pos[1]/100), int(pos[0]/100)):
                print("That spot's taken, dummy!")
            else:
                if symbol:
                    Xarr.append((int(pos[1]/100), int(pos[0]/100)))
                    total.append((int(pos[1]/100), int(pos[0]/100)))
                    if won(Xarr):
                        print("Player X won! Get rekt Player O!")
                        gameOver = True
                else:
                    Oarr.append((int(pos[1]/100), int(pos[0]/100)))
                    total.append((int(pos[1]/100), int(pos[0]/100)))
                    if won(Oarr):
                        print("Player O won! Get rekt Player X!")
                        gameOver = True
                if (not won(Xarr) and not won(Oarr) and len(total) == 9):
                    gameOver = True
                    print("You both suck!")
                symbol = not symbol

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # --- Drawing code should go here
    pygame.draw.rect(screen, MISTYROSE, [0, 0, 100, 100])
    pygame.draw.rect(screen, LAVENDERBLUSH, [100, 0, 100, 100])
    pygame.draw.rect(screen, MISTYROSE, [200, 0, 100, 100])
    pygame.draw.rect(screen, LAVENDERBLUSH, [0, 100, 100, 100])
    pygame.draw.rect(screen, MISTYROSE, [100, 100, 100, 100])
    pygame.draw.rect(screen, LAVENDERBLUSH, [200, 100, 100, 100])
    pygame.draw.rect(screen, MISTYROSE, [0, 200, 100, 100])
    pygame.draw.rect(screen, LAVENDERBLUSH, [100, 200, 100, 100])
    pygame.draw.rect(screen, MISTYROSE, [200, 200, 100, 100])

    pygame.draw.line(screen, WHITE, [100, 0], [100, 300], 5)
    pygame.draw.line(screen, WHITE, [200, 0], [200, 300], 5)
    pygame.draw.line(screen, WHITE, [0, 100], [300, 100], 5)
    pygame.draw.line(screen, WHITE, [0, 200], [300, 200], 5)

    for (x, y) in Xarr:
        drawX(screen, x, y)
    for (x, y) in Oarr:
        drawO(screen, x, y)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()
