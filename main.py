from classes.game import *

if __name__ == '__main__':
    character = Character("Hero", 300, 10, 30, 125, 2,
                          Actions(Spell("Eldritch Blast", 10, 15, 5),
                                  Spell("Fireball", 30, 40, 20),
                                  Spell("Disintegrate", 150, 250, 50),
                                  Weapon("Star Razer", 20, 35, 2),
                                  Weapon("Dreihänder", 50, 125, 3)),
                          True)

    enemy = Character("Orc", 500, 20, 5, 25, 2,
                      Actions(Spell("True Strike", 10, 25, 1),
                              Spell("Violent Smite", 0, 50, 20)),
                      False)

    combat = Combat(character, enemy)
    combat.do_combat()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
