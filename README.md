# Welcome to Shards of Creation!

Required Development Software: 
> Python 3.7.3 (https://www.python.org/downloads/)
> Tiled (https://www.mapeditor.org/)

## Setup:
1. In the root directory of this repository, create a virtual environment from the command line/terminal:
> python -m venv venv
2. Activate the venv in the terminal/command line:
> venv\Scripts\activate
3. Verify that the path in your command prompt is now prefixed with:
> (venv)
4. Install current requirements in your local vevn by running the following command from the command line*:
> python -m pip install -r requirements.txt

\*Please note, if during development you install any additional python dependencies, you must update the requirements.txt. The easiest way to accomplish this will be by running the following command from a command line/terminal with an activated virtual enviornment:
python -m pip freeze > requirements.txt

## Making a release:
1. Activate the venv in the terminal/command line:
> venv\Scripts\activate
2. Verify that the path in your command prompt is now prefixed with:
> (venv)
3. Run the make_a_release.bat script from the command line
> make_a_release.bat
4. Go into the dist folder, select all the contents, and on the right-click context menu, select "Send To > Compressed (zipped) Folder"
4. Move the release *.zip to another loaction
5. Clean up the release process:
> clean_up_release.bat

## Starting the game:
1. Activate the venv in the terminal/command line:
> venv\Scripts\activate
2. Verify that the path in your command prompt is now prefixed with:
> (venv)
3. The game can now be ran by running the command:
> python main.py

# Controls

General Controls:
* Esc         - Quit
* h           - Activate hit box outlines if in debug mode
* p           - Pause
* n           - Night mode
* e           - Open Inventory
* t           - Talk
* Space       - Fire Spell

Movement Controls:
* a           - Rotate Left
* d           - Rotate Right
* w           - Move Forward
* s           - Move Backwards
* Left Arrow  - Rotate Left
* Right Arrow - Rotate Right
* Up Arrow    - Move Forward
* Down Arrow  - Move Backwards

Inventory Controls:
* w           - Scroll Up Inventory List
* s           - Scroll Down Inventory List
* Up Arrow    - Scroll Up Inventory List
* Down Arrow  - Scroll Down Inventory List
* r           - Throw/Discard Selected Inventory Item
* u           - Use Selected Inventory Item
* x           - Exit Inventory Screen

Conversation Controls:
* x           - Exit Conversation