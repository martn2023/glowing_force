import characters_manager


class GameInstance:
    def __init__(self):
        self.player_name = "Martin"
        ##self.player_name = input("DUNGEON MASTER: What is your name?: ")
        print(f"DUNGEON MASTER: Welcome, {self.player_name}.")
        self.build_team_of_chars()
        self.build_initial_maps()
        self.active_maps = []

    def build_team_of_chars(self):
        print("DUNGEON MASTER: It's time to build your team.")
        import characters_manager
        self.playable_characters = characters_manager.CharacterLibrary()

        char_1 = characters_manager.Characters("Thor", "warrior", "\u2656",15, 4, 3, 4, 3, 1)
        char_2 = characters_manager.Characters("Black Widow", "rogue", "\u2659", 11, 5, 1, 3, 5, 1)
        char_3 = characters_manager.Characters("Hawkeye", "hunter", "\u2657", 12, 5, 1, 3, 4, 2)

        self.playable_characters.playable_characters.add(char_1)
        self.playable_characters.playable_characters.add(char_2)
        self.playable_characters.playable_characters.add(char_3)

        print(f"DUNGEON MASTER: Your team now has {self.playable_characters.show_playable_char_names() }")
        print(f"BACKEND: Your team now has {self.playable_characters.show_playable_char_keys()}")
        print(f"BACKEND: the map icons will be {self.playable_characters.show_playable_char_icons()}")

    def build_initial_maps(self):
        import map_manager
        first_map = map_manager.MapIndividual("Awakened Forrest", 3,5)
        first_map.place_playable_chars(self.playable_characters.show_playable_char_keys())

        first_map.print_map_basic()
        first_map.print_map_backend()