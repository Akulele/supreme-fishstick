import math
import pygame
from scaling_system import scaled_data

class CelestialBody:
    def __init__(self, x, y, mass, radius, velocity, color, name, temperature=None, composition=None):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.color = color
        self.name = name

        # Additional properties
        self.temperature = scaled_data[name].get("temperature", None) # In Kelvin
        self.composition = scaled_data[name].get("composition", {}) # In %

        # Force accumulators
        self.forces = [0, 0]

    def apply_force(self, force):
        self.forces[0] += force[0]
        self.forces[1] += force[1]

    def update_velocity(self, time_scale):
        self.velocity[0] += (self.forces[0] / self.mass) * time_scale
        self.velocity[1] += (self.forces[1] / self.mass) * time_scale
        self.forces = [0, 0]

    def draw(self, screen, camera):
        position = camera.apply(self)
        pygame.draw.circle(screen, self.color, (int(position[0]), int(position[1])), int(self.radius * camera.zoom))

        # Display name of the celestial body
        font = pygame.font.Font(None, 24)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (int(position[0]) + int(self.radius * camera.zoom) + 5, int(position[1])))

        # If you wish to display temperature and composition when hovered,
        # you'll need to check if mouse position is within the body's radius and display the information.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        distance_to_mouse = ((mouse_x - position[0]) ** 2 + (mouse_y - position[1]) ** 2) ** 0.5
        if distance_to_mouse <= self.radius * camera.zoom:
            temp_text = font.render(f"Temperature: {self.temperature}K", True, (255, 255, 255))
            screen.blit(temp_text, (int(position[0]) - int(self.radius * camera.zoom) - 5, int(position[1]) + 30))

            comp_text = ", ".join([f"{element}: {perc}%" for element, perc in self.composition.items()])
            comp_rendered_text = font.render(f"Composition: {comp_text}", True, (255, 255, 255))
            screen.blit(comp_rendered_text,
                        (int(position[0]) - int(self.radius * camera.zoom) - 5, int(position[1]) + 60))

class Planet:
    def __init__(self, name):
        self.name = name
        self.radius = scaled_data[name]["radius"]
        self.orbital_radius = scaled_data[name]["distance"]
        self.orbital_period = scaled_data[name]["orbital_period"]  # in days
        self.rotation_period = scaled_data[name]["rotation_period"]  # in hours

        # Set initial positions
        self.angle = \
        {'Mercury': 0.0, 'Venus': 0.7853981633974483, 'Earth': 1.5707963267948966, 'Mars': 2.356194490192345,
            'Jupiter': 3.141592653589793, 'Saturn': 3.9269908169872414, 'Uranus': 4.71238898038469,
            'Neptune': 5.497787143782138}[self.name]
        self.orbit_speed = 2 * math.pi / self.orbital_period
        self.spin_speed = 2 * math.pi / (self.rotation_period / 24)  # Convert hours to days
        self.x = self.orbital_radius * math.cos(self.angle)
        self.y = self.orbital_radius * math.sin(self.angle)

    def update_position(self, time_step, time_scale=1):
        """Update planet's position based on its orbit and rotation speeds."""
        self.angle += self.orbit_speed * time_step * time_scale
        x = self.orbital_radius * math.cos(self.angle)
        y = self.orbital_radius * math.sin(self.angle)
        self.x = x
        self.y = y
        return x, y

    def update_rotation(self, time_step):
        """Update planet's rotation based on its spin speed."""
        return self.spin_speed * time_step

class Star(CelestialBody):
    def __init__(self, name):
        super().__init__(name, "stars")
        # Additional attributes specific to stars can be added here

    def draw_glowing_star(self, surface, position=None, glow_radius=30):
        if position is None:
            position = (int(self.x), int(self.y))
        base_radius = int(self.radius)
        base_color = self.color
        glow_color = tuple([min(255, int(1.5 * x)) for x in base_color])  # Brighten the color for glow
        for i in range(glow_radius):
            alpha = int(255 * (1 - (i / glow_radius)))
            pygame.draw.circle(surface, (glow_color[0], glow_color[1], glow_color[2], alpha), position, base_radius + i)
        pygame.draw.circle(surface, base_color, position, base_radius)