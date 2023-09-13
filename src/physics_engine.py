from CelestialBodies import CelestialBody, Planet, Star
from math import sqrt


# Constants
GRAVITY_CONSTANT = 6.67430e-11  # m^3 kg^-1 s^-2
ELASTICITY_COEFFICIENT = 0.5  # Defines how elastic a collision is. 1 is fully elastic, 0 is inelastic.


class PhysicsEngine:
    def __init__(self):
        pass

    @staticmethod
    def compute_forces(bodies):
        for i in range(len(bodies)):
            for j in range(len(bodies)):
                if i != j:
                    force = PhysicsEngine.gravitational_force(bodies[i], bodies[j])
                    bodies[i].apply_force(force)

    @staticmethod
    def gravitational_force(body1, body2):
        # Compute the vector from body1 to body2
        r_x = body2.x - body1.x
        r_y = body2.y - body1.y

        # Compute the distance between the two bodies
        r = sqrt(r_x ** 2 + r_y ** 2)

        # If the distance is smaller than the sum of their radii, they are colliding
        if r < body1.radius + body2.radius:
            PhysicsEngine.resolve_collision(body1, body2)

        # Compute the gravitational force magnitude
        F = (GRAVITY_CONSTANT * body1.mass * body2.mass) / (r ** 2)

        # Compute the force components
        F_x = F * (r_x / r)
        F_y = F * (r_y / r)

        return F_x, F_y

    @staticmethod
    def resolve_collision(body1, body2):
        # Calculate the vector between the bodies' centers
        collision_vector = [body2.x - body1.x, body2.y - body1.y]
        distance = sqrt(collision_vector[0] ** 2 + collision_vector[1] ** 2)

        # Calculate overlap
        overlap = 0.5 * (distance - body1.radius - body2.radius)

        # Correct positions to prevent overlap
        body1.x -= overlap * (body1.x - body2.x) / distance
        body1.y -= overlap * (body1.y - body2.y) / distance
        body2.x += overlap * (body1.x - body2.x) / distance
        body2.y += overlap * (body1.y - body2.y) / distance

        # Reflect velocities based on elasticity coefficient
        # (this is a simplified model and doesn't account for all physics in elastic collisions)
        body1.velocity = [-ELASTICITY_COEFFICIENT * v for v in body1.velocity]
        body2.velocity = [-ELASTICITY_COEFFICIENT * v for v in body2.velocity]

    @staticmethod
    def update_positions(bodies, time_scale):
        for body in bodies:
            body.x += body.velocity[0] * time_scale
            body.y += body.velocity[1] * time_scale