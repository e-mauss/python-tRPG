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
    """A spell designed for use as a combat action.

    Keeps track of
    the name of a spell,
    two integers delimiting a range of damage,
    the cost of a spell.
    """
    def __init__(self, name: str, damage_low: int, damage_high: int, cost: int):
        """The constructor."""
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.cost = cost

    def get_damage_low(self):
        """Returns the lower boundary of damage range."""
        return self.damage_low

    def get_damage_high(self):
        """Returns the upper boundary of damage range."""
        return self.damage_high

    def get_cost(self):
        """Returns the cost of a spell."""
        return self.cost


class Weapon:
    """A weapon designed for use as a combat action.

    Keeps track of
    the name of a weapon,
    two integers delimiting a range of damage,
    the amount of hands needed to use the weapon.
    """
    def __init__(self, name: str, damage_low: int, damage_high: int, hands: int):
        """The constructor."""
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.hands = hands

    def get_damage_low(self):
        """Returns the lower boundary of damage range."""
        return self.damage_low

    def get_damage_high(self):
        """Returns the upper boundary of damage range."""
        return self.damage_high

    def get_hands(self):
        """Returns amount of hands needed to wield a weapon."""
        return self.hands


class Actions:
    """Keeps track of all the actions a character can use."""
    def __init__(self, *actions):
        """The constructor."""
        self.actions = []
        for action in actions:
            self.add_action(action)

    def add_action(self, action: Spell or Weapon):
        """Adds an action to the end of the array."""
        self.actions.append(action)

    def get_action(self, index: int):
        """Returns the action at the given index from the array."""
        return self.actions[index]


class Character:
    """A character which can participate in combat.

    Keeps track of
    the name of a character,
    their health points and maxhp,
    their mana points and maxmp,
    their physical and magic attack modifiers,
    their available actions,
    their available hands,
    whether the character is a player character.
    """
    def __init__(self, name: str, hp: int, attackdmg: int, magicdmg: int, mana: int, hands: int, actions: Actions,
                 is_player: bool):
        """The constructor."""
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

    def _print_spell(self, index: int, item: Spell):
        print(str(index) + ". ", item.name + ", Minimum Damage:", str(item.get_damage_low()) +
              ", Maximum Damage:", str(item.get_damage_high()) + ", Cost:", item.get_cost())

    def _print_weapon(self, index: int, item: Weapon):
        print(str(index) + ". ", item.name + ", Minimum Damage:", str(item.get_damage_low()) +
              ", Maximum Damage:", str(item.get_damage_high()) + ", Hands:", item.get_hands())

    def show_actions(self):
        """Prints all actions currently available for use.

        Prints the
        name,
        damage boundaries,
        and further specifications (hands, cost)
        of an action
        using _print_weapon and _print_spell respectively.
        """
        i = 1
        print("You have", self.hands, "hands,", self.hp, "/", self.maxhp, "hp and",
              self.mana, "/", self.maxmana, "mana.\n")
        for item in self.actions.actions:
            if type(item) is Spell:
                self._print_spell(i, item)
            elif type(item) is Weapon:
                self._print_weapon(i, item)
            i += 1

    def spell_damage(self, action: Spell):
        """Handles spellcasting.

        Checks for available mana, decreases mana by cost, and returns the damage of a given spell after printing
        information about the spells name, its damage, the caster and their leftover mana.
        """
        if action.get_cost() > self.mana:
            return -1
        self.mana -= action.get_cost()

        damage = random.randrange(action.get_damage_low(), action.get_damage_high() + 1, 1) + self.magicdmg

        print(self.name, "dealt", str(damage), "damage using", action.name +
              ". They still have", self.mana, "mana left. \n")

        return damage

    def weapon_damage(self, action: Weapon):
        """Handles weapons.

        Checks for available hands, and returns the damage of a given weapon after printing
        information about the weapons name, its damage and the wielder.
        """
        if action.get_hands() > self.hands:
            return -1

        damage = random.randrange(action.get_damage_low(), action.get_damage_high() + 1, 1) + self.attackdmg

        print(self.name, "dealt", str(damage), "damage using", action.name + ".\n")

        return damage

    def generate_damage(self) -> int:
        """Determines which action to use. Returns the damage of the action, or -1 in case of error.

        Parses player input or chooses random action for non-player characters.
        Checks for out of bounds inputs.
        Returns -1 in case of error.
        """
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
        """Lets a character receive damage. Returns leftover hp, or -1 in case of error.

        Also prints a spacer marking a new round of combat after receiving damage.
        """
        if damage == -1:
            return -1
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(self.name, "has", str(self.hp), "hp left.")
        print("\n==========\n")
        return self.hp


'''
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
    """Handles combat for two characters."""
    def __init__(self, player: Character, enemy: Character):
        """The constructor."""
        self.current = player
        self.other = enemy

    def do_combat(self):
        """Lets two character clash off until one of them dies."""
        while True:
            status = self.other.receive_damage(self.current.generate_damage())
            if status == -1:
                continue
            elif status > 0:
                self.current, self.other = self.other, self.current
            elif status == 0:
                break
