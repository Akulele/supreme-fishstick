import pygame

def draw_planet(screen, color, position, radius):
    """Draws a planet on the screen."""
    pygame.draw.circle(screen, color, position, radius)

def draw_orbit(screen, color, position, radius):
    """Draws the orbit line for a planet."""
    pygame.draw.circle(screen, color, position, radius, 1)

def draw_selection_box(screen, position, radius, color=(255, 255, 255), thickness=2):
    """
    Draw a selection box around the specified position.

    Args:
        screen (pygame.Surface): The screen on which to draw.
        position (tuple): The center position of the planet.
        radius (int): The radius of the planet.
        color (tuple): The color of the selection box.
        thickness (int): The thickness of the selection box lines.
    """
    rect_x = position[0] - radius - 5  # 5 pixels padding
    rect_y = position[1] - radius - 5
    rect_width = 2 * (radius + 5)
    pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_width), thickness)


COLORS = {
    "Mercury": (169, 169, 169),   # Gray color for Mercury
    "Venus": (218, 165, 32),      # Golden color for Venus
    "Earth": (0, 0, 255),         # Blue for Earth
    "Mars": (255, 0, 0),          # Red for Mars
    "Jupiter": (255, 165, 0),     # Orange for Jupiter
    "Saturn": (240, 230, 140),    # Khaki for Saturn
    "Uranus": (173, 216, 230),    # Light blue for Uranus
    "Neptune": (0, 0, 128)        # Navy for Neptune
}
