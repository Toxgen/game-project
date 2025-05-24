import json
import logging

import pygame
from pygame import Vector2

from src.constants import *
from src.components.support import *
from src.components.timer import *

"""
future me
im working on a stopwatch and im going to put it in the timer
update function so implement that
also work on until timer there should be a comment there
also fix that tween thing at key function thing
make screen zoom in proportional to speed
"""

class Player(pygame.sprite.Sprite):

    def load(self) -> None:
        """
        returns None 
        loads player data
        sets variables
        """

        with open("save/data.json") as file:
            try:
                data = json.load(file)

                # self.selected_tool = weapons[data[0]]
                self.tool_index = data[0]
                self.items_inv = data[1]
                self.items_inv = data[2]
                self.location = data[3]
                self.status = data[4]

            except json.decoder.JSONDecodeError as j:
                logging.warning(f"json load error: {j}")

    def save(self) -> None:
        """
        return None
        saves
        TODO: save what map player is in
        """

        # add this in the first index of obj self.selected_tool.name

        obj = (self.tool_index, [x.name for x in self.items_inv], 
               self.items_inv, self.location, self.status)

        with open("save/data.json", "w") as file:
            json.dump(obj, file, indent=4)
    
    def set_rect_and_location(self):
        """
        sets rect and location (for movement)
        """
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

        self.location["x"] = self.pos.x
        self.location["y"] = self.pos.y
        
    def _get_hitboxes(self) -> None:
        """
        return None
        gets the hitboxes for the sword
        TODO: ? do this for when going diagonal
        Solution: hash table baby!!!
        """

        self.sword_hitbox = pygame.Rect((self.rect.x, self.rect.y), (10, 10))
        # polish this so the square goes inside character
        # for diagonals just find the center of the diagnol
        # very easy
        match self.status.split("_")[0]:
            case "up":
                self.sword_hitbox.x += 2
                self.sword_hitbox.y -= 9
                self.sword_hitbox.width += 19
            case 'down':
                self.sword_hitbox.x += 4
                self.sword_hitbox.y += 38
                self.sword_hitbox.width += 19
            case 'left':
                self.sword_hitbox.x -= 8
                self.sword_hitbox.y += 8
                self.sword_hitbox.height += 20
            case 'right':
                self.sword_hitbox.x += 29
                self.sword_hitbox.y += 7
                self.sword_hitbox.height += 20

        self._test.fill("red", self.sword_hitbox)

        logging.log(logging.INFO, f"{self._test} rect-xy {self.rect.x}:{self.rect.y}")

    def __init__(self, group):
        
        """
        initalize all player elements
        """

        super().__init__(group)
        self.in_Attack: bool = False
        self.in_roll: bool = False

        self.import_assets()
        
        self.load()

        self.frame_index: int = 0
        self.roll_frame: int = 0
        self.sprint_collection: dict[str, object] = {
            "sprint": 0,
            "sprint_decrease": False
        }

        self.image = self.animations[self.status][self.frame_index]
        self.rect: pygame.Rect = self.image.get_rect(center = (self.location["x"], self.location["y"]))

        self.direction = Vector2()
        self.pos = Vector2(self.rect.center)
        self.speed: int = 200
        self.base_speed: int = 200 

        self.timer = {
            "tool swap": Timer(200),
            "weapon use": Timer(250),
            "roll": Timer(500) # just pass in a boolean value
        }

        self.messsage_to_blit: dict[str, tuple] = {}

        # testing
        self._test = pygame.display.get_surface()

    def action(self, attack: bool = False, roll: bool = False) -> None:
        """
        return None
        starts events for the player

        """
        if roll:
            self.roll()
            self.in_roll = True
            return
        
        if attack:
            self._get_hitboxes()                        
            self.in_Attack = True
            return
        
        else:
            self.sword_hitbox = None
    
    def import_assets(self) -> None:
        """
        return None
        imports all current animations for player
        TODO: give credits
        """
        self.animations = {
            'up': [],
            'down': [],
            'left': [],
            'right': [],
            "up_left": [],
            "up_right": [],
            "down_left": [],
            "down_right": [],
            "up_left_idle": [],
            "up_right_idle": [],
            "down_left_idle": [],
            "down_right_idle": [],
            'up_idle': [],
            'down_idle': [],
            'left_idle': [],
            'right_idle': []
        }

        for animation in self.animations.keys():
            fullpath = "Assets/Resources/Character/" + animation
            self.animations[animation] = import_folder(fullpath)

    def animation(self) -> None:
        """
        return None
        shows current animation frame
        """
        try:
            self.frame_index += 4 *  self.dt
            if self.frame_index >= len(self.animations[self.status]):
                self.frame_index = 0

            self.image = self.animations[self.status][int(self.frame_index)]

        except (IndexError, Exception) as error:
            self._log = f"self.status = {self.status}, self.frame_index = {self.frame_index}"
            logging.warning(f"animation went wrong, {self._log}, error: {error}")

    def get_status(self) -> None:
        """
        return None \n
        shows if the player is idle or nah
        """
            
        try:
            if self.direction.magnitude() == 0:
                self.status = self.status.split("_")[0] + "_idle"

        except Exception as error:
            self._log = f"func name: {self.get_status.__name__}, args: {locals()}"
            logging.warning(
                f"getting status went wrong, {self._log}, error: {error}")
            raise Exception

    def input(self, events) -> None:
        """
        return None
        checks for user input
        timer checks for stuff
        """
        keys = pygame.key.get_pressed()

        timers_active = [timer for timer in self.timer.values() if timer.active]

        if not len(timers_active):

            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = "up"
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = "down"
            else:
                self.direction.y = 0

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status = "right"
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status = "left"
            else:
                self.direction.x = 0

            self.direction_to_status()

            if events["mouse_down"]:
                self.timer["weapon use"].activate()
                self.action(attack=True)
                self.direction = Vector2()
                self.frame_index = 0

            # if keys[pygame.K_q]:
            #     self.timer['tool swap'].activate()
            #     self.tool_index += 1
            #     self.tool_index = self.tool_index if self.tool_index > len(self.tools_inv) else 0
            #     self.selected_tool = self.tools_inv[self.tool_index]
            
            if keys[pygame.K_LCTRL]:
                self.timer["roll"].activate()
                logging.log(logging.INFO, "clicked shift")
                self.action(roll=True)

            # checks if the shift is pressed or sprint is bigger than 1e-3
            if (keys[pygame.K_LSHIFT] or self.sprint_collection["sprint"] > 1e-3) and not self.in_roll:
                # calculates speed
                self.speed = easeOutQuad(self.sprint_collection["sprint"], self.base_speed)
                
                # if sprint is not pressed and sprint is bigger 0 (naturally decreases)
                if (self.sprint_collection["sprint"] > 1e-3 and not keys[pygame.K_LSHIFT] and not self.sprint_collection["sprint_decrease"]):
                    self.sprint_collection["sprint"] -= 0.01
                    if self.sprint_collection["sprint"] > 1e-3:
                        self.speed = self.base_speed
                        self.sprint_collection["sprint_decrease"] = False
                        logging.log(logging.INFO, "sprint ended")
                    return
                # decreases sprint if not sprint-bool is true
                self.sprint_collection["sprint"] += 0.01 if not self.sprint_collection["sprint_decrease"] else -0.01

                # if sprint is max and sprint-bool is not false
                if (self.sprint_collection["sprint"] > 0.99 and not self.sprint_collection["sprint_decrease"]):
                    self.sprint_collection["sprint_decrease"] = True

                elif (self.sprint_collection["sprint"] < 1e-3): 
                    self.sprint_collection["sprint_decrease"] = False
                    self.speed = self.base_speed
                    logging.log(logging.INFO, "sprint ended")

    def direction_to_status(self) -> None:
        """
        Takes the direction and sets the status to whatever it
        is
        """
        a = self.direction.x
        b = self.direction.y
        
        if (a == -1 and b == -1):
            self.status = "up_left"

        elif (a == 1 and b == -1):
            self.status = "up_right"

        elif (a == -1 and b == 1):
            self.status = "down_left"

        elif (a == 1 and b == 1):
            self.status = "down_right"

    def status_to_direction(self, _A: str) -> None:
        """
        returns None
        Changes status to the direction of the player

        twoMore (bool): determines if the direction is more complex than n-w-s-e
        _A (str): what the player is facing

        # jst use a dict/hash tbl??
        """
        # this is such a bad idea lol
        twoMore = True if len(_A) > 5 else False

        if twoMore:
            if _A == "up_left":
                self.direction.x = -1
                self.direction.y = -1
            elif _A == "up_right":
                self.direction.x = 1
                self.direction.y = -1
            elif _A == "down_left":
                self.direction.x = -1
                self.direction.y = 1
            elif _A == "down_right":
                self.direction.x = 1
                self.direction.y = 1

        if _A == "up":
            self.direction.y = -1
        elif _A == "down":
            self.direction.y = 1

        if _A == "left":
            self.direction.x = -1
        elif _A == "right":
            self.direction.x = 1

    def move(self) -> None:
        """
        return None
        calculates the movement for player
        """

        if self.in_roll: # maybe make this into a class (like timer)
            return None

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.set_rect_and_location()
                
        self.pos.x += self.direction.x * self.speed * self.dt
        self.pos.y += self.direction.y * self.speed * self.dt

    def update_timers(self) -> None:
        """
        return None
        updates current ACTIVE timers && stopwatches
        """
        for timer in self.timer.values():
            if timer.active:
                timer.update()

    def roll(self) -> None:
        """
        return None
        """
        if not self.roll_frame:
            self.base_speed = 300
            self.speed = easeInOutExpo(self.roll_frame / 10, self.base_speed)
            
        self.status_to_direction(self.status.split("_idle")[0])
        
        self.roll_frame += 1
        logging.log(logging.INFO, f"roll_frame: {self.roll_frame}")
        
        if self.roll_frame > 10:
            self.roll_frame = 0
            self.base_speed, self.speed = 200, 200
            self.in_roll = False

    def display_information(self) -> None:
        """
        returns None
        displays information about the player
        """
        
        self.messsage_to_blit["speed"] = (str(round(self.speed, 1)), False)
        
 
    def update(self, cls_args) -> (None | dict[str, tuple]):
        """
        returns the swords hitbox
        where all player events are held

        dt: delta time
        keys: keys pressed
        first: to not make update function called twice per frame
        """
        if cls_args["first"]: return None
        if self.in_roll: self.roll()

        self.dt = cls_args["dt"]
        
        self.get_status()
        self.input(cls_args["keys"])

        self.update_timers()
        self.move()
        self.animation()
        self.display_information()

        return self.messsage_to_blit

if __name__ == "__main__":
    pass

"""
for tiled make a trees pixel image 64 by 64 -> 128x
then just automically throw it into the map class
use the offset
y-axis should be a lil more complicated but shouldne be hard
lambda x: self.whatever i dont really know
"""