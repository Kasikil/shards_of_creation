Welcome to Shards of Creation!

Starting the game:
Go to the venv\Scripts\activate.bat file (on Windows) and edit the following line:
    set "VIRTUAL_ENV=C:\Users\clayt\py\shards_of_creation\venv"
to be the absolute path to your venv folder

With the changes saved, from the root directory (the folder where this file is located), enter the following command in a command prompt:
    venv\Scripts\activate

Verify that the path in your command prompt is now prefixed with:
(venv)

The game can now be ran by running the command:
    python main.py


General Controls:
Escape      - Quit
h           - Activate hit box outlines if in debug mode
p           - Pause
n           - Night mode
e           - Open Inventory
t           - Talk
Space       - Fire Spell

Movement Controls:
a           - Rotate Left
d           - Rotate Right
w           - Move Forward
s           - Move Backwards
Left Arrow  - Rotate Left
Right Arrow - Rotate Right
Up Arrow    - Move Forward
Down Arrow  - Move Backwards

Inventory Controls:
w           - Scroll Up Inventory List
s           - Scroll Down Inventory List
Up Arrow    - Scroll Up Inventory List
Down Arrow  - Scroll Down Inventory List
r           - Throw/Discard Selected Inventory Item
u           - Use Selected Inventory Item
x           - Exit Inventory Screen

Conversation Controls:
x           - Exit Conversation