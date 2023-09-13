import pygame
import math
from physics_engine import Planet
from draw_utils import draw_planet, draw_orbit, draw_selection_box, COLORS
from scaling_system import scaled_data
from time_simulation import simulate
from camera import Camera
from menu import Menu, PlanetDataMenu

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 800

selected_planet = None

# Creating our solar system planets
planets = [Planet(name) for name, attributes in scaled_data.items() if "distance" in attributes]

# Instantiate the Camera
camera = Camera(WIDTH, HEIGHT, scaled_data, planets)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

menu = Menu(WIDTH, HEIGHT, WIDTH)
print(f"Initial time scale from menu: {menu.get_time_scale()}")
time_scale = menu.get_time_scale()
planet_data_menu = PlanetDataMenu(WIDTH, HEIGHT)
print("Drawing menu for:", selected_planet.name if selected_planet else "None")
clock = pygame.time.Clock()


def planet_under_mouse(mouse_pos):
    for planet in planets:
        x, y = camera.get_camera_centered_position(planet)
        if (x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2 <= camera.get_scaled_radius(planet) ** 2:
            return planet
    return None

def get_selected_planet(mouse_pos, planets):
    global selected_planet
    for planet in planets:
        distance = math.sqrt((planet.x - mouse_pos[0]) ** 2 + (planet.y - mouse_pos[1]) ** 2)
        if distance <= planet.radius:
            selected_planet = planet
            print("Selected planet:", selected_planet.name if selected_planet else "None")
            return
    selected_planet = None


running = True

while running:
    needs_redraw = False  # Initialize the flag at the start of the main loop
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            running = False

        # Dynamic zoom in and out with the mouse wheel
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up (Zoom in)
                camera.zoom(1.2)
            elif event.button == 5:  # Scroll down (Zoom out)
                camera.zoom(0.8)
            elif event.button == 1:  # Left click
                camera.select_planet(planet_under_mouse(event.pos))
                selected_planet = camera.selected_planet

        # Pass the event to the menu
        menu.handle_event(event)
        if event.type == pygame.MOUSEMOTION and menu.handle.dragging:
            needs_redraw = True

    screen.fill((0, 0, 0))  # Fill the screen with black

    time_scale = menu.get_time_scale()
    simulate(planets, time_delta, time_scale)
    print(f"Passing time scale to simulate: {time_scale}")

    # Get rendering offset from the camera
    offset_x, offset_y = camera.get_render_offset()

    for planet in planets:
        position = camera.get_scaled_position(planet)

        # Apply rendering offset
        draw_x = position[0] + offset_x
        draw_y = position[1] + offset_y

        radius = camera.get_scaled_radius(planet)

        # Draw orbits and planets with the adjusted positions
        if camera.side_view:
            # Adjust y position based on distance from the sun and apply offset
            y_offset = planet.orbital_radius * camera.scale_factor / 4
            draw_y = camera.center[1] + y_offset

            # Draw horizontal orbit line
            pygame.draw.line(screen, COLORS[planet.name], (0, draw_y), (WIDTH, draw_y))
        else:
            draw_orbit(screen, COLORS[planet.name], (camera.center[0] + offset_x, camera.center[1] + offset_y),
                       int(planet.orbital_radius * camera.scale_factor))

        draw_planet(screen, COLORS[planet.name], (draw_x, draw_y), radius)

        # Draw the selection box if a planet is selected
        if planet == camera.selected_planet:
            draw_selection_box(screen, (draw_x, draw_y), radius)

        menu.draw(screen)
        if selected_planet:
            planet_data_menu.draw(screen, selected_planet)

    pygame.display.flip()

    pygame.time.wait(50)

pygame.quit()
