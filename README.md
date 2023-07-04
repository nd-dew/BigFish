# Big Fish, what is that?
Game created in python, where you have to eat smaller fishes to grow and survive.

![Game Teaser gif](docs/game_teaser.gif)



# How do I run this project?
1. Clone (or download) this repository
2. Change directory into unpacked Bigfish folder.
3. Prerequisites
    1. Install python 3.8+
    2. Create and activate virtual environment (optional)
    ```python
    python -venv bigfish-venv
    ```
    ```
    ./bigfish-venv/activate_script_depending_on_platform
    ```
    3. Install required modules
    ```python
    pip install -r requirements.txt
    ```
4. Run game
```python
pip -m main
```

[![Video installation tutorial](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://youtu.be/Skv75mWkEvI)




## How to play?
- You start as a small fish, you need to avoid bigger ones.
- You can grow by eating smaller fishes.
- When you outgrow certain type of fish you can add them to your menu.

You control your character with arrows on your keyboard (<-, ->). 


# Developer note
There is inbuild debug mode helping visualize bounding boxes around difrent types of enemies. Press F12 in the main menu to enter. Press up and down keys to see relation of your size to your points. Press Enter to exit to main menu.











# Useful tutorials and materials
1. [VSC in pyCharm](https://www.youtube.com/watch?v=jFnYQbUZQlA)
2. [pyGame overview](https://realpython.com/pygame-a-primer/)
3. [Why we should use display.update() not .flip()] (https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip)
4. [Why __init__.py is not required anymore] (https://stackoverflow.com/questions/37139786/is-init-py-not-required-for-packages-in-python-3-3)
5. [Nice tuto on docstring nad documenting code](https://www.youtube.com/watch?v=JQ8RQru-Y9Y)
6. [Tuto on text display in pygame ](https://pygame.readthedocs.io/en/latest/4_text/text.html)
7. [predefined pygame colors] (https://github.com/pygame/pygame/blob/main/src_py/colordict.py)

# Used to create project structure 
1. <a href="https://python-forum.io/Thread-PyGame-Structure-and-Organizing-part-8"> Structure</a>
2. <a href="https://github.com/metulburr/ShooterGame/tree/moved_main_loop_into_data">github game </a> 
