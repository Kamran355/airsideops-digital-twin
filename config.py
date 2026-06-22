# config.py

from pathlib import Path

#
# Paths
#

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

SMALL_AIRPORT_CONFIG = DATA_DIR / "airport_config_small.json"
MEDIUM_AIRPORT_CONFIG = DATA_DIR / "airport_config_medium.json"
FLIGHT_SCHEDULE_SMALL = DATA_DIR / "flight_schedule_small.csv"
FLIGHT_SCHEDULE_MEDIUM = DATA_DIR / "flight_schedule_medium.csv"


#
# Simulation Defaults
#

RANDOM_SEED = 42
SIM_START_HOUR = 6      #simulation clock starts at 0600
SIM_DURATION_HRS = 18   #simulation runs for 18hrs (0600 through midnight)

# Monte Carlo
DEFUALT_REPS = 100
MAX_REPS = 1000

#
# Turnaround task durations (in minutes)
#   triangular    -> (min, mode, max)
#   normal        -> (mean, std_dev)
#

# TODO: durations are flat right now regardless of aircraft size - Revisit once Flight/Aircraft classes exist and can carry a size category

TASK_DURATIONS = {
    "deplaning":         {"dist": "triangular", "params": (15, 22, 35)},
    "baggage_unload":    {"dist": "triangular", "params": (20, 30, 45)},
    "fueling":           {"dist": "triangular", "params": (15, 25, 40)},
    "cleaning":          {"dist": "triangular", "params": (10, 18, 30)},
    "catering":          {"dist": "triangular", "params": (15, 25, 40)},
    "maintenance_check": {"dist": "triangular", "params": (10, 20, 45)},
    "boarding":          {"dist": "triangular", "params": (20, 30, 45)},
    "baggage_load":      {"dist": "triangular", "params": (20, 28, 40)},
    "pushback":          {"dist": "triangular", "params": (5,   8, 15)},
}

#
# Disruption probabilities and delay magnitudes
#

DISRUPTION_PROBS = {
    "late_arrival":      0.20,
    "fueling_delay":     0.08,
    "maintenance_issue": 0.05,
    "crew_shortage":     0.06,
    "weather_delay":     0.04,
    "gate_conflict":     0.03,
}

# How much delay each disruption adds when it fires  (min, mode, max) in minutes
DISRUPTION_DELAYS = {
    "late_arrival":      (5,  20,  60),
    "fueling_delay":     (5,  15,  30),
    "maintenance_issue": (10, 30,  90),
    "crew_shortage":     (5,  15,  45),
    "weather_delay":     (10, 25, 120),
    "gate_conflict":     (5,  10,  25),
}

#
# Optimization Penalty Weights
#

DELAY_WEIGHT_NORMAL     = 1.0
DELAY_WEIGHT_CONNECTING = 2.5   # connecting flights hurt more if delayed
DELAY_WEIGHT_HIGH_PAX   = 1.5   # TODO: define threshold for "high pax"

#
# Aircraft -> Gate Size Compatibility
# Gate Sizes: S = small, M = medium, L = large
#

AIRCRAFT_GATE_COMPAT = {
    # regional jets
    "CRJ2":  ["S", "M", "L"],
    "CRJ7":  ["S", "M", "L"],
    "CRJ9":  ["S", "M", "L"],
    "E170":  ["S", "M", "L"],
    "E75L":  ["S", "M", "L"],

    # narrowbody mainline
    "A319":  ["M", "L"],
    "A320":  ["M", "L"],
    "A321":  ["M", "L"],
    "A20N":  ["M", "L"],
    "A21N":  ["M", "L"],
    "BCS3":  ["M", "L"],   # A220-300, Breeze's plane
    "B737":  ["M", "L"],
    "B738":  ["M", "L"],
    "B739":  ["M", "L"],
    "B38M":  ["M", "L"],
    "B39M":  ["M", "L"],

    # biggest thing the narrowbody gates handle, can also slot into a heavy
    # gate if that's all that's open
    "B752":  ["L", "H"],

    # widebodies - NPB only, dedicated heavy gates (Terminal D)
    "B77W":  ["H"],
    "B789":  ["H"],
    "A333":  ["H"],
}
# TODO: increase number of supported aircraft
# TODO: define aircraft using ICAO code

