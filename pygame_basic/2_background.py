import pygame

pygame.init() # 초기화

# 화면 크기 설정

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game') # 게임 이름

background = pygame.image.load('C:/Users/nexys/PycharmProjects/mskim/pygame_basic/background.png')

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 어떤 이벤트인지
            running = False

    screen.fill((100,100,100)) # 화면 체우기
    # screen.blit(background,(0,0)) # 배경 그리기
    
    pygame.display.update() # 화면 다시 그리기

# pygame 종료
pygame.quit()