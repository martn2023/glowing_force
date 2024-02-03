class MapIndividual:
    def __init__(self, map_name: str, height: int, width: int):
        self.map_name = map_name
        self.height = height
        self.width = width
        self.map_terrain = "_"  #in the beginning, assume all terrain patches are defaulted to an underscore _
        self.map_matrix = height * [self.width*[self.map_terrain]]  #possiblye built incorrectly
        self.map_matrix = [ ["-","-","-","-"],["-","-","-","-"],["-","-","-","-"] ]
        print("newly made matrix", self.map_matrix)


    def place_playable_chars(self, list_of_playable_chars):
        print("want to place playables, objs:", list_of_playable_chars)

        bottom_row = len(self.map_matrix)-1
        leftmost_col = 0

        self.map_matrix[2][0] = "8"  #not making sense at all
        print(self.map_matrix)

        """
        for character_object in list_of_playable_chars:  # in early versions, assume there is enough space at bottom-left of map to hold all the teammates
            print("iteration", character_object, "what row am i changing?", bottom_row)
            self.map_matrix[0][0] = 8
            
            character_object.row_index = bottom_row
            character_object.col_index = leftmost_col
            print(f"coords changed for {character_object}, {character_object.row_index}, {character_object.col_index}")
            self.map_matrix[character_object.row_index][character_object.col_index] = character_object.map_icon
            
        """

    def print_map_basic(self):
        print("\n", self.map_name)
        for row in self.map_matrix:
            print("MAP:", row)

    def print_map_backend(self):
        print("\n", self.map_name)
        for row in self.map_matrix:
            print("MAP:", row)


        print(self.map_matrix)