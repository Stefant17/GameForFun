import pygame
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
  display_enemy(gameDisplay)
  winner = False
  print(monster_name)
  while (winner == False):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
          monster_health -= weaponDamage
          if monster_health <= 0:
            winner = True
        if event.key == pygame.K_p:
          player_health += 50
        if event.key == pygame.K_q:
          winner = True
      button(150,500,100,30)

def display_enemy(gameDisplay):
  gameDisplay.fill(white)
  pygame.draw.rect(gameDisplay, red, [100, 50 , 500 , 400])
  pygame.draw.rect(gameDisplay,red ,[150, 500, 100, 30])
  pygame.display.update()

def button( x, y , width, height):
  cur = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if x + width > cur[0] > x and y + height > cur[1] > y:
    if click[0] == 1:
      print("yes")
