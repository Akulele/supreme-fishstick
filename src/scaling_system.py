scaled_data = {
    "Sun": {
        "position": (100, 100),
        "radius": 10 * 10**5,  # In km, 1 solar radius = 100,000 km
        "mass": 1.989 * 10**30,
        "velocity": [0, 0],
        "color": (255, 223, 186),
        "temperature": 5778,  # in Kelvin
        "composition": {
            "Hydrogen": 74,
            "Helium": 24,
            "Oxygen": 1,
            "Carbon": 0.5,
            "Neon": 0.1,
            "Iron": 0.1  # in percentage
        }
    },
    "Mercury": {
        "radius": 2440,
        "distance": 57.9e6,
        "orbital_period": 88,
        "rotation_period": 1407.6 / 24,
        "position": (200, 200),
        "mass": 3.3011 * 10**23,
        "velocity": [0, 0],
        "color": (169, 169, 169),
        "temperature": 440,  # in Kelvin
        "composition": {
            "Oxygen": 42,
            "Sodium": 29,
            "Hydrogen": 22,
            "Helium": 6,
            "Potassium": 0.5
        }
    },
    "Venus": {
        "radius": 6052,
        "distance": 108.2e6,
        "orbital_period": 224.7,
        "rotation_period": 5832.5 / 24,
        "position": (300, 300),
        "mass": 4.867 * 10**24,
        "velocity": [0, 0],
        "color": (255, 165, 0),
        "temperature": 737,  # in Kelvin
        "composition": {
            "Carbon Dioxide": 96.5,
            "Nitrogen": 3.5
        }
    },
    "Earth": {
        "radius": 6371,
        "distance": 149.6e6,
        "orbital_period": 365.25,
        "rotation_period": 24 / 24,
        "position": (400, 400),
        "mass": 5.97237 * 10**24,
        "velocity": [0, 0],
        "color": (0, 128, 255),
        "temperature": 288,  # in Kelvin
        "composition": {
            "Nitrogen": 78,
            "Oxygen": 21,
            "Argon": 0.93,
            "Carbon Dioxide": 0.04
        }
    },

    "Mars": {
        "radius": 3389.5,
        "distance": 227.9e6,
        "orbital_period": 687,
        "rotation_period": 24.6 / 24,
        "position": (500, 500),
        "mass": 6.4171 * 10**23,
        "velocity": [0, 0],
        "color": (255, 0, 0),
        "temperature": 210,  # in Kelvin
        "composition": {
            "Carbon Dioxide": 95.3,
            "Nitrogen": 2.7,
            "Argon": 1.6,
            "Oxygen": 0.13,
            "Carbon Monoxide": 0.08
        }
    },

    "Jupiter": {
        "radius": 69911,
        "distance": 778.3e6,
        "orbital_period": 4331,
        "rotation_period": 9.9 / 24,
        "position": (600, 600),
        "mass": 1.8982 * 10**27,
        "velocity": [0, 0],
        "color": (255, 69, 0),
        "temperature": 165,  # in Kelvin
        "composition": {
            "Hydrogen": 90,
            "Helium": 10
        }
    },

    "Saturn": {
        "radius": 58232,
        "distance": 1.42e9,
        "orbital_period": 10747,
        "rotation_period": 10.7 / 24,
        "position": (700, 700),
        "mass": 5.6834 * 10**26,
        "velocity": [0, 0],
        "color": (255, 223, 186),
        "temperature": 134,  # in Kelvin
        "composition": {
            "Hydrogen": 96,
            "Helium": 3,
            "Methane": 0.45,
            "Ammonia": 0.0125,
            "Hydrogen Deuteride": 0.0002
        }
    },

    "Uranus": {
        "radius": 25362,
        "distance": 2.87e9,
        "orbital_period": 30589,
        "rotation_period": 17.2 / 24,
        "position": (800, 800),
        "mass": 8.6810 * 10**25,
        "velocity": [0, 0],
        "color": (173, 216, 230),
        "temperature": 76,  # in Kelvin
        "composition": {
            "Hydrogen": 82.5,
            "Helium": 15.2,
            "Methane": 2.3
        }
    },

    "Neptune": {
        "radius": 24622,
        "distance": 4.5e9,
        "orbital_period": 59800,
        "rotation_period": 16.1 / 24,
        "position": (900, 900),
        "mass": 1.02413 * 10**26,
        "velocity": [0, 0],
        "color": (0, 0, 255),
        "temperature": 72,  # in Kelvin
        "composition": {
            "Hydrogen": 80,
            "Helium": 19,
            "Methane": 1.5
        }
    }
}