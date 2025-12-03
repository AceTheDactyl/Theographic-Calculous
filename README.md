# Theographic Calculus

A unified operator language for describing physical, chemical, and emergent systems across domains.

## Overview

**Theographic Calculus (TC)** is the canonical operator language for **Cosmic Emergence Theory (CET)**. It provides a compact symbolic grammar for encoding how fields, symmetries, and attractors transform through discrete operator actions.

This repository contains:
- **Alpha-Physical Language (APL)** — A testable subset of TC focused on falsifiable physical predictions
- **Core Token System** — A 288-token universe for encoding system states
- **Neural Codex** — Mapping of TC operators to neural/consciousness frameworks
- **Validation Tools** — Python implementations and test suites

## Terminology Reference

### Core Acronyms

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **TC** | Theographic Calculus | Canonical operator language for CET |
| **CET** | Cosmic Emergence Theory | Foundational theory of emergent systems |
| **APL** | Alpha-Physical Language | Testable physical prediction framework |
| **UMOL** | Universal Modulation Operator Law | Principle that no perfect modulation exists; residue always remains |
| **BFADGS** | Boundary-Fusion-Amplification-Decoherence-Grouping-Separation | Six fundamental interaction operators |
| **PRS** | Paradox Resolution Sequence | Temporal ordering of coherence transitions (P1-P5) |
| **CLT** | Coherence Lock Transform | Modulation feedback mechanism |

### The Three Fields (Spirals)

| Symbol | Name | Domain | Role |
|--------|------|--------|------|
| **Φ** (Phi) | Structure Field | Geometry | Stability, spatial arrangement, boundaries |
| **e** | Energy Field | Wave/Dynamics | Flow, oscillations, thermodynamics |
| **π** (Pi) | Emergence Field | Chemistry/Biology | Selection, information, complexity |

### Universal Operators (BFADGS)

| Symbol | Name | Function |
|--------|------|----------|
| `()` | Boundary (B) | Containment, lift, enclosure |
| `×` | Fusion (F) | Convergence, merge, joining |
| `^` | Amplification (A) | Gain, oscillation, resonance |
| `÷` or `%` | Decoherence (D) | Breaking, noise, reset |
| `+` | Grouping (G) | Aggregation, clustering, routing |
| `-` | Separation (S) | Splitting, cutting, fission |

### Operator Machines

| Symbol | Name | Direction | Role | Tier |
|--------|------|-----------|------|------|
| **U** | Up/Projection | Ascending | Forward projection, expansion | 1 |
| **D** | Down/Integration | Descending | Backward integration, collapse | 1 |
| **M** | Middle/Modulation | Equilibrium | CLT modulation, coherence lock | 2 |
| **E** | Expansion | Output | Expression, emission | 2 |
| **C** | Collapse | Input | Consolidation, compression | 2 |
| **Mod** | Spiral Inheritance | Regulatory | Cross-field modulation | 2 |

### Truth States

| State | Description | Temporal Operator |
|-------|-------------|-------------------|
| **TRUE** | Coherent, process succeeds | DAY |
| **UNTRUE** | Unresolved, dormant potential | NIGHT |
| **PARADOX** | Contradiction, terminal attractor | None |

### Temporal Transitions

| Transition | From | To | Description |
|------------|------|-----|-------------|
| **DAY** | TRUE | UNTRUE | Active coherence generates reflection |
| **NIGHT** | UNTRUE | UNTRUE | Unresolved remains stored |
| **DAWN** | UNTRUE | TRUE | Resolution emerges from dormancy |
| **DUSK** | TRUE | UNTRUE | Coherence dissolves into potential |

## APL Sentence Structure

APL sentences follow the format:
```
[Direction][Operator] | [Machine] | [Domain] → [Regime/Behavior]
```

Example: `u^|Oscillator|wave` reads as "Forward amplification in an oscillatory machine in a wave domain."

### The Seven Test Sentences

| # | Sentence | Predicted Regime | Domain |
|---|----------|------------------|--------|
| **A1** | `d()\|Conductor\|geometry` | Isotropic lattice / sphere | Geometry |
| **A3** | `u^\|Oscillator\|wave` | Closed vortex / recirculation | Wave dynamics |
| **A4** | `m×\|Encoder\|chemistry` | Helical encoding | Chemistry |
| **A5** | `u×\|Catalyst\|chemistry` | Branching networks | Chemistry |
| **A6** | `u+\|Reactor\|wave` | Focusing jet / beam | Fluid/plasma |
| **A7** | `u%\|Reactor\|wave` | Turbulent decoherence | Flow systems |
| **A8** | `m()\|Filter\|wave` & `d×\|Catalyst\|chemistry` | Adaptive filter | Wave & chemistry |

## Token System

The core token set contains **288 tokens** organized as:

| Category | Count | Description |
|----------|-------|-------------|
| Identity Tokens | 162 | Self-referential field-machine combinations |
| Meta-Operators | 54 | Tier-2 process control operators |
| Domain Selectors | 54 | Tier-3 domain-specific semantics |
| Safety Tokens | 30 | Runtime protection flags |

### Token Syntax

```
Field:Machine(Operator)TruthState@Tier
```

Examples:
- `Φ:U(U)TRUE@1` — Structure-Up projects itself, coherent, foundational
- `e:D(D)UNTRUE@2` — Energy-Down integrates itself, unresolved, intermediate
- `π:M(resolve)UNTRUE@3` — Emergence-Modulation resolves, unresolved, advanced

### Tier System

| Tier | Name | Allowed Machines | Scope |
|------|------|------------------|-------|
| 1 | Foundational | U, D | Local |
| 2 | Intermediate | U, D, M, E, C | Regional |
| 3 | Advanced | U, D, M, E, C, Mod | Global |

## Symmetry Identity Fields

The 3-6-9-12-15 ladder structure:

| Layer | Count | Elements |
|-------|-------|----------|
| **3** | Fields | Chain (1D), Sheet (2D), Network (3D) |
| **6** | Interactions | BFADGS operators |
| **9** | Archetypes | System patterns from field-operator combinations |
| **12** | Gauges | Directional transition variants (±) |
| **15** | Gradients | Attracting convergence states (C1-5, S1-5, N1-5) |

### N0 Legality Constraints

- **N0-1**: Amplification (`^`) cannot initiate; requires prior structure
- **N0-2**: Fusion (`×`) requires ≥2 inputs
- **N0-3**: Decoherence (`÷`) requires active structure
- **N0-4**: Grouping (`+`) cannot immediately collapse via `()`
- **N0-5**: Separation (`-`) must route to `()` or `+` downstream

## Repository Structure

```
Theographic-Calculous/
├── README.md                              # This file
└── SUB QUANTUM SPOODER/
    ├── README.md                          # APL Seven Sentences documentation
    ├── COMPILE_INSTRUCTIONS.md            # LaTeX compilation guide
    ├── LaTeX/                             # Source documents
    │   ├── apl-operators-manual.tex       # Operator reference
    │   ├── apl-seven-sentences-test-pack.tex
    │   └── apl-domain-token-sets.tex
    ├── TOKENS/                            # Token system
    │   ├── apl-core-tokens.json           # 288-token universe
    │   ├── token.py                       # Python implementation
    │   ├── TOKEN_INDEX.md                 # Neural region mapping
    │   └── NEURAL_PATHING_MATRIX.md       # Pathway connectivity
    ├── docs/                              # Extended documentation
    │   ├── theographic_calculus_key_full.txt
    │   ├── Core_Manual_v1_3.txt
    │   └── TC_Language_Module_v2_1_Expanded.txt
    ├── cet_vortex_test_suite.py           # Validation framework
    └── workflows/                         # GitHub Actions
        ├── compile-latex.yml
        └── jekyll-gh-pages.yml
```

## Safety Constraints

| Parameter | Value | Description |
|-----------|-------|-------------|
| Coherence Minimum | 0.60 | Required for tier advancement |
| Load Maximum | 0.80 | Prevents runaway processes |
| Recursion Maximum | 3 | Prevents infinite loops |

Tier-1 tokens are immutable. No constant mutation is permitted.

## UMOL Principle

> "No perfect modulation exists; residue always remains."

Every modulation operation (M) leaves an UNTRUE shadow:
```
M(x) → TRUE + ε(UNTRUE) where ε > 0
```

## Testing Philosophy

APL is designed to be **falsifiable**. Each of the seven sentences is a testable hypothesis:

- **Evidence FOR APL**: Clear, reproducible overrepresentation of predicted regimes under specified conditions
- **Evidence AGAINST APL**: No such bias, or controls produce regimes equally or more often

Recommended simulation frameworks:
- Navier-Stokes (fluid dynamics)
- Wave equations (electromagnetics, acoustics)
- Reaction-diffusion (chemistry)
- Phase-field models (interfaces, materials)
- Polymer growth / aggregation

## Getting Started

1. **Read the operator manual**: `SUB QUANTUM SPOODER/LaTeX/apl-operators-manual.tex`
2. **Explore the token system**: `SUB QUANTUM SPOODER/TOKENS/apl-core-tokens.json`
3. **Run the validation suite**: `python SUB QUANTUM SPOODER/cet_vortex_test_suite.py`
4. **Choose a test sentence** (A1, A3, or A5 recommended for beginners)

## Contributing

This is an open scientific framework. Contributions welcome:
- Test implementations
- Simulation results (positive or negative)
- Refined control designs
- Critical analysis

## Citation

```
Theographic Calculus v1.0
Canonical Operator Language for Cosmic Emergence Theory
```

## License

This work is provided for scientific testing and educational purposes.
