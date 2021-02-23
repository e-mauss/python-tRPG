import random


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Spell:
    def __init__(self, name: str, damage_low: int, damage_high: int, cost: int):
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.cost = cost

    def get_damage_low(self):
        return self.damage_low

    def get_damage_high(self):
        return self.damage_high

    def get_cost(self):
        return self.cost


class Weapon:
    def __init__(self, name: str, damage_low: int, damage_high: int, hands: int):
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.hands = hands

    def get_damage_low(self):
        return self.damage_low

    def get_damage_high(self):
        return self.damage_high

    def get_hands(self):
        return self.hands


class Actions:
    def __init__(self, *actions):
        self.actions = []
        for action in actions:
            self.add_action(action)

    def add_action(self, action: Spell or Weapon):
        self.actions.append(action)

    def get_action(self, index: int):
        return self.actions[index]


class Character:
    def __init__(self, name: str, hp: int, attackdmg: int, magicdmg: int, mana: int, hands: int, actions: Actions,
                 is_player: bool):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.attackdmg = attackdmg
        self.magicdmg = magicdmg
        self.maxmana = mana
        self.mana = mana
        self.hands = hands
        self.actions = actions
        self.is_player = is_player

    '''
    def calc_hp(self):
        self.maxhp = (self.stats.constitution + 5) * self.level
        self.hp = self.maxhp
    
    def get_statvalue(self, stat):
        if stat == "strength":
            return self.stats.strength
        if stat == "dexterity":
            return self.stats.dexterity
        if stat == "constitution":
            return self.stats.constitution
        if stat == "intelligence":
            return self.stats.intelligence
        if stat == "wisdom":
            return self.stats.wisdom
        if stat == "charisma":
            return self.stats.charisma

    def update_actions(self):
        for spell in self.spellbook.spells:
            self.actions.append(spell)
        if self.weapons.mainhand is not None:
            self.actions.append(self.weapons.mainhand)
        if self.weapons.offhand is not None:
            self.actions.append(self.weapons.offhand)
    '''

    def print_spell(self, index: int, item: Spell):
        print(str(index) + ". ", item.name + ", Minimum Damage:", str(item.get_damage_low()) +
              ", Maximum Damage:", str(item.get_damage_high()) + ", Cost:", item.get_cost())

    def print_weapon(self, index: int, item: Weapon):
        print(str(index) + ". ", item.name + ", Minimum Damage:", str(item.get_damage_low()) +
              ", Maximum Damage:", str(item.get_damage_high()) + ", Hands:", item.get_hands())

    def show_actions(self):
        i = 1
        print("You have", self.hands, "hands,", self.hp, "/", self.maxhp, "hp and",
              self.mana, "/", self.maxmana, "mana.\n")
        for item in self.actions.actions:
            if type(item) is Spell:
                self.print_spell(i, item)
            elif type(item) is Weapon:
                self.print_weapon(i, item)
            i += 1

    def spell_damage(self, action: Spell):
        if action.get_cost() > self.mana:
            return -1
        self.mana -= action.get_cost()

        damage = random.randrange(action.get_damage_low(), action.get_damage_high() + 1, 1) + self.magicdmg

        print(self.name, "dealt", str(damage), "damage using", action.name +
              ". They still have", self.mana, "mana left. \n")

        return damage

    def weapon_damage(self, action: Weapon):
        if action.get_hands() > self.hands:
            return -1

        damage = random.randrange(action.get_damage_low(), action.get_damage_high() + 1, 1) + self.attackdmg

        print(self.name, "dealt", str(damage), "damage using", action.name + ".\n")

        return damage

    def generate_damage(self) -> int:
        if self.is_player is True:
            self.show_actions()
            choice = input("\nChoose Action: ")
            print("")
            index = int(choice) - 1
        else:
            index = random.randrange(0, len(self.actions.actions), 1)

        if index >= len(self.actions.actions):
            return -1

        action = self.actions.get_action(index)

        if type(action) is Spell:
            damage = self.spell_damage(action)
        elif type(action) is Weapon:
            damage = self.weapon_damage(action)
        else:
            damage = -1
        return damage

    def receive_damage(self, damage: int):
        if damage == -1:
            return -1
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(self.name, "has", str(self.hp), "hp left.")
        print("\n==========\n")
        return self.hp


'''
class Stats:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


class Armory:
    helmet = None
    cuirass = None
    cuisses = None
    gauntlets = None
    greaves = None
    pauldrons = None

    def __init__(self, *armory):
        for armor in armory:
            self.add_armor(armor)

    def add_armor(self, armor):
        if armor.slot == "helmet":
            self.helmet = armor
        elif armor.slot == "cuirass":
            self.cuirass = armor
        elif armor.slot == "cuisses":
            self.cuisses = armor
        elif armor.slot == "gauntlets":
            self.gauntlets = armor
        elif armor.slot == "greaves":
            self.greaves = armor
        elif armor.slot == "pauldrons":
            self.pauldrons = armor


class Weapons:
    mainhand = None
    offhand = None
    hands = 2

    def __init__(self, mainhand, offhand):
        if mainhand is not None:
            self.equip_mainhand(mainhand)
        if offhand is not None:
            self.equip_offhand(offhand)

    def equip_mainhand(self, weapon):
        if weapon.hands <= self.hands:
            self.mainhand = weapon
            self.hands -= weapon.hands
        return self.hands

    def equip_offhand(self, weapon):
        if weapon.hands <= self.hands:
            self.offhand = weapon
            self.hands -= weapon.hands
        return self.hands


class Armor:
    def __init__(self, name, physdefense, magicdefense, slot):
        self.name = name
        self.physdefense = physdefense
        self.magicdefense = magicdefense
        self.slot = slot
'''


class Gamestate:
    def __init__(self, world):
        self.time = 0
        self.location = {4, 45}
        self.world = world


class Combat:
    def __init__(self, player: Character, enemy: Character):
        self.current = player
        self.other = enemy

    def do_combat(self):
        while True:
            status = self.other.receive_damage(self.current.generate_damage())
            if status == -1:
                continue
            elif status > 0:
                self.current, self.other = self.other, self.current
            elif status == 0:
                break
