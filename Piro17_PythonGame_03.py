from bdb import Breakpoint
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
            self.drink_limit = int(input("당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요) : "))*2
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
            self.player.append(Player(self.name, self.drink_limit * 2, 0))
            break
        self.turn_player = len(self.player)-1 #사용자가 첫번째 차례
        print("~" * 70)

      else:
        print("게임을 진행하지 않습니다.")
        exit()
     
    def play_game(self):
      '''술게임을 진행하는 함수'''
      wave = 69 # 물결수-> 나중에 제거
      dead_flag = False
      dead_player = '' # 사망한 플레이어이름
      
      while True :
        # (1) 현재 마신 잔 수, 치사량까지 남은 잔 수 계산 및 출력
        print('~'*wave)

        for i in range(len(self.player)):
          print(f'{self.player[i].name}은(는) 지금까지 {self.player[i].drink_amount}🍺! 치사량까지 {self.player[i].drink_limit - self.player[i].drink_amount}')
          if self.player[i].drink_limit - self.player[i].drink_amount == 0:
            dead_flag = True
            dead_player = self.player[i].name

        
        print('~'*wave)
        # 누군가 죽었을때 -> 게임종료
        if dead_flag:
          print(f'{dead_player}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz')
          print('~'*wave)
          print(' '*20,"🍺 다음에 술마시면 또 불러주세요~ 안녕! 🍺")
          print('~'*wave)
          exit() 

        # (2) 게임 리스트 출력
        print('~'*20," 🍺 오늘의 Alcohol GAME 🍺 ",'~'*20)
        print(' '*20," 🍺 1. 사랑의 총알 게임")
        print(' '*20," 🍺 2. 좋아 게임")
        print(' '*20," 🍺 3. 369 게임")
        print(' '*20," 🍺 4. 두부 게임")
        print(' '*20," 🍺 5. 초성 게임")

        print('~'*wave)
        # (3) 게임 선택 - 현재 차례가 사용자이면 입력을 받고, 컴퓨터면 랜덤 선택

        if self.turn_player == len(self.player)-1: # turn_player 가 사용자일 때
          while True:
            try:
              print(f'{self.player[self.turn_player].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : ', end='')
              selected_game = int(input()) 
            except ValueError:
              print('잘못 선택하셨습니다. 다시 선택해 주세요.')
            if selected_game < 0 or selected_game > 5:
              print('잘못 선택하셨습니다. 다시 선택해 주세요.')
            else:
              break
        else: # turn_player 가 컴퓨터일 때
          start_key = input('술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"를, 계속하고 싶으면 아무키나 입력해 주세요! :')
          if start_key == 'exit':
            print('술게임을 종료합니다. 안녕~')
            print('~'*wave)
            exit() 
          else:
            while True:
              try:
                selected_game = random.randint(1,5)
                print(f'{self.player[self.turn_player].name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨게임? : {selected_game}')
              except ValueError:
                print('잘못 선택하셨습니다. 다시 선택해 주세요.')
              if selected_game < 0 or selected_game > 5:
                print('잘못 선택하셨습니다. 다시 선택해 주세요.')
              else:
                break
          
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
        elif selected_game == 0:
          self.game_0()
        # (5) 치사량에 도달한 사람이 생기면 게임 종료 ->(1)안에서 처리  
        

    def decideTurn(self) :
      '''게임 순서를 바꾸는 함수'''
      if self.turn_player == len(self.player)-1 :
        self.turn_player = 0
      else :
        self.turn_player += 1

    def game(self):
      ''' 게임을 실행하는 함수'''
    
      #술게임 시작 전 필요한 것들을 세팅
      self.set_game()

      #술게임 진행
      self.play_game()


    #매 술게임이 끝날 때마다 벌칙자(술마시는 사람)이 결정되고, 그 사람의 마신 잔 수를 ++해줘야 함.

    def game_0(self):
      print('게임실행')
      print('사용자가 벌칙')
      self.player[-1].drink_amount += 1
      self.decideTurn()

    def game_1(self): # 사랑의 총알 게임
      '''술게임 1'''
      # TODO 3
      print(self.player[self.turn_player].name,'님이 술래! 😁')
      print('사랑의~ 빵! 😍 총알을~ 빵! 😉 누구에게 쏠까요~~ 빵빵!!')

      player_list = [] # list_tmp 리스트of 리스트 ex) [[1,2],[2,2],[0,1]]-> 자신을 제외한 2씩명 중복 지목
      list_tmp = [] # 임시 리스트
      selected_player = [] # 사용자가 선택한 사람2명의 리스트

      for i in range(len(self.player)):  
        if i == len(self.player)-1:  # 사용자일 때
          print(f'쏠 사람을 2명 선택하세요(띄어쓰기 1칸!) : ',end='')
          selected_player = (input().split())
          for j in range(len(self.player)):
            for k in range(2):
              if self.player[j].name == selected_player[k]:
                list_tmp.append(j)
          player_list.append(list_tmp) 
          list_tmp = [] 
        else:  # 컴퓨터일 때
          count = 0
          while count <= 2:
            num = random.randint(0,len(self.player)-1)
            if num != i:
              list_tmp.append(num)
              count += 1
          player_list.append(list_tmp) 
          list_tmp = []
          count = 0
      # 첫 턴 사람부터 총 쏘기
      next_player = self.turn_player
      while True:
        if len(player_list[next_player])!= 0:
          next_player = selected_player[next_player].pop(random.randint(0,1))
        else: # 손을 다 내린상태에서 맞았을 때 
          self.player[i].drink_amount += 1
          self.player[i].drink_limit -= 1
          self.play_game(i)





      
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

