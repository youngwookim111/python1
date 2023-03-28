import random

class Character:
   
    #모든 캐릭터의 모체가 되는 클래스
   
    
    def __init__(self, name, hp, power , magic_power , mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.magic = magic_power
        self.mp= mp
        
        

    def attack(self, monster):
        damage = random.randint(self.power - 2, self.power + 2)
        monster.hp = max(monster.hp - damage, 0)
        print(f"{self.name}의 공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.hp == 0:
            print(f"{monster.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")

class Player(Character):
     def __init__(self, name, hp, power , magic_power , mp):   
        super().__init__(self, name, hp, power , magic_power , mp)
       
              
        
    
     def normal_attack(self, monster):
         attack = self.power
         print(f"{self.name}의 일반공격으로 {monster.name}에게 {attack}의 데미지를 입혔습니다")
         monster.hp -= attack
           
         def magic_attack(self, monster):
            if self.mp >= 10:
                attack = self.magic_power
                print(f"{self.name}의 마법공격으로 {monster.name}에게 {attack}의 데미지를 입혔습니다.")
                monster.hp -= attack
                self.mp =- 10
            else:
              print(f"{self.name}의 마나가 부족하여 마법공격을 할 수 없습니다.")
            
      
           
            
         class monster(Character):
           def __init__(self, name, hp, power, ):    
            super().__init__(self, name, hp, power,)
    

         def normal_attack(self, player):
             attack = self.attack
             print(f"{self.name}의 일반공격으로 {player.name} 에게 {attack}의 데미지를 입혔습니다")
             player.hp -= attack


#Playr 인스턴스생성 할줄 모르겠음...

#monster 인스턴스생성 할줄 모르겠음...