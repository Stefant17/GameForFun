import pygame
import gameover as gameover 
white = (255,255,255)
red = (255,0,0)

def combat(enemy_id, enemyList, caracter_info, gameDisplay): 
  monster_health = 0
  lvl = 0
  monster_name = "a"
  monster_attack = 0 
  player_name = caracter_info[0]
  PlayerHealth = caracter_info[1]
  weaponDamage = caracter_info[2]
  for i in enemyList:
    if i[1] == enemy_id:
      monster_name = i[2]
      lvl = i[3]
      monster_health = i[4]
      monster_attack = i[5]
      img_location = i[6]
  display_enemy(gameDisplay, img_location)
  winner = False
  print(monster_name)
  while (winner == False):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
          monster_health -= weaponDamage
          if monster_health <= 0:
            print('you won!! ')
            return enemy_id
        elif event.key == pygame.K_p:
          player_health += 50
        elif event.key == pygame.K_q:
          return enemy_id
        elif event.key == pygame.K_a:
          caracter_info[1] -= 10
          if caracter_info[1] <= 0:
            gameover.gameover()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if button(150,500,100,30):
          monster_health = attack(caracter_info, monster_health)
          if (monster_health <= 0):
            return enemy_id
        if button(350, 500, 100, 30):
          potion(caracter_info[1], 30)
        if button(550, 500, 100, 30):
          inventory(caracter_info[6])


def display_enemy(gameDisplay, img_location):
  gameDisplay.fill(white)
  img = pygame.image.load(img_location)
  img = pygame.transform.scale(img, (500, 400))
  gameDisplay.blit(img, (100, 50))
  pygame.draw.rect(gameDisplay,red ,[150, 500, 100, 30])
  pygame.draw.rect(gameDisplay,red ,[350, 500, 100, 30])
  pygame.draw.rect(gameDisplay,red ,[550, 500, 100, 30])
  pygame.display.update()

def button( x, y , width, height):
  cur = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if x + width > cur[0] > x and y + height > cur[1] > y:
    if click[0] == 1:
      return True

def attack(caracter_info, monster_health):
  return monster_health - caracter_info[2]

def potion(caracter_health, potion):
  return caracter_health + potion

def inventory(inventory): 
  return 0 #hugmyndin var a[ ýta á takka og svo breytir það vopninu sem þú ert með en er að íhugsa hluti
