import characters_manager

class MapIndividual:
    def __init__(self, map_name: str, height: int, width: int, imported_playable_chars, map_number):

        self.map_number = map_number
        self.map_name = map_name
        self.height = height
        self.width = width
        self.map_terrain = "\u229E"  #in the beginning, assume all terrain patches are defaulted to an underscore 220E was a squre
        self.map_matrix = []

        for row in range(self.height): ## first, we need to create a map full of blank terrain
            self.map_matrix.append([])
            for col in range(self.width):
                self.map_matrix[-1].append(self.map_terrain) ## not entirely necessary that we specify content as a logo, since it will only check character object vs. not character object

        self.imported_playable_chars = imported_playable_chars
        self.place_playable_chars()
        self.non_playable_chars = []
        self.create_non_playable_chars()
        self.place_non_playable_chars()


        self.status = "in progress" ## assume that the 3 options are (in progress / completed / failed) THIS CODE ISNT BEING LEVERAGED JUST YET

        self.round_number = 0
        while self.status == "in progress":
            if self.round_number == 5: ## temporary code to block infinite loops
                break

            self.next_round()


    def place_playable_chars(self):
        print(f"BACKEND: Placing playable chars onto {self.map_name}")
        bottom_row = len(self.map_matrix)-1
        leftmost_col = 0

        for character_object in self.imported_playable_chars.show_playable_char_keys():  # in early versions, assume there is enough space at bottom-left of map to hold all the teammates
            character_object.row_index = bottom_row
            character_object.col_index = leftmost_col
            self.map_matrix[character_object.row_index][character_object.col_index] = character_object
            leftmost_col += 1  #avoiding overlap of PC placement

    def place_non_playable_chars(self): ## put htis code on hold bc we need to add x and y coordinates into npc inputs
            print(f"BACKEND: Placing playable chars onto {self.map_name}")
            for npc_object in self.non_playable_chars:
                self.map_matrix[npc_object.row_index][npc_object.col_index] = npc_object
                #print(f"placing npc: {npc_object.display_name}, {npc_object.map_icon}")

    def create_non_playable_chars(self):
        print("BACKEND: creating and placing npcs")
        file_path = "map_models/map" + str(self.map_number) + ".txt"  #careful with the (lack of) leading zeros, this won't work after 9th map
        map_specific_npc_file_lines = open(file_path, 'r').readlines()
        for each_line in map_specific_npc_file_lines:
            individual_npc_input = each_line.split(",")
            individual_npc_input[-1] = individual_npc_input[-1][:-1]

            display_name = individual_npc_input[0]
            char_class = individual_npc_input[1]
            map_icon = '\u2620' ##MANUALLY HARDCODED WORKAROUND Why is the split adding an extra \ backslash to the front of the unicode?
            maximum_health = int(individual_npc_input[3])
            attack_power = int(individual_npc_input[4])
            physical_armor = int(individual_npc_input[5])
            initiative = int(individual_npc_input[6])
            mobility = int(individual_npc_input[7])
            physical_attack_range = int(individual_npc_input[8])
            row_index = int(individual_npc_input[9])
            col_index = int(individual_npc_input[10])

            new_npc = characters_manager.Characters(
                display_name,
                char_class,
                map_icon,
                maximum_health,
                attack_power,
                physical_armor,
                initiative,
                mobility,
                physical_attack_range,
                row_index, col_index)

            self.non_playable_chars.append(new_npc)

    def print_map_backend(self):
        print("\n", "\t", self.map_name)
        top_border = "\t" + "MAP:" + "\t" + " " + "\t"
        for col_index in range(len(self.map_matrix[0])):
            new_string = str(col_index) + '\t'
            top_border += new_string

        print(top_border)
        for row_index in range(len(self.map_matrix)):
            traversed_row_with_tabs = ""
            for col_index in range(len(self.map_matrix[0])):
                if isinstance(self.map_matrix[row_index][col_index], characters_manager.Characters):
                    content_for_display = self.map_matrix[row_index][col_index].map_icon
                else: ## not an object of the class CHARACTER, so we assume it's background/terrain, possible design flaw
                    content_for_display = self.map_terrain
                traversed_row_with_tabs += content_for_display + "\t"

            print("\t" + "MAP:", "\t", row_index, "\t", traversed_row_with_tabs)

    def next_round(self):
        self.round_number += 1
        print(f"DUNGEON MASTER: Round {self.round_number} begins")
