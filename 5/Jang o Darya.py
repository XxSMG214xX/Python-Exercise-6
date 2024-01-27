class Soldier:
    sold = []

    def __init__(self, sold_t, sold_id, x, y):
        self.sold_t = sold_t
        self.sold_id = sold_id
        self.health = 100
        self.x = x
        self.y = y
        Soldier.sold.append(self.sold_id)

class Melee(Soldier):
    def __init__(self, sold_id, x, y):
        super().__init__("melee", sold_id, x, y)
class Archer(Soldier):
    def __init__(self, sold_id, x, y):
        super().__init__("archer", sold_id, x, y)
class Game:
    def __init__(self,n):
        self.positions = {0:{},1:{}}
        self.players = {0: [], 1: []}
        self.current_turn = 0
        self.n=n
    def invalidswitch_turn(self):
        self.current_turn = 1 - self.current_turn 
    def create_soldier(self, sold_t, sold_id, x, y):
        player_ids = [i.sold_id for i in self.players[self.current_turn]]
        if sold_id in player_ids:
            print("duplicate tag")
            return
        if (x, y) not in self.positions[self.current_turn]:
            self.positions[self.current_turn][(x, y)] = []
        if sold_t == "archer":
            sold = Archer(sold_id, x, y)
        elif sold_t == "melee":
            sold = Melee(sold_id, x, y)
        else: 
            print("Invalid soldier type")
            return
        self.positions[self.current_turn][(x, y)].append(sold)
        self.players[self.current_turn].append(sold)
        self.invalidswitch_turn()
    def move_soldier(self, sold_id, direction):
        sold = self.find_soldier(sold_id)
        if sold is not None:
            old_position = (sold.x, sold.y)
            if direction == "up":
                new_x, new_y = sold.x, sold.y-1
            elif direction == "down":
                new_x, new_y = sold.x, sold.y+1
            elif direction == "left":
                new_x, new_y = sold.x-1, sold.y
            elif direction == "right":
                new_x, new_y = sold.x+1, sold.y 
            else:
                print("Invalid direction")
                return
            if not (0 <= new_x < self.n and 0 <= new_y < self.n):
                print("out of bounds")
                return
            self.positions[self.current_turn][old_position].remove(sold)
            if (new_x, new_y) not in self.positions[self.current_turn]:
                self.positions[self.current_turn][(new_x, new_y)] = []
            self.positions[self.current_turn][(new_x, new_y)].append(sold)
            sold.x = new_x
            sold.y = new_y
            self.invalidswitch_turn()
            return
        else:
            print(f"soldier does not exist")
            return
    def attack(self, attacker_id, target_id):
        attacker = self.find_soldier_foratack(attacker_id,"atacker")
        target = self.find_soldier_foratack(target_id,"defender")
        if attacker is None or target is None:
            return
        if isinstance(attacker, Archer):
            if self.calculate_distance(attacker.x, attacker.y, target.x, target.y) > 2:
                 print("the target is too far")
                 return
            target.health -= 10
        elif isinstance(attacker, Melee):
            if self.calculate_distance(attacker.x, attacker.y, target.x, target.y) > 1:
                 print("the target is too far")
                 return
            target.health -= 20
        if target.health <= 0:
            print("target eliminated")
            target_position = (target.x, target.y)
            if target_position in self.positions[1 - self.current_turn]:
                if target in self.positions[1 - self.current_turn][target_position]:
                    self.positions[1 - self.current_turn][target_position].remove(target)
            if target in self.players[1 - self.current_turn]:
                self.players[1 - self.current_turn].remove(target)
        self.invalidswitch_turn()
        return
    def get_info(self, sold_id):
        sold = self.find_soldier(sold_id)
        if sold is None:
            print(f"soldier does not exist")
            return
        print(f"health:  {sold.health}")
        print(f"location:  {sold.x}   {sold.y}") 
        self.invalidswitch_turn()
        return

    def who_is_in_lead(self):
        score = {0: 0, 1: 0}
        for player, soldiers in self.players.items():
            for sold in soldiers:
                score[player] += sold.health

        if score[0] > score[1]:
            print("player  1")
        elif score[0] < score[1]:
            print("player  2")
        else:
            print("draw")

    def find_soldier(self, sold_id):
        for soldiers_list in self.positions[self.current_turn].values():
            for sold in soldiers_list:
                if sold.sold_id == sold_id:
                    return sold
    def find_soldier_foratack(self, sold_id,whois):
        if whois=="atacker":
            for soldiers_list in self.positions[self.current_turn].values():
                for sold in soldiers_list:
                    if sold.sold_id == sold_id:
                        return sold
        else:
            for soldiers_list in self.positions[1-self.current_turn].values():
                for sold in soldiers_list:
                    if sold.sold_id == sold_id:
                        return sold
        print(f"soldier does not exist")
        return None
    def calculate_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
n = int(input())
game = Game(n)
commands=[]
while True:
            try:
                line = input().split(" ")
                if 'end' in line :
                    break
                commands.append(line)
            except EOFError:
                break
poin=0
while True:
    if poin==len(commands):
        break
    command = commands[poin]
    if command[0] == "new":
        game.create_soldier(command[1], int(command[2]), int(command[3]), int(command[4]))
    elif command[0] == "move":
        game.move_soldier(int(command[1]), command[2])
    elif command[0] == "attack":
        game.attack(int(command[1]), int(command[2]))
    elif command[0] == "info":
        game.get_info(int(command[1]))
    elif command[0] == "who":
        game.who_is_in_lead()
    poin+=1
