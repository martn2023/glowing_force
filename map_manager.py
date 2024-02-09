import characters_manager

class MapIndividual:
    def __init__(self, map_name: str, height: int, width: int, imported_playable_chars, map_number):
        self.map_number = map_number
        self.map_name = map_name
        self.height = height
        self.width = width
        self.map_terrain = "_"  #in the beginning, assume all terrain patches are defaulted to an underscore _
        self.map_matrix = []

        for row in range(self.height):
            self.map_matrix.append([])
            for col in range(self.width):
                self.map_matrix[-1].append(self.map_terrain)

        self.imported_playable_chars = imported_playable_chars
        self.place_playable_chars()
        self.non_playable_chars = []
        self.create_npcs()
        #self.place_non_playable_chars()

    def place_playable_chars(self):
        bottom_row = len(self.map_matrix)-1
        leftmost_col = 0

        for character_object in self.imported_playable_chars.show_playable_char_keys():  # in early versions, assume there is enough space at bottom-left of map to hold all the teammates
            character_object.row_index = bottom_row
            character_object.col_index = leftmost_col
            self.map_matrix[character_object.row_index][character_object.col_index] = character_object.map_icon

            leftmost_col += 1  #avoiding overlap of PC placement

    def place_non_playable_chars(self): ## put htis code on hold bc we need to add x and y coordinates into npc inputs
        top_row = 0
        leftmost_col = 0

        for character_object in self.non_playable_chars:  # in early versions, assume there is enough space at bottom-left of map to hold all the teammates
            character_object.row_index = bottom_row
            character_object.col_index = leftmost_col
            self.map_matrix[character_object.row_index][character_object.col_index] = character_object.map_icon

            leftmost_col += 1  #avoiding overlap of PC placement





    def create_npcs(self):
        print("BACKEND: creating and placing npcs")
        file_path = "map_models/map" + str(self.map_number) + ".txt"  #careful with the (lack of) leading zeros, this won't work after 9th map
        map_specific_npc_file_lines = open(file_path, 'r').readlines()

        for each_line in map_specific_npc_file_lines:
            individual_npc_input = each_line.split(",")
            individual_npc_input[-1] = individual_npc_input[-1][:-1]

            display_name = individual_npc_input[0]
            char_class = individual_npc_input[1]
            map_icon = individual_npc_input[2]
            maximum_health = int(individual_npc_input[3])
            attack_power = int(individual_npc_input[4])
            physical_armor = int(individual_npc_input[5])
            initiative = int(individual_npc_input[6])
            mobility = int(individual_npc_input[7])
            physical_attack_range = int(individual_npc_input[8])
            row_index = int(individual_npc_input[9])
            col_index = int(individual_npc_input[10])

            new_npc = characters_manager.Characters(display_name, char_class, map_icon, maximum_health, attack_power, physical_armor, initiative, mobility, physical_attack_range, row_index, col_index)
            self.non_playable_chars.append(new_npc)


    def print_map_backend(self):
        print("\n", self.map_name)
        top_border = "MAP: "
        for col_index in range(len(self.map_matrix[0])):
            top_border += "    "+str(col_index)

        print(top_border)
        for row_index in range(len(self.map_matrix)):
            print("MAP:", row_index, self.map_matrix[row_index])