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
      
    def play_game(self):
      '''술게임을 진행하는 함수'''

      # TODO 2
      # (1) 현재 마신 잔 수, 치사량까지 남은 잔 수 계산 및 출력
      # (2) 게임 리스트 출력
      # (3) 게임 선택 - 현재 차례가 사용자이면 입력을 받고, 컴퓨터면 랜덤 선택
      # (4) 선택된 게임 함수 호출
      # (5) 치사량에 도달한 사람이 생기면 게임 종료          

    def game(self):
      ''' 게임을 실행하는 함수'''
    
      #술게임 시작 전 필요한 것들을 세팅
      self.set_game()
      #술게임 진행
      self.play_game()


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