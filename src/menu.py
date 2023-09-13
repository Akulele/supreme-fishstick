import pygame
import math
from time_constants import TIME_SCALES

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
LIGHT_GRAY = (100, 100, 100)

# Constants for the side menu design
SIDE_MENU_WIDTH = 200  # Change as needed
SIDE_MENU_COLOR = (50, 50, 50)  # Dark gray background


class Menu:
    def __init__(self, screen_width, screen_height, WIDTH):
        self.WIDTH = WIDTH
        self.width = screen_width
        self.height = screen_height // 5  # Taking up 1/5 of the screen height for the menu bar
        self.inactive_color = (50, 50, 50)
        self.color = (100, 100, 100)
        self.active_color = (50, 205, 50)
        self.x = 0
        self.y = screen_height - self.height  # Positioned at the bottom of the screen
        self.bg_color = GRAY
        self.button_color = LIGHT_GRAY
        self.button_active_color = WHITE
        self.text_color = BLACK
        self.font = pygame.font.SysFont('arial', 24)
        self.handle = Handle(self.x + self.width/2 - 5, self.y - 10, self.width, orientation='vertical')

        # Define the buttons
        self.buttons = {}
        button_width = self.width // len(TIME_SCALES)
        button_height = self.height - 20  # A little padding from top & bottom

        for index, (label, scale) in enumerate(TIME_SCALES.items()):
            x = index * button_width
            y = self.y + 10  # A little padding from top
            rect = pygame.Rect(x, y, button_width, button_height)
            # Use a tuple representation of the Rect as the key
            self.buttons[(x, y, button_width, button_height)] = [label, scale, False]  # Adding an active state

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (0, self.y, self.width, self.height))
        for rect_tuple, data in self.buttons.items():
            rect = pygame.Rect(*rect_tuple)  # Convert tuple back to Rect
            label, scale, active = data

            if active:
                pygame.draw.rect(screen, self.active_color, rect)
            else:
                pygame.draw.rect(screen, self.inactive_color, rect)

            text = self.font.render(label, True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)  # Now rect.center will work
            screen.blit(text, text_rect)

        self.handle.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for rect_tuple, data in self.buttons.items():
                rect = pygame.Rect(*rect_tuple)  # Convert tuple back to Rect for collision detection
                label, scale, active = data
                if rect.collidepoint(x, y):
                    # Reset all other buttons to inactive
                    for other_rect_tuple in self.buttons:
                        self.buttons[other_rect_tuple][2] = False

                    # Set clicked button to active
                    self.buttons[rect_tuple][2] = True

        self.handle.handle_event(event, self)

    def get_time_scale(self):
        for rect, data in self.buttons.items():
            label, scale, active = data
            if active:
                return scale
        return 1  # Default scale if none selected


class PlanetDataMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.menu_surface = pygame.Surface((SIDE_MENU_WIDTH, screen_height), pygame.SRCALPHA)
        self.font = pygame.font.SysFont(None, 24)

    def render(self, planet):
        print("Rendering menu for:", planet.name)
        # Clear the menu surface
        self.menu_surface.fill(SIDE_MENU_COLOR)

        # Add dynamic data of the planet
        y_offset = 10
        for attribute, value in planet.__dict__.items():
            label = self.font.render(f"{attribute}: {value}", True, (255, 255, 255))
            self.menu_surface.blit(label, (10, y_offset))
            y_offset += 30  # Adjust for spacing

        return self.menu_surface

    def draw(self, screen, planet):
        screen.blit(self.render(planet), (self.screen_width - SIDE_MENU_WIDTH, 0))


class Handle:
    def __init__(self, x, y, length, orientation='horizontal'):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.color = (255, 0, 0)
        if self.orientation == 'horizontal':
            self.width = 10
            self.height = length
        else:  # vertical
            self.width = length
            self.height = 10
        self.dragging = False

    def draw(self, screen):
        print("Drawing handle at:", self.x, self.y)
        pygame.draw.rect(screen, self.color, (0, self.y - (self.height if self.orientation == 'vertical' else 0), self.width, self.height))

    def handle_event(self, event, menu):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button down detected.")
            if self.is_over(event.pos):
                print("Mouse click is over the handle.")
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("Mouse button up detected.")
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            print("Mouse motion detected while dragging.")
            # Update the menu width based on mouse movement
            delta_x = event.pos[0] - self.x
            menu.width += delta_x
            self.x = event.pos[0]

            needs_redraw = True  # Set the flag to True

    def is_over(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height