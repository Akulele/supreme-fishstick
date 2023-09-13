from physics_engine import Planet

def simulate(planets, time_step, time_scale):
    print(f"Simulating with time scale: {time_scale}")
    # Adjust planet positions based on the passed timescale
    for planet in planets:
        planet.update_position(time_step, time_scale)
        planet.update_rotation(time_step * time_scale)
