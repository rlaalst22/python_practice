import pygame
import random
pygame.init()  # 초기화

# 화면 크기 설정

screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')  # 게임 이름

clock = pygame.time.Clock()

background = pygame.image.load('C:/Users/nexys/PycharmProjects/mskim/pygame_basic/background.png')

# 케릭터 불러오기
character = pygame.image.load('C:/Users/nexys/PycharmProjects/mskim/pygame_basic/character.png')
character_size = character.get_rect().size # 이미지 크기 가져온다.
character_width = character_size[0] # 가로
character_height = character_size[1] # 세로
character_x_pos = screen_width/2 - character_width/2 # 화면 가로 중앙에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래 위치

to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6
enemy_speed = 0.8

# 적 enemy 캐릭터
enemy = pygame.image.load('C:/Users/nexys/PycharmProjects/mskim/pygame_basic/enemy.png')
enemy_size = character.get_rect().size # 이미지 크기 가져온다.
enemy_width = character_size[0] # 가로
enemy_height = character_size[1] # 세로
enemy_x_pos = screen_width/2 - enemy_width/2 # 화면 가로 중앙에 위치
enemy_y_pos = 0 # 화면 세로 크기 가장 아래 위치

# 폰트 정의
game_font = pygame.font.Font(None,40) # 폰트 객체 생성 ( 폰트,크기)

# 총 시간
total_time = 10

# 장애물 피한 수
obstacle_cnt = 0

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick 을 받아옴

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(144) # 초당 프레임 수 설정

    for event in pygame.event.get(): # 어떤 이벤트인지
        if event.type == pygame.QUIT: # 창 닫기 버튼 클릭
            running = False

        if event.type ==pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    enemy_y_pos += (enemy_speed+(0.01*(obstacle_cnt+1))) * dt

    if character_x_pos>screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_x_pos<0:
        character_x_pos = 0

    if enemy_y_pos>=screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.random()*screen_width
        obstacle_cnt += 1

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('충돌')
        running = False

    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) # 케릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # 적 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간 1000으로 나눠서 초 단위로 표시

    # timer = game_font.render(str(int(elapsed_time)),True,(0,0,0))
    cnt = game_font.render(str(int(obstacle_cnt)),True,(0,0,0))

    screen.blit(cnt,(10,10))

    # if total_time - elapsed_time <= 0:
    #     print("타임아웃")
    #     running = False

    pygame.display.update()  # 화면 다시 그리기

pygame.time.delay(2000)

# pygame 종료
pygame.quit()