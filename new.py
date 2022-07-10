import random

class Player:
    def __init__(self, name, drink_limit, drink_amount):
      self.name = name # 이름
      self.drink_limit = drink_limit # 주량
      self.drink_amount = drink_amount # 현재까지 마신 잔의 수
      self.rejection = 0 # 좋아게임 거절

class Game:
    def __init__(self):
      self.player = []  # 플레이어 목록
      self.user_name = ""  # 사용자 이름

    def set_game(self):
      '''술게임 시작 전 필요한 것들을 진행하는 함수'''
      # TODO 1
      # (1) 게임을 진행할까요? (y/n)
      ans = input("게임을 진행할까요? (y/n) : ")
      if ans == "y":
        # (2) 사용자 이름 받기
        self.name = input("오늘 거하게 취해볼 당신의 이름은? : ")
        # (3) 본인의 주량 선택하기
        print("~" * 20, end="")
        print("소주 기준 당신의 주량은? ", end="")
        print("~" * 20)
        print("1. 소주 반병(2잔)")
        print("2. 소주 반병에서 한병(4잔)")
        print("3. 소주 한병에서 한병 반(6잔)")
        print("4. 소주 한병 반에서 두병(8잔)")
        print("5. 소주 두병 이상(10잔)")
        print("~" * 70)
        while True:
          try:
            self.drink_limit = int(input("당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요) : "))
            if self.drink_limit < 1 or self.drink_limit > 5:
              raise ValueError
            break
          except ValueError:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")

        # (4) 같이 대결할 사람 초대하기 & 게임 리스트 출력하기 
        list_name = ["은서", "하연", "연서", "예진", "헌도"]
        while True:
          try:
            num = int(input("함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : "))
            if num < 1 or num > 3:
              raise ValueError
          except ValueError:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
          else:
            alist = []
            for i in range(num):
                a = random.randint(0, 4)
                while a in alist:
                  a = random.randint(0, 4)
                self.player.append(Player(list_name[a], (a + 1) * 2, 0))
                alist.append(a)
                print(f"오늘 함께 취할 친구는 {self.player[i].name}입니다! (치사량 : {self.player[i].drink_limit})")
            self.player.append(Player(self.name, self.drink_limit, 0))
            break
        print("~" * 70)
      else:
        print("게임을 진행하지 않습니다.")
        exit()

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

      # self.play_game()
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
      reaction = ["캌 퉤", "나도 좋아"]
      name = input("술도 마셨는데 좋아게임할까? ")
      while True:
        try:
          flag = False
          for i in range(len(self.player)):
            if name[0:2] in self.player[i].name:
              flag = True
          if flag == False:
            raise ValueError
        except ValueError:
          print("잘못 입력하셨습니다. 다시 입력해주세요.")
        else:
          react = random.randint(0, 1)
          print(reaction[react])

          if react == 0: # 칵 퉤
            while True:
              for i in range(len(self.player)):
                if name[0:2] == self.player[i].name:
                  self.player[i].rejection += 1
                  if self.player[i].rejection == 3:
                    self.player[i].drink_amount += 1

              list = []
              for i in range(len(self.player)):
                if name[0:2] != self.player[i].name:
                  list.append(i)
              a = random.randint(0, len(list) - 1)
              if a != len(list) - 1:
                print(self.player[list[a]].name, "좋아!")

              react = random.randint(0, 1)
              if react == 1:
                break    
          else: # 나도 좋아
              list = []
              for i in range(len(self.player)):
                if name[0:2] != self.player[i].name:
                  list.append(i)
              a = random.randint(0, len(list) - 1)
              if a != len(list) - 1:
                print(self.player[list[a]].name, "좋아!")
              else:
                input()
                
    def game_5(self):
      '''술게임 5 (크롤링)'''
      # TODO 7


game = Game()
game.game()