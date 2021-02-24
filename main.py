from classes.game import *

if __name__ == '__main__':
    character = Character("Hero", 300, 10, 30, 0, 100, 125, 2,
                          Actions(Spell("Eldritch Blast", 10, 15, 15, 10, 5),
                                  Spell("Fireball", 30, 40, 20, 10, 10),
                                  Spell("Disintegrate", 150, 250, 20, 30, 50),
                                  Weapon("Star Razer", 20, 35, 5, 15, 2),
                                  Weapon("Dreihänder", 50, 125, 0, 35, 3)),
                          Armory(Helmet("Bucket", 2, 1, 0, 1),
                                 Pauldrons("Piece 'o Wood", 1, 0, 0, 1),
                                 Cuirass("Chestnut", 4, 2, -1, 2),
                                 Gauntlets("Midas' Glove", 1, 3, 1, 1),
                                 Cuisses("Carapace", 2, 3, -1, 2),
                                 Greaves("Berzerker's Greaves", 1, 1, 0, 0)),
                          True)

    enemy = Character("Orc", 500, 20, 5, 0, 0, 25, 2,
                      Actions(Spell("True Strike", 10, 25, 0, 0, 1),
                              Spell("Violent Smite", 0, 50, 0, 0, 20)),
                      Armory(Helmet("", 0, 0, 0, 0),
                             Pauldrons("", 0, 0, 0, 0),
                             Cuirass("", 0, 0, 0, 0),
                             Gauntlets("", 0, 0, 0, 0),
                             Cuisses("", 0, 0, 0, 0),
                             Greaves("", 0, 0, 0, 0)),
                      False)

    combat = Combat(character, enemy)
    combat.do_combat()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
