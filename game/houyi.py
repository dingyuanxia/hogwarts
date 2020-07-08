from python_lianxi.test_huihe import Game


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

houyi=HouYi()
houyi.fight1(1000,200)