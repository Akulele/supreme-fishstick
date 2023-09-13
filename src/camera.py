from scaling_system import scaled_data

class Camera:
    def __init__(self, width, height, scaled_data, planets):
        self.WIDTH = width
        self.HEIGHT = height
        self.center = (width // 2, height // 2)
        self.scaled_data = scaled_data  # Store scaled_data as an instance variable
        self.planets = planets  # Store the list of Planet objects as an instance variable
        self.selected_planet = None
        self.side_view = False
        self.base_scale_factor = 1e-7
        self.max_distance = max([data["distance"] for data in self.scaled_data.values() if "distance" in data])
        self.scale_factor = min(width, height) / (2 * self.max_distance)

    def get_scaled_position(self, planet):
        x, y = planet.update_position(0.1)
        return (self.center[0] + int(x * self.scale_factor), self.center[1] + int(y * self.scale_factor))

    def get_scaled_radius(self, planet):
        MIN_PLANET_SIZE = 5
        return max(int(planet.radius * self.scale_factor), MIN_PLANET_SIZE)

    def get_camera_centered_position(self, planet):
        """Return the position of the planet adjusted for camera centering."""
        x, y = self.get_scaled_position(planet)
        offset_x, offset_y = self.get_render_offset()
        return x + offset_x, y + offset_y

    def get_render_offset(self):
        """"Get the offset needed to render objects based on the selected planet and its neighbors."""
        if self.selected_planet:
            # Get the position of the selected planet
            selected_x, selected_y = self.get_scaled_position(self.selected_planet)

            # Calculate the average position of the selected planet and its immediate neighbors
            planet_names = [planet.name for planet in self.planets]  # Use self.planets to get planet names
            index = planet_names.index(self.selected_planet.name)
            positions = [(selected_x, selected_y)]

            # Previous neighbor
            if index > 0:
                prev_planet = self.planets[index - 1]
                prev_x, prev_y = self.get_scaled_position(prev_planet)
                positions.append((prev_x, prev_y))

            # Next neighbor
            if index < len(planet_names) - 1:
                next_planet = self.planets[index + 1]
                next_x, next_y = self.get_scaled_position(next_planet)
                positions.append((next_x, next_y))

            # Calculate the average position
            avg_x = sum(x for x, _ in positions) / len(positions)
            avg_y = sum(y for _, y in positions) / len(positions)

            # Calculate the offset based on the actual position of the planet
            return self.center[0] - selected_x, self.center[1] - selected_y
        return 0, 0

    def zoom_in_to(self):
        if not self.side_view:
            self.scale_factor /= 50
            self.side_view = True
        else:
            self.scale_factor = self.base_scale_factor
            self.side_view = False

    def zoom(self, factor):
        self.scale_factor *= factor

    def select_planet(self, planet):
        if self.selected_planet == planet:
            self.zoom_in_to()
        else:
            self.selected_planet = planet