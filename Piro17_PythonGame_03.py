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
      self.turn_player = ""

    def set_game(self):
      '''술게임 시작 전 필요한 것들을 진행하는 함수'''
      # TODO 1
     
     
    def play_game(self):
      '''술게임을 진행하는 함수'''

        

    def decideTurn(self) :



    #매 술게임이 끝날 때마다 벌칙자(술마시는 사람)이 결정되고, 그 사람의 마신 잔 수를 ++해줘야 함.

    def game_1(self): # 사랑의 총알 게임
      '''술게임 1'''
      # TODO 3
      





      
#       [사랑의 총알 게임]

# 인트로 : 사랑의~ 빵! 총알을~ 빵!
# 누구에게 쏠까요~ 빵빵!

# ① 인트로의 빵빵 때 각자 두 사람을 가리킨다.
# ② 가리킨 사람을 쏘며 한 손을 내린다.
# (맨 처음에 쏘는 사람은 손을 내리지 않는다)
# ③ 총알을 맞은 사람이 또다시 다른 사람을 쏜다.
# ④ 반복하여 총이 없는 상태(손을 다 내린 상태)에서 맞은 사람이 마신다.
# (총 3회 맞았을 때)

    def game_2(self): 
      '''술게임 2'''
      # TODO 4

    def game_3(self):
      '''술게임 3'''
      # TODO 5

    def game_4(self):
      '''술게임 4'''
      # [두부 게임 설명]
      # 1)참가자+ 두부n개 = 총 5개가 리스트 안에서 랜덤으로 섞여 배열을 만든다
      # 3) 두부 3모를 기준으로 왼쪽으로 갈 수록 1모씩 모 수가 감소하고, 오른쪽으로 갈 수록 1모씩 모 수가 증가한다.
      #  (Ex. 1모 2모 *3모* 4모 5모)
      # 4)5개 중 한개가 기준인 3모로 지목되어 공개된다.
      # 5) 지목된 기준인 3모를 기준으로 문제로 제시되는 n모에 해당하는 사람의 이름을 올바르게 말하면 정답. 틀리면 오답.
      
      tofu_player = []
      for n in range(len(self.player)):
        tofu_player.append(self.player[n].name)  
      
      tofu_match = dict()
      
      print("-"*35)
      print("\n두부두부두부✨ 으쌰으쌰으쌰으쌰!✨\n")
      print("두부 게임을 시작합니다.")
      print('\n🚨주의 사항: 문제에 알맞은 모 수에 해당하는 사람의 이름을 !똑같이! 입력하세요 (철자 틀릴 시 오답으로 간주)🚨\n')

      while True:
        if len(tofu_player) < 5:
          for i in range(1,5-len(tofu_player)+1):
            tofu_player.append(f'두부{i}')

        random.shuffle(tofu_player)
        print("-"*35)
        print("순서는 다음과 같습니다")
        print(tofu_player)

        std = random.randint(0,4)
        print(f"{tofu_player[std]}(이)가 3모입니다.")

        if std < 3:
          tofu_match[1] = tofu_player[std-2]
          tofu_match[2] = tofu_player[std-1]
          tofu_match[3] = tofu_player[std]
          tofu_match[4] = tofu_player[std+1]
          tofu_match[5] = tofu_player[std+2]
        elif std == 3:
          tofu_match[1] = tofu_player[std-2]
          tofu_match[2] = tofu_player[std-1]
          tofu_match[3] = tofu_player[std]
          tofu_match[4] = tofu_player[std+1]
          tofu_match[5] = tofu_player[std-3]
        else:
          tofu_match[1] = tofu_player[std-2]
          tofu_match[2] = tofu_player[std-1]
          tofu_match[3] = tofu_player[std]
          tofu_match[4] = tofu_player[std-4]
          tofu_match[5] = tofu_player[std-3]


        quiz = random.randint(1,5)
        
        while True:  
          if quiz == 3:
            quiz = random.randint(1,5)
          else:
            break

          
        while True: #사용자 차례에서는 input으로 답 받기
          if self.turn_player == len(self.player)-1:
            answer = input(f"\n❗QUIZ! - {self.player[self.turn_player].name} : {quiz}모는 누구일까요?: ")
            self.turn_player = 0
            break
          else:                            #컴퓨터 차례에는 랜덤으로 답 받기
            print(f"\n❗QUIZ! - {self.player[self.turn_player].name} : {quiz}모는 누구일까요?")
            t_f = random.randint(0,1)
            if t_f == 0:
                answer = tofu_match[quiz]
            else:
              w_answer = random.randint(1,5)
              while True:
                if w_answer == quiz:
                  w_answer = random.randint(1,5)
                else:
                  break
              w_answer = answer   
            print(f"{answer}입니다.")
            break
            
        if tofu_match[quiz] == answer:
          print("\n정답!")
          print("두부게임 계속 진행합니다")
          self.turn_player += 1
        else:
          print("\n틀렸습니다!")
          print(f'\n아 누가누가 술을 마셔😲 {self.player[self.turn_player].name}(가) 술을 마셔🤪 원~~~샷❗🧨 원샷!')
          self.player[self.turn_player].drink_amount += 1
          print("-"*7,"게임을 종료합니다.","-"*7)
          self.decideTurn()
          break
      
                
                
    def game_5(self):
      '''술게임 5 (크롤링)'''
      # TODO 7

game = Game()
game.game()

