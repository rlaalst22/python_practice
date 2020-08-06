import pygame

pygame.init()  # 초기화

# 화면 크기 설정

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')  # 게임 이름

background = pygame.image.load('C:/Users/nexys/PycharmProjects/mskim/pygame_basic/background.png')

# 케릭터 불러오기
character = pygame.image.load('C:/Users/nexys/PycharmProjects/mskim/pygame_basic/character.png')
character_size = character.get_rect().size # 이미지 크기 가져온다.
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = screen_width/2 - character_width/2 # 화면 가로 중앙에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래 위치


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트인지
        if event.type == pygame.QUIT: # 창 닫기 버튼 클릭
            running = False

    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()  # 화면 다시 그리기

# pygame 종료
pygame.quit()