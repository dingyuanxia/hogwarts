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
