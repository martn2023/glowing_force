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

        self.imported_playable_chars = imported_playable_chars ## this is a list, right?
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

        print("\n")

    def next_round(self):
        print("\n")
        self.round_number += 1
        print(f"DUNGEON MASTER: --- Round {self.round_number} begins")

        alls_chars = self.imported_playable_chars.show_playable_char_keys() + self.non_playable_chars
        alls_chars.sort(key=lambda x: x.initiative, reverse = True ) ## sorting by initiative, then reversing so highest score can go first

        for character in alls_chars:
            self.take_turn(character)
            self.status = self.check_map_status()
            if self.status != "in progress":
                return None ## breaking the FOR LOOP because not all characters need to move if game is over

    def take_turn(self, character_object):
        print("\n")
        if character_object.current_health <= 0:
            print(f"BACKEND: {character_object.display_name} is dead - skipping.")
            return None

        print(f"DUNGEON MASTER: --- Round {self.round_number} | {character_object.display_name} gets his or her turn.")
        self.move_char(character_object)
        self.attack_step(character_object)

    def move_char(self, character_object):
        self.print_map_backend()
        print(f"DUNGEON MASTER: {character_object.display_name} is at row: {character_object.row_index}  col: {character_object.col_index}, and can move up {character_object.mobility} spaces.")
        destination_row = int(input(f"DUNGEON MASTER: What row will {character_object.display_name} go to? "))
        destination_col = int(input(f"DUNGEON MASTER: What column will {character_object.display_name} go to? "))

        while True:
            try:
                if self.map_matrix[destination_row][destination_col] == self.map_terrain:
                    attempted_distance = abs(destination_row-character_object.row_index) +abs(destination_col-character_object.col_index)
                    if attempted_distance > character_object.mobility:
                        print(f"DUNGEON MASTER: {character_object.display_name} can move {character_object.mobility}, but not {attempted_distance} spaces.")
                    else:
                        print(f"BACKEND: {character_object.display_name} moved.") ## might remove this code
                        self.map_matrix[character_object.row_index][character_object.col_index] = self.map_terrain
                        self.map_matrix[destination_row][destination_col] = character_object
                        character_object.row_index = destination_row
                        character_object.col_index = destination_col
                        break
                else:
                    if destination_row == character_object.row_index and destination_col == character_object.col_index: ##making an exception if the object that's blocking the square is itself
                        break
                    else:
                        print("DUNGEON MASTER: That spot is not empty.")
            except:
                print("DUNGEON: Not sure what you meant by that. I only accept numbers shown in the map.")

            destination_row = int(input(f"DUNGEON MASTER: What row will {character_object.display_name} go to? "))
            destination_col = int(input(f"DUNGEON MASTER: What column will {character_object.display_name} go to? "))




    def attack_step(self, character_object):
        self.print_map_backend()
        while True:
            print(f"DUNGEON MASTER: {character_object.display_name} searches for enemies to attack. ***Enter char's own coords to skip***") ## might be easier if attacking terrain = skipping, but what happens in the freak accidents where the map has no empty no terrain?
            attack_row = int(input(f"DUNGEON MASTER: What row will {character_object.display_name} attack? "))
            attack_col = int(input(f"DUNGEON MASTER: What col will {character_object.display_name} attack? "))
            print("\n")

            try:  #catch invalid/unreadable entries first, THEN worry about whether this is a valid attack, a step-skip, or an invalid attack
                potential_target = self.map_matrix[attack_row][attack_col]
            except:
                print("DUNGEON: Not sure what you meant by that. I only accept numbers shown in the map.")

            if potential_target == self.map_terrain: ##first see if there's anything to attack or its empty terrain, then we worry about whether the target is friendly
                print("DUNGEON MASTER: There's no enemy to attack there.")
                continue

            if self.hostility_check(character_object, potential_target):
                attacker = character_object
                defender = self.map_matrix[attack_row][attack_col]
                if self.check_range_sufficiency(attacker, defender):
                    self.engage_combat(attacker, defender)
                    break

            else:
                print(f"BACKEND: {character_object.display_name} skips the attack step, because they tried to attack an ally.")  ## for deletion
                break


    def check_range_sufficiency(self, attacker_object,defender_object):
        attempted_distance = abs(attacker_object.row_index - defender_object.row_index) + abs(attacker_object.col_index - defender_object.col_index)
        if attempted_distance > attacker_object.physical_attack_range:
            print(f"DUNGEON MASTER: {attacker_object.display_name} can attack {attacker_object.physical_attack_range} spaces away, but not {attempted_distance}.")
            return False

        return True


    def engage_combat(self, attacker, defender): ## this is a separate function because we currently assume that the attacker gets an attack, and then defender gets an attack, but there may be a day when someone gets multiple attacks
        print("DUNGEON MASTER: MORTAL KOMBAAAAAT!!!!!!")

        self.combat_action(attacker, defender)
        if defender.current_health > 0: ## later, must address additional situation where the defender can't fight back (incapacitated for example)
            self.combat_action(defender, attacker)


    def combat_action(self, damager, damaged):
        attempted_damage = damager.attack_power
        mitigated_damage = attempted_damage - damaged.physical_armor
        damaged.current_health -= mitigated_damage

        print(f"DUNGEON MASTER: {damager.display_name} attempted to attack {damaged.display_name} for {attempted_damage} physical damage, and was mitigated by {damaged.physical_armor}.")
        print(f"DUNGEON MASTER: {damaged.display_name}'s health falls {mitigated_damage} points to {damaged.current_health}.")

        if damaged.current_health <= 0: ##again, assumes for now this is the only way to die/be out of the map
            print(f"DUNGEON MASTER: {damaged.display_name} died, and is now being removed from the map board.")
            self.remove_char_from_map(damaged)

    def remove_char_from_map(self, char_object):
        self.map_matrix[char_object.row_index][char_object.col_index] = self.map_terrain

    def hostility_check(self, attacker_object, defender_object):
        return attacker_object.playable != defender_object.playable

    def check_map_status(self):
        print("BACKEND: checking map condition")
        one_playable_alive = False
        for playable in self.imported_playable_chars.show_playable_char_keys():
            if playable.current_health > 0:
                one_playable_alive = True
                break

        if one_playable_alive == False:
            return "failed"

        for npc in self.non_playable_chars: ##only need to find one living enemy
            if npc.current_health > 0:
                return "in progress"

        return "complete"

