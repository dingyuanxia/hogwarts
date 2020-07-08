class Game:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power



    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp-enemy_hp
        enemy_final_hp = self.power-enemy_power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("我输了")

class HouYi(Game):
    #子类中定义了__init__父类中的__init__将覆盖
    def __init__(self):
        super().__init__(1000, 200)
        self.defense = 100
    def fight1(self,enemy_power,enemy_hp):
        final_hp = self.hp+self.defense-enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("我输了")
        else:
            print("平局")








