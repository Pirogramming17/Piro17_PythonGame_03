import random

class Player:
    def __init__(self, name, drink_limit, drink_amount):
      self.name = name # 이름
      self.drink_limit = drink_limit # 주량
      self.drink_amount = drink_amount # 현재까지 마신 잔의 수

class Game:
    def __init__(self):
      self.player = []  # 플레이어 목록
      self.user_name = ""  # 사용자 이름

    def set_game(self):
      '''술게임 시작 전 필요한 것들을 진행하는 함수'''
    
      # TODO 1
      # (1) 게임을 진행할까요? (y/n)
      # (2) 사용자 이름 입력받기
      # (3) 주량 선택하기
      # (4) 플레이어들을 self.player에 할당함
      # self.player.append(Player("name(심은서)", drink_limit(랜덤), drink_amount(0)))
      # self.player.append(Player("name(조하연)", drink_limit(랜덤), drink_amount(0)))
      # self.player.append(Player("name(조연서)", drink_limit(랜덤), drink_amount(0)))
      # self.player.append(Player("name(박예진)", drink_limit(랜덤), drink_amount(0)))
      # self.player.append(Player("name(이헌도)", drink_limit(랜덤), drink_amount(0)))
      # self.player.append(Player("name(사용자가 입력한 이름)", drink_limit(사용자가 선택한 주량), drink_amount(0)))
    
      # (5) 같이 대결할 사람 초대하기(최대 몇명?)
      
    def play_game(self, turn_player):
      '''술게임을 진행하는 함수'''

      # TODO 2

      wave = 69 # 물결수-> 나중에 제거
      dead = False # 누군가 사망유뮤
      dead_player = '' # 사망한 플레이어이름

      # (1) 현재 마신 잔 수, 치사량까지 남은 잔 수 계산 및 출력
      print('~'*wave)

      for i in range(len(self.player)):
        print(f'{self.player[i].name}은(는) 지금까지 {self.player[i].drink_amount}잔! 치사량까지 {self.player[i].drink_limit}')
        if self.player[i].drink_limit <= 0:
          dead = True
          dead_player = self.player[i].name

      print('~'*wave)
      # 누군가 죽었을때 -> 게임종료
      if dead:
        print(f'{dead_player}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz')
        print('~'*wave)
        print(' '*20,"잔 다음에 술마시면 또 불러주세요~ 안녕! 잔")
        print('~'*wave)
        exit()

      # (2) 게임 리스트 출력
      print('~'*20," 잔 오늘의 Alcohol GAME 잔 ",'~'*20)
      print(' '*20," 잔 1. 사랑의 총알 게임")
      print(' '*20," 잔 2. 좋아 게임")
      print(' '*20," 잔 3. 369 게임")
      print(' '*20," 잔 4. 두부 게임")
      print(' '*20," 잔 5. 초성 게임")

      print('~'*wave)
      # (3) 게임 선택 - 현재 차례가 사용자이면 입력을 받고, 컴퓨터면 랜덤 선택
      if turn_player == 5: # turn_player 가 사용자일 때
        start_key : input('술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"를, 계속하고 싶으면 아무키나 입력해 주세요! :')
        if start_key == 'exit':
          print('술게임을 종료합니다.안녕~')
          print('~'*wave)
          exit() 
        else:
          while True:
            try:
              selected_game = int(input(f'{self.player[turn_player].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : ')) 
            except ValueError:
              print('잘못 선택하셨습니다. 다시 선택해 주세요.')
            if selected_game <= 0 or selected_game > 5:
              print('잘못 선택하셨습니다. 다시 선택해 주세요.')
            else:
              break
      else: # turn_player 가 컴퓨터일 때
        selected_game = random.randint(1,5) #import 해야됨
        print(f'{self.player[turn_player].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : {selected_game}')

      print('~'*wave)
      # (4) 선택된 게임 함수 호출
      if selected_game == 1:
        self.game_1()
      elif selected_game == 2:
        self.game_2()
      elif selected_game == 3:
        self.game_3()
      elif selected_game == 4:
        self.game_4()
      elif selected_game == 5:
        self.game_5()
      # (5) 치사량에 도달한 사람이 생기면 게임 종료 ->(1)안에서 처리         

    def game(self):
      ''' 게임을 실행하는 함수'''
    
      #술게임 시작 전 필요한 것들을 세팅
      self.set_game()
      #술게임 진행
      self.play_game(5)


    #매 술게임이 끝날 때마다 벌칙자(술마시는 사람)이 결정되고, 그 사람의 마신 잔 수를 ++해줘야 함.

    def game_1(self):
      '''술게임 1'''
      # TODO 3

    def game_2(self):
      '''술게임 2'''
      # TODO 4

    def game_3(self):
      '''술게임 3'''
      # TODO 5

    def game_4(self):
      '''술게임 4'''
      # TODO 6

    def game_5(self):
      '''술게임 5 (크롤링)'''
      # TODO 7


game = Game()
game.game()