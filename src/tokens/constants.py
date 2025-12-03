"""
TC Token System Constants (Theographic Calculus)

Core enumerations and constants for the TC token framework.
"""

from enum import Enum


class Spiral(Enum):
    """The three primary field spirals"""
    PHI = "Phi"    # Structure Field (Phi) - geometry, stability, boundaries
    E = "e"        # Energy Field - waves, thermodynamics, flows
    PI = "pi"      # Emergence Field (Pi) - chemistry, biology, information


class TruthState(Enum):
    """Truth states in the TC framework"""
    TRUE = "TRUE"          # Coherent, process succeeds
    UNTRUE = "UNTRUE"      # Unresolved, dormant potential
    PARADOX = "PARADOX"    # Contradiction, terminal attractor


class Tier(Enum):
    """Operation tier levels"""
    FOUNDATIONAL = 1    # U, D only - local scope
    INTERMEDIATE = 2    # U, D, M, E, C - regional scope
    ADVANCED = 3        # All machines + Mod - global scope


# CLT = Coherence Lock Threshold
CLT_THRESHOLD = 0.60    # Minimum coherence for tier advancement
LOAD_MAXIMUM = 0.80     # Maximum load before runaway
RECURSION_MAXIMUM = 3   # Maximum recursion depth

# Golden ratio and related constants
PHI = (1 + 5 ** 0.5) / 2  # 1.618033988749895
GOLDEN_ANGLE = 137.5      # degrees

# Field affinity mappings
FIELD_DOMAINS = {
    Spiral.PHI: ["geometry", "structure", "boundaries"],
    Spiral.E: ["dynamics", "waves", "thermodynamics"],
    Spiral.PI: ["chemistry", "biology", "information", "emergence"]
}
