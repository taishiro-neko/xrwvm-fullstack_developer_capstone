from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
        {"name": "Nebula Dynamics",
         "description": "Mid-range interstellar haulers for captains on a budget."}, # noqa
        {"name": "Starlance Shipyards",
         "description": "High-performance strike craft with questionable safety margins."}, # noqa
        {"name": "Aurora Fleetworks",
         "description": "Luxury cruisers for admirals, oligarchs, and suspiciously rich cats."}, # noqa
        {"name": "Voidwalk Industries",
         "description": "Experimental prototypes. May or may not return from hyperspace."}, # noqa
        {"name": "Quantum Paws Labs",
         "description": "Compact ships with illegally cute AI copilots."},
    ]
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
            )
        )
    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year": 2023,
            "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023,
            "car_make": car_make_instances[4]},
        # Nebula Dynamics (freighters / haulers)
        {"name": "Nebula Runner", "type": "SUV", "year": 2025,
            "car_make": car_make_instances[5]},
        {"name": "Cargo Comet", "type": "SUV", "year": 2025,
            "car_make": car_make_instances[5]},
        {"name": "Dustcrawler", "type": "SUV", "year": 2025,
            "car_make": car_make_instances[5]},

        # Starlance Shipyards (fast attack / fighters)
        {"name": "Starlance Mk-II", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[6]},
        {"name": "Meteor Fang", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[6]},
        {"name": "Solar Javelin", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[6]},

        # Aurora Fleetworks (luxury cruisers)
        {"name": "Aurora Serenade", "type": "SUV", "year": 2025,
            "car_make": car_make_instances[7]},
        {"name": "Celestial Mirage", "type": "SUV", "year": 2025,
            "car_make": car_make_instances[7]},
        {"name": "Eclipse Royale", "type": "SUV", "year": 2025,
            "car_make": car_make_instances[7]},

        # Voidwalk Industries (weird prototypes)
        {"name": "Void Whisper", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[8]},
        {"name": "Phase Skipper", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[8]},
        {"name": "Graviton Moth", "type": "SUV", "year": 2025,
            "car_make": car_make_instances[8]},

        # Quantum Paws Labs (small & quirky)
        {"name": "Starling Cub", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[9]},
        {"name": "Quark Hopper", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[9]},
        {"name": "Photon Pouncer", "type": "Sedan", "year": 2025,
            "car_make": car_make_instances[9]},


    ]
    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'])
