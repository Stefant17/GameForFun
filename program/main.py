import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
list_caracters = []

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255, 255, 0)
#main caracter equipment
#             name,  health, weapon_attack, health_potions, mana_potions, Spells 
caracter_info["stefan",  100,  10 , 3 , 2 , [heal, fireball, arcane missles]]


# initial enemy location for developmennt
#             x     y  id     name  lvl health  attak 
enemyList = [[[60, 500], 1 , "dragon" , 2  , 200    , 20] ]
enemy_available = []

def initialize():
#  amount = input('how manny caracters?')
#  for i in range(int(amount)):
  list_caracters.append(create_caracter())
  
def create_caracter():
#  done = False
#  while done == False:
#    for i in pygame.get.event():
#      if event.type == pygame.KEYDOWN:
#        if event.key == pygame
  name = input("what is the name of this caracter? ")
  lvl = 1
  AC = input("what is your armor class? ")
  HP = input("what is your caracters HP ")
  Speed = input("the speed of the caracter? ")
  STR = input("how strong? ")
  DEX = input("DEX? ")
  CON = input("CON? ")
  INT = input("INT? ")
  WIS = input("WIS? ")
  CHA = input("CHA? ")
  skills = []
  skill = input("what is your skill? ")
  skills.append(skill)
  sence = "darksight"
  sences = [sence]
  languages = ["common toung"]
  challange = 0 
  list_caracters.append([name,lvl,AC,HP,Speed,STR,DEX,CON,INT, WIS, CHA, skills, languages])

def main(): 
##  initialize()
  global enemyList
  x_cord = 67 
  y_cord = 540
  gameDisplay.fill(white)
  pygame.display.update()
  GameExit = False
  while GameExit == False:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          GameExit = True
        if event.key == pygame.K_q:
          #if the Q key is pressed, quit the game 
          gameExit = True
        
        elif event.key == pygame.K_LEFT:
          # if the left key is pressed, the player x-coordinates will move left for 50 pixles (jump_movement) if the player is not out of bounds
          x_cord = x_cord - 5
          movement(x_cord, y_cord)
        elif event.key == pygame.K_RIGHT:
          # if the right key is pressed the x-coordinates of the player will be moved right 50 pixles (jump_movemnt) if the player is not out of bounds
          x_cord = x_cord + 5
          movement(x_cord, y_cord)
        elif event.key == pygame.K_DOWN:
          y_cord = y_cord + 5
          movement(x_cord, y_cord)
        elif event.key == pygame.K_UP:
          y_cord = y_cord - 5
          movement(x_cord, y_cord)
    if (check_if_hit(x_cord,y_cord)):
      combat(1)
      enemyList[0][0][0] = 0
      enemyList[0][0][1] = 0

def movement(X_cord, y_cord):
  global enemyList
  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, red, [ X_cord, y_cord , 30, 30])
  pygame.draw.rect(gameDisplay, red, [enemyList[0][0][0], enemyList[0][0][1] , 20, 20])
  pygame.display.update()

def combat(enemy_id): 
  global enemyList
  monster_health = 0
  lvl = 0
  monster_name = "a"
  monster_attack = 0 
  for i in enemyList:
    if i[1] == enemy_id:
      monster_name = i[2]
      lvl = i[3]
      monster_health = i[4]
      monster_attack = i[5]
  gameDisplay.fill(white)
  pygame.display.update()
  MonsterHealth = 100 
  PlayerHealth = 100
  winner = False
  print(monster_name)
  while (winner == False):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
          monsterHealth -= weaponDamage
          if monsterHealth <= 0:
            winner = True
        if event.key == pygame.K_p:
          player_health += 50
        if event.key == pygame.K_q:
          winner = True

def check_if_hit(x_cord, y_cord):
  global enemyList
  for i in enemyList:
    if x_cord > i[0][0] and x_cord < i[0][0]+35 or x_cord + 30 > i[0][0] and x_cord + 30 < i[0][0] + 35:
      if y_cord > i[0][1] and y_cord < i[0][1]+ 35 or y_cord+35 > i[0][1] and y_cord + 30 < i[0][1] + 35:
        return True






main()