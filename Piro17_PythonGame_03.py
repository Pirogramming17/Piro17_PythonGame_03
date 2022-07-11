import random
import requests

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
              if selected_game < 0 or selected_game > 5:
                raise ValueError
            except ValueError:
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

    def game_1(self): # 사랑의 총알 게임
      '''술게임 2'''
      # TODO 3
      print(self.player[self.turn_player].name,'님이 술래! 😁\n')
      print('사랑의~ 빵! 😍 총알을~ 빵! 😉 누구에게 쏠까요~~ 빵빵!!\n')

      player_list = [] # list_tmp 리스트of 리스트 ex) [[1,2],[2,2],[0,1]]-> 자신을 제외한 2씩명 중복 지목
      list_tmp = [] # 임시 리스트
      selected_player = [] # 사용자가 선택한 사람2명의 리스트

      for i in range(len(self.player)):  
        if i == len(self.player)-1:  # 사용자일 때
          while True:
            if len(self.player) == 2:
              print(f'총 인원이 2명이므로 상대방이름만을 2번 입력 하세요(띄어쓰기 1칸!) : ',end='')
              selected_player = (input().split())
            else:
              print(f'쏠 사람을 2명 선택하세요(띄어쓰기 1칸!) : ',end='')
              selected_player = (input().split())
            try:
              for i in range(2):
                if self.player[self.turn_player].name == selected_player[i]:
                  print('자신은 지목 불가!. 다시 선택해 주세요.')
              break
            except IndexError:
              print('잘못 선택하셨습니다. 다시 선택해 주세요.')
          print('\n')
          for j in range(len(self.player)):
            for k in range(2):
              if self.player[j].name == selected_player[k]:
                list_tmp.append(j)
          player_list.append(list_tmp) 
          list_tmp = [] 
        else:  # 컴퓨터일 때
          cnt = 0
          while cnt < 2:
            num = random.randint(0,len(self.player)-1)
            if num != i:
              list_tmp.append(num)
              cnt += 1
          player_list.append(list_tmp) 
          list_tmp = []
          cnt = 0
      for i in range(len(player_list)): #처음 두명씩 가리키는 모습
        print(f'{self.player[i].name}: 👉 {self.player[player_list[i][0]].name} 👉 {self.player[player_list[i][1]].name}')
      print('\n')
      print('='*20)
      # 첫 턴 사람부터 총 쏘기
      next_player = self.turn_player
      while True:
        if len(player_list[next_player])!= 0:
          print(f'{self.player[next_player].name}:',end='')
          next_player = player_list[next_player].pop(random.randint(0,len(player_list[next_player])-1))
          print(f' 👉 {self.player[next_player].name} 빵!!\n\n')
          for i in range(len(player_list)):
            print(f'{self.player[i].name}:',end='')
            for j in range(len(player_list[i])):
              print(f' 👉 {self.player[player_list[i][j]].name}',end='')
            print('\n')
          print('='*20)
        else: # 손을 다 내린상태에서 맞았을 때 
          self.player[next_player].drink_amount += 1
          #self.player[next_player].drink_limit -= 1
          print(f'{self.player[next_player].name} : 😱 으악!! 😱')
          self.decideTurn()
          self.play_game()

    def game_2(self): 
      '''술게임 2'''
      # TODO 4

      reaction = ["캌 퉤", "나도 좋아"]
      now = self.player[len(self.player) - 1].name
      user = self.player[len(self.player) - 1].name
      cnt = 0
      
      print("❗현재 사람들 중 한명을 지목하여 ㅇㅇ 좋아!를 입력해주세요 (본인 제외)❗")
      while True:
        try:              
          name = input("술도 마셨는데 좋아게임할까? ")[0:2]
          flag = False
          for i in range(len(self.player)):
            if name in self.player[i].name:
              flag = True
          if flag == False:
            raise ValueError
          if name == now: # 본인 지목
            raise ValueError
        except ValueError:
          print("잘못 입력하셨습니다. 다시 입력해주세요.")
        else:
          while True:
            list = []
            if cnt != 0:
              if react != 0:
                for i in range(len(self.player)):
                  if self.player[i].name != now:
                    list.append(i)
                a = random.randint(0, len(list) - 1)
                name = self.player[list[a]].name
              print(now, ":", name, "좋아!")
              if name == user:
                while True:
                  res = input("'캌 퉤'와 '나도 좋아' 둘 중에 입력해주세요. ")
                  if res == "캌 퉤":
                    react = 0
                    break
                  elif res == "나도 좋아":
                    react = 1
                    break
            cnt += 1
            if name != user:
              react = random.randint(0, 1)
              if react == 0:
                print("➡ ", name, ":", reaction[0], "😂")
              elif react == 1:
                print("➡ ", name, ":", reaction[1], "😍")

            if react == 0: # 칵 퉤
              for i in range(len(self.player)):
                if now == self.player[i].name:
                  self.player[i].rejection += 1
                  if self.player[i].rejection == 3:
                    self.player[i].drink_amount += 1
                    print(f"아 누가누가 술을 마셔😲 {now}이(가) 술을 마셔🤪 원~~~샷❗🧨")
                    self.decideTurn()
                    return
                  for i in range(len(self.player)):
                    if self.player[i].name != now:
                      list.append(i)
                  a = random.randint(0, len(list) - 1)
                  name = self.player[list[a]].name
            elif react == 1: # 나도 좋아
                now = name

    def game_3(self):
      '''술게임 3'''
      # TODO 5
      print('(ง˙∇˙)ว 삼육구 삼육구 삼육구 삼육구 (ง˙∇˙)ว')
      your_turn = ''
      cur_num = 1
      is_go = True

      #입력값에 3,6,9가 들어있는지 확인 하는 함수
      def claps(cur_num):
          cur_num_str = str(cur_num)
          count_369 = 0

          c = str(cur_num).count('3')+str(cur_num).count('6')+str(cur_num).count('9')
          if c==0: #3,6,9가 포함되어 있지 않는 경우
              count_369 = 0
              return count_369
          else: # 3,6,9가 포함되어 있는 경우
              count_369 = 1*c
              return count_369

      #'짝' 리턴하는 함수
      def to_clap(count_369, clap_sound = '짝'):
          return count_369 * clap_sound

      #사용자가 제대로 입력했는지 확인하는 함수
      def you_right(cur_num, your_turn):
          count_369 = claps(cur_num)
          if count_369 != 0 and your_turn in to_clap(count_369): #짝 차례
              return 1
          elif count_369 == 0 and your_turn == str(cur_num): #숫자 차례
              return 2
          else:
              return False

      while is_go == True:
          flag = True
          num_ran = random.randint(1,10)
          count_369 = claps(cur_num)
          for i in range(len(self.player)-1):
              count_369 = claps(cur_num)
              if num_ran != 2:
                  if count_369 == 0:
                      print(self.player[i].name,f': {cur_num}')
                  else:
                      print(self.player[i].name,f': {to_clap(count_369)}')
                  cur_num += 1
              else:
                  if count_369 == 0:
                    print(self.player[i].name, '짝')
                  elif count_369 == 1:
                    print(self.player[i].name,f': {cur_num}')
                  else:
                      print(self.player[i].name,'짝')
                  print(self.player[i].name,'벌칙!')
                  print('아 누가누가 술을 마셔😲',self.player[i].name,'이(가) 술을 마셔🤪 원~~~샷❗🧨')
                  self.player[i].drink_amount += 1
                  flag = False
                  break
          if flag == False:
            break

          your_turn = input("네 차례: ")
          if you_right(cur_num, your_turn) == 1:
              cur_num += 1
              continue
          if you_right(cur_num, your_turn) == 2:
              cur_num += 1
              continue
          else:
              print(self.user_name, '벌칙!')
              print('아 누가누가 술을 마셔😲',self.player[-1].name,'이(가) 술을 마셔🤪 원~~~샷❗🧨')
              self.player[-1].drink_amount += 1
              is_go = False
          self.decideTurn()

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
      
      turn = self.turn_player #게임을 고른 사람부터 시작
      characters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉ';
      choseong = ''.join(i for i in [random.choice(characters) for j in range(2)]) #랜덤 초성 발생
      ans_list = [] #이미 나온 답을 저장하는 리스트
      wrong_flag = False #틀렸는지 알려주는 플래그

      word_list = []
      url = f"https://wordrow.kr/초성/{choseong}" 
      response = requests.get(url)

      from bs4 import BeautifulSoup as bs
      soup = bs(response.text, "html.parser")

      raw_words = soup.select(".sub-heading + .larger > ul > li")
      
      for raw_word in raw_words:
        word_list.append(raw_word.select_one("b").text)
      
      print(word_list)
      
      print('%s 부터 시작! 😜' %self.player[turn].name)
      print('다음 초성에 해당하는 단어를 말해주세요! %s' %choseong)
      
      while True :
        if turn == len(self.player)-1 : #현재 차례가 사용자라면
          ans = input('%s : ' %(self.player[turn].name))
          if ans in word_list and ans not in ans_list : #맞는 답을 말했다면
            print('⭕🙆‍♂️ 통과!!! 🙆‍♂️⭕')
            ans_list.append(ans)
            turn = 0
          elif ans in ans_list : #이미 나왔던 답이라면
            print('❌🙅‍♂️그건 이미 나온 단어인데!!!❌🙅‍♂️ 바보!!!👎👎👎')
            wrong_flag = True
            break
          else : #틀린 답을 말했다면
            print('❌🙅‍♂️ 땡!!! 🙅‍♂️❌')
            wrong_flag = True
            break
        else : #현재 차례가 컴퓨터라면
          pass_or_fail = random.randint(0,3) #0,1,2,3 중 하나를 뽑는다
          if pass_or_fail == 0 : #0이면 틀리기
            print('%s : 모...모르겠는데!!! 🙄💦' %(self.player[turn].name))
            print('❌🙅‍♂️ 땡!!! 🙅‍♂️❌')
            wrong_flag = True
            break
          else : #0이 아니면 정답 말하기
            ans = random.choice(word_list)
            print('%s : %s' %(self.player[turn].name, ans))
            if ans in ans_list : #이미 나왔던 답이라면
              print('❌🙅‍♂️그건 이미 나온 단어인데!!!❌🙅‍♂️ 바보!!!👎👎👎')
              wrong_flag = True
              break
            else :
              print('⭕🙆‍♂️ 통과!!! 🙆‍♂️⭕')
              ans_list.append(ans)
              turn += 1
            
            
      if wrong_flag == True :
        print('아 누가누가 술을 마셔😲 %s이(가) 술을 마셔🤪 원~~~샷❗🧨' %self.player[turn].name)
        self.player[turn].drink_amount += 1
        self.decideTurn()
      

game = Game()
game.game()