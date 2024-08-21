**AUTHOR'S CONTEXT**:

This is my first self-directed project, meaning:
1. I came up with the product idea, and architecture decisions all by myself.
2. All code and comments were written without any assistance i.e. I wrote every line by myself without leaning on other people or ChatGPT.

This is different from the GeekTrust project where someone else laid out clearly defined input instructions and output requirements, and is also different from the book library project (hidden from GitHub now) which was my first CRUD system, but relied heavily on Mozilla's tutorial.

**PROJECT GOALS**:

	SCOPE AND SCALE:
	1. Build something small enough appropriate for a novice
	2. Build something that could extend to a larger project
	3. Build something that is simple for much of the population to understand immediately

	DEMONSTRATION OF TECHNICAL CONCEPTS:
	1. OOP, particularly on the encapsulation side
	2. SRP
	3. Extensibility, particularly with the maps
	4. Data storage, particularly with the NPCs (INCOMPLETE)
	5. The idea of a working game loop (SATISFCATORY)

	INTRODUCTION TO BEST PRACTICES:
	1. Linting (Flake8) and industry coding standards (PEP8)
	2. Storing and sharing code in GitHub
	3. Better naming


**OVERVIEW**:

"Glowing Force" is a tactical RPG (role-playing game) that is similar in style to SEGA's Shining Force, Nintendo's Fire Emblem series, and PlayStation's Final Fantasy Tactics. Stages/maps are 2-D grids where player-operated characters take turns moving around the board and fighting with NPCS.

	STAGE 1: This game will be 100% text/terminal based.
	STAGE 2: The next project will be a proof-of-concept with PyGame, where I will prove visuals
	STAGE 3: Rebuild stage 1 with PyGame so the visuals match the backend code
	STAGE 4: Rebuild stage 3 with more features

![glowingforce1](https://github.com/user-attachments/assets/4b47005e-fec6-443d-b5f4-85255fe0aa9f)

![glowingforce2](https://github.com/user-attachments/assets/320f0b86-8d54-4e0d-9dc0-12e5ba216f97)

![glowingforce3](https://github.com/user-attachments/assets/ed437522-5612-49e8-8d84-741c4b118fe0)

![glowingforce4](https://github.com/user-attachments/assets/4fff5a01-7bdc-463b-af21-4e8fbe8107f8)


**DOD** :
1. START SCREEN THAT ALLOWS PLAYER TO ENTER UNFINISHED MAPS
2. +2 maps with unique NPCs
3. +3 playable characters with different combat attributes (e.g. health points, armor, attack power)
4. Game loop that puts someone back at a Main Menu after failing a map, and ends when a player either quits OR finished all maps


**NOT IN SCOPE** :
1. SAVED GAMES
2. Custom characters
3. NPC AI
4. Character drafting
5. Ability to inspect characters mid-game
6. Graphics beyond terminal/ASCII
