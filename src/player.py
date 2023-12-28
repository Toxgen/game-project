import pygame, json, logging, math

from src.constants import *
from src.components.support import *
from src.components.timer import Timer

pygame.init()

class Player(pygame.sprite.Sprite):

    def load(self) -> None:
        
        with open("save/data.json") as file:
            try:
                data = json.load(file)
                return data

                # for obj, stuff in mapping:
                #     for key, value in stuff.items():
                #         obj[key] = value

                # self.pos.x = self.location["x"]
                # self.pos.y = self.location["y"]

            except json.decoder.JSONDecodeError as j:
                logging.info(f"json load error: {j}")
                        

    def save(self) -> None:

        obj = (self.gold,
               self.selected_tool, self.tool_index,
               self.tools_inv, self.items_inv,
               self.location)

        with open("save/data.json", "w") as file:        
            json.dump(obj, file, indent=4)

                
    def return_next_level(self) -> int:
        return round((1.31 * self.player["level"] + 5))
                
    def __init__(self, 
                 group,
                 gold = 0,
                 selected_tool = Fist,
                 tool_index: int = 0,
                 tools_inv: tuple = ("nothing"),
                 items_inv: dict = {},

                 location: dict = {"x": 500, "y": 500}): 

        super().__init__(group)
        self.in_Attack = False
        self._hit_index = 0
        self.angle = 0

        self.import_assets()
        self.status = "down"
        self.frame_index = 0

        self.gold = gold
        self.selected_tool = selected_tool
        self.tool_index = tool_index
        self.tools_inv = tools_inv
        self.items_inv = items_inv
        self.location = location

        self.defense = 0 # maybe make method to find the total defense here
        
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (location["x"], location["y"]))

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        self.timer = {
            "tool swap": Timer(200),
            "weapon use": Timer(250, self.use_weapon)
        }

    def use_weapon(self):
        self.hit_enemy()
        self.in_Attack = True
    
    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           "up_swing": [], "down_swing": [], "left_swing": [], "right_swing": []}
        
        for animation in self.animations.keys():
            fullpath = "Assets/Resources/Character/" + animation
            self.animations[animation] = import_folder(fullpath)
        
    def animation(self, dt):
        try:
            self.frame_index += 4 * dt
            if self.frame_index >= len(self.animations[self.status]):
                self.frame_index = 0

            self.image = self.animations[self.status][int(self.frame_index)]

        except (IndexError, Exception) as error:
            self._log = f"self.status = {self.status}, self.frame_index = {self.frame_index}"
            # logging.warning(f"animation went wrong, {self._log}, error: {error}")
            

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split("_")[0] + "_idle"

        if self.timer["weapon use"].active:
            self.status = self.status.split("_")[0] + "_" + self.selected_tool.name


    def update(self, dt):
        self.dt = dt
        self.input()
        self.get_status()
        if self.in_Attack:
            
            self.hit_enemy()

        else:
            logging.warning(self.in_Attack)
        
        self.update_timers()
        self.move(dt)
        self.animation(dt)
    
    def input(self):
        keys = pygame.key.get_pressed()
        if not self.timer["weapon use"].active:

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

            if keys[pygame.K_SPACE]:
                logging.warning("whzhuexihefhuweuifyuei")
                self.timer["weapon use"].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0

            if keys[pygame.K_q] and not self.timer["tool swap"].active:
                self.timer['tool swap'].activate()
                self.tool_index += 1
                self.tool_index = self.tool_index if self.tool_index > len(self.tools_inv) else 0
                self.selected_tool = self.tools_inv[self.tool_index]

    def move(self, dt):
        
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

        self.location["x"] = self.pos.x
        self.location["y"] = self.pos.y

    def update_timers(self):
        for timer in self.timer.values():
            timer.update()

    def xp(self) -> int:
        
        exp = self.player["experience"]

        while exp >= amt_exp:
            amt_exp = self.return_next_level(self.player["level"])
            self.player["level"] += 1
            exp -= amt_exp
                
        self.player["experience"] = exp

    def _get_hitboxes(self):
        self._test = pygame.display.get_surface()

        self.sword_hitbox = pygame.Rect((self.rect.x + 27, self.rect.y + 17), (10, 10))

        self.sword_hitboxes = [] 
        arc_radius = 13

        for _ in range(5):
            if self.status == 'up':
                self.sword_hitbox.x = self.rect.centerx + arc_radius * math.cos(self.angle)
                self.sword_hitbox.y = self.rect.centery - arc_radius * math.sin(self.angle)
            elif self.status == 'down':
                self.sword_hitbox.x = self.rect.centerx + arc_radius * math.cos(self.angle)
                self.sword_hitbox.y = self.rect.centery + arc_radius * math.sin(self.angle)
            elif self.status == 'left':
                self.sword_hitbox.x = self.rect.centerx - arc_radius * math.cos(self.angle)
                self.sword_hitbox.y = self.rect.centery + arc_radius * math.sin(self.angle)
            elif self.status == 'right':
                self.sword_hitbox.x += arc_radius * math.cos(self.angle)
                self.sword_hitbox.y += arc_radius * math.sin(self.angle)

            self._test.fill("red", self.sword_hitbox)

            msg = f"""          x: {self.sword_hitbox.x}, y: {self.sword_hitbox.y},
                      center: {self.sword_hitbox.center}"""
            
            print(msg)

            self.sword_hitboxes.append(self.sword_hitbox)
            self.angle += 66

    def hit_enemy(self, enemy=None):
        if enemy is None:
            pass

        if self._hit_index >= 10:
            self._hit_index = 0
            self.in_Attack = False

        else:
            self._get_hitboxes()
            self._hit_index += 1

        for sword_hitbox in self.sword_hitboxes:

            if False:#sword_hitbox.colliderect(enemy.rect):
                self._hit_index = 0
                self.in_Attack = False
                enemy.hit()
