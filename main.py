from classes.game import *

if __name__ == '__main__':
    game = Gamestate(5)
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
    '''
    character = Character(1, Stats(10, 10, 10, 10, 10, 10),
                          Spellbook(Spell("Eldritch Blast", "charisma", 10, 0, "necrotic", 0),
                                    Spell("Fireball", "intelligence", 30, 2, "fire", 0)),
                          Armory(Armor("Bucket", 2, 1, "helmet"),
                                 Armor("Chestnut", 4, 2, "cuirass"),
                                 Armor("Carapace", 2, 3, "cuisses"),
                                 Armor("Piece 'o Wood", 1, 0, "pauldrons"),
                                 Armor("Berzerker's Greaves", 1, 1, "greaves"),
                                 Armor("Midas' Glove", 1, 3, "gauntlets")),
                          Weapons(Weapon("Star Razer", "strength", 8, 2, "slashing", 2),
                                  Weapon("Throwaway Dagger", "dexterity", 4, 0, "piercing", 1)), True)
    '''
    hp = 5
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
