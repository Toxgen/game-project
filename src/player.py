import json
import logging
import math
from functools import partial

import pygame

from src.constants import *
from src.components.support import *
from src.components.timer import Timer

class Player(pygame.sprite.Sprite):

    def load(self) -> None:
        """
        returns None
        loads player data
        sets variables, no return
        """

        with open("save/data.json") as file:
            try:
                data = json.load(file)

                self.selected_tool = weapons[data[0]]
                self.tool_index = data[1]
                self.items_inv = data[2]
                self.items_inv = data[3]
                self.location = data[4]
                self.status = data[5]

            except json.decoder.JSONDecodeError as j:
                logging.warning(f"json load error: {j}")

    def save(self) -> None:
        """
        return None
        saves
        TODO: save what map player is in
        """

        obj = (self.selected_tool.name, self.tool_index,
               [x.name for x in self.items_inv
                ], self.items_inv, self.location, self.status)

        with open("save/data.json", "w") as file:
            json.dump(obj, file, indent=4)

    # def return_next_level(self) -> int:
    #     return round((1.31 * self.player["level"] + 5))

    def __init__(self,
                 group,
                 selected_tool = Fist,
                 tool_index: int = 0,
                 tools_inv: tuple = ("nothing",),
                 items_inv: tuple = (),
                 location: dict = {
                     "x": 500,
                     "y": 500
                 }):
        
        """
        initalize all player elements
        """

        super().__init__(group)
        self.in_Attack = False
        self.in_Roll = False

        self.hit_index = 0
        self.angle = 0

        self.import_assets()

        self.status = "down"
        self.frame_index = 0

        self.selected_tool = selected_tool
        self.tool_index = tool_index
        self.tools_inv = tools_inv
        self.items_inv = items_inv
        self.location = location

        self.defense = 0  # maybe make method to find the total defense here

        self.load()

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (self.location["x"], self.location["y"]))

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        attack_action = partial(self.action, attack=True)
        roll_action = partial(self.action, roll=True)

        self.timer = {
            "tool swap": Timer(200),
            "weapon use": Timer(250, True, attack_action),
            "roll": Timer(100, True, roll_action)
        }

    def action(self, attack=False, roll=False) -> None:
        """
        return None
        starts events for the player
        """
        if attack:
            self.hit_enemy()
            self.in_Attack = True
            return

        if roll:
            self.roll()
            self.in_Roll = True
            return
    
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
            'up_idle': [],
            'down_idle': [],
            'left_idle': [],
            'right_idle': []
        }

        for animation in self.animations.keys():
            fullpath = "Assets/Resources/Character/" + animation
            self.animations[animation] = import_folder(fullpath)

    def animation(self, dt) -> None:
        """
        return None
        shows current animation frame
        """
        try:
            self.frame_index += 4 * dt
            if self.frame_index >= len(self.animations[self.status]):
                self.frame_index = 0

            self.image = self.animations[self.status][int(self.frame_index)]

        except (IndexError, Exception) as error:
            self._log = f"self.status = {self.status}, self.frame_index = {self.frame_index}"
            logging.warning(f"animation went wrong, {self._log}, error: {error}")

    def get_status(self) -> None:
        """
        return None
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

    def update(self, dt, events) -> None:
        """
        return None
        where all player events are held
        TODO: ? maybe make another function to make this
        look a lil cleaner
        """
        self.dt = dt
        self.input(events)
        self.get_status()
        if self.in_Attack:
            self.hit_enemy()
        self.update_timers()
        self.move(dt)
        self.animation(dt)

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

            if events["mouse_down"]:
                self.timer["weapon use"].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0

            if keys[pygame.K_q] and not self.timer["tool swap"].active:
                self.timer['tool swap'].activate()
                self.tool_index += 1
                self.tool_index = self.tool_index if self.tool_index > len(self.tools_inv) else 0
                self.selected_tool = self.tools_inv[self.tool_index]
            
            if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                self.timer["roll"].activate()

    def move(self, dt) -> None:
        """
        return None
        calculates the movement for player
        """
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

        self.location["x"] = self.pos.x
        self.location["y"] = self.pos.y

    def update_timers(self) -> None:
        """
        return None
        updates current ACTIVE timers 
        """
        for timer in self.timer.values():
            if timer.active:
                timer.update()

    def _get_hitboxes(self) -> None:
        """
        return None
        gets the hitboxes for the sword
        TODO: ? maybe return rect locations bc how it gonna check
        if it hit the enemy ??
        """
        self._test = pygame.display.get_surface()

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
        

    def hit_enemy(self, enemy=None) -> None:
        """
        return None
        checks if it hit the enemy
        """

        if self.hit_index:
            self.hit_index = 0
            self.in_Attack = False

        else:
            self._get_hitboxes()
            self.hit_index += 1

        if enemy is not None:

            for sword_hitbox in self.sword_hitboxes:

                if sword_hitbox.colliderect(enemy.rect):
                    self.hit_index = 0
                    enemy.hit()

    def roll(self) -> None:
        """
        return None
        WIP
        """
        logging.info("roll init")

    # def xp(self) -> int:

    #     exp = self.player["experience"]

    #     while exp >= amt_exp:
    #         amt_exp = self.return_next_level(self.player["level"])
    #         self.player["level"] += 1
    #         exp -= amt_exp

    #     self.player["experience"] = exp


if __name__ == "__main__":
    pass
