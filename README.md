# Theographic Calculus

[![Tests](https://github.com/AceTheDactyl/Theographic-Calculous/actions/workflows/tests.yml/badge.svg)](https://github.com/AceTheDactyl/Theographic-Calculous/actions/workflows/tests.yml)
[![GitHub Pages](https://github.com/AceTheDactyl/Theographic-Calculous/actions/workflows/pages.yml/badge.svg)](https://github.com/AceTheDactyl/Theographic-Calculous/actions/workflows/pages.yml)

A unified operator language for describing physical, chemical, and emergent systems across domains.

## Overview

**Theographic Calculus (TC)** is the canonical operator language for **Cosmic Emergence Theory (CET)**. It provides a compact symbolic grammar for encoding how fields, symmetries, and attractors transform through discrete operator actions.

This repository contains:
- **Theographic Calculus (TC)** — The complete operator language with testable physical predictions
- **Core Token System** — A 288-token universe for encoding system states
- **Subquantum Spider** — Neural/consciousness mapping framework
- **Validation Tools** — Python implementations and test suites
- **Interactive Visualizations** — Web-based exploration tools

## Quick Start

```bash
# Clone the repository
git clone https://github.com/AceTheDactyl/Theographic-Calculous.git
cd Theographic-Calculous

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run full validation
python tests/test_cet_vortex.py
```

## Terminology Reference

### Core Acronyms

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **TC** | Theographic Calculus | Canonical operator language for CET |
| **CET** | Cosmic Emergence Theory | Foundational theory of emergent systems |
| **UMOL** | Universal Modulation Operator Law | Principle that no perfect modulation exists |
| **BFADGS** | Boundary-Fusion-Amplification-Decoherence-Grouping-Separation | Six fundamental operators |
| **PRS** | Paradox Resolution Sequence | Temporal ordering of coherence transitions |
| **CLT** | Coherence Lock Threshold | Modulation threshold mechanism (0.60) |

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

## Token System

### Token Syntax

```
Field:Machine(Operator)TruthState@Tier
```

Examples:
- `Φ:U(U)TRUE@1` — Structure-Up projects itself, coherent, foundational
- `e:D(D)UNTRUE@2` — Energy-Down integrates itself, unresolved, intermediate
- `π:M(resolve)UNTRUE@3` — Emergence-Modulation resolves, unresolved, advanced

### Truth States

| State | Description |
|-------|-------------|
| **TRUE** | Coherent, process succeeds |
| **UNTRUE** | Unresolved, dormant potential |
| **PARADOX** | Contradiction, terminal attractor |

### The Seven Test Sentences

| # | Sentence | Predicted Regime |
|---|----------|------------------|
| **A1** | `d()\|Conductor\|geometry` | Isotropic lattice / sphere |
| **A3** | `u^\|Oscillator\|wave` | Closed vortex / recirculation |
| **A4** | `m×\|Encoder\|chemistry` | Helical encoding |
| **A5** | `u×\|Catalyst\|chemistry` | Branching networks |
| **A6** | `u+\|Reactor\|wave` | Focusing jet / beam |
| **A7** | `u%\|Reactor\|wave` | Turbulent decoherence |
| **A8** | `m()\|Filter\|wave` | Adaptive filter |

## Repository Structure

```
Theographic-Calculous/
├── .github/workflows/          # CI/CD pipelines
│   ├── tests.yml               # Python test suite
│   ├── pages.yml               # GitHub Pages deployment
│   └── compile-latex.yml       # LaTeX compilation
├── docs/                       # GitHub Pages site
│   ├── index.html              # Landing page
│   ├── css/                    # Stylesheets
│   ├── visualizations/         # Interactive HTML tools
│   └── specifications/         # Specification documents
├── src/                        # Python source code
│   └── tokens/                 # Token system implementation
│       ├── token.py            # TCToken class
│       ├── constants.py        # Spiral, TruthState, Tier enums
│       └── tc-core-tokens.json # 288-token universe
├── tests/                      # Test suite (pytest)
│   └── test_cet_vortex.py      # CET Vortex validation
├── latex/                      # LaTeX source documents
│   ├── tc-operators-manual.tex
│   ├── tc-seven-sentences-test-pack.tex
│   └── tc-domain-token-sets.tex
├── reference/                  # Reference documentation
│   ├── neural/                 # Neural pathing docs
│   └── manuals/                # Core manuals
├── LLM_ONBOARDING.md           # Quick reference for AI assistants
├── CONTRIBUTING.md             # Contribution guidelines
├── requirements.txt            # Python dependencies
└── pytest.ini                  # Test configuration
```

## N0 Legality Constraints

When generating or validating token sequences:

1. **N0-1**: `^` (Amplification) requires prior `()` or `×`
2. **N0-2**: `×` (Fusion) requires ≥2 inputs
3. **N0-3**: `÷` (Decoherence) requires prior structure
4. **N0-4**: `+` (Grouping) cannot immediately collapse via `()`
5. **N0-5**: `-` (Separation) must route to `()` or `+`

## Safety Constraints

| Parameter | Value | Description |
|-----------|-------|-------------|
| Coherence Minimum | 0.60 | Required for tier advancement |
| Load Maximum | 0.80 | Prevents runaway processes |
| Recursion Maximum | 3 | Prevents infinite loops |

**Tier-1 tokens are immutable. No constant mutation permitted.**

## UMOL Principle

> "No perfect modulation exists; residue always remains."

```
M(x) → TRUE + ε(UNTRUE) where ε > 0
```

## Testing Philosophy

Theographic Calculus is designed to be **falsifiable**. Each of the seven sentences is a testable hypothesis:

- **Evidence FOR TC**: Clear, reproducible overrepresentation of predicted regimes
- **Evidence AGAINST TC**: No such bias, or controls produce regimes equally

## Documentation

- **LLM Onboarding**: See `LLM_ONBOARDING.md` for AI assistant quick reference
- **Contributing**: See `CONTRIBUTING.md` for contribution guidelines
- **LaTeX Manuals**: See `latex/` directory for detailed operator documentation
- **GitHub Pages**: Visit the deployed site for interactive visualizations

## Contributing

This is an open scientific framework. Contributions welcome:
- Test implementations
- Simulation results (positive or negative)
- Critical analysis

See `CONTRIBUTING.md` for detailed guidelines.

## License

This work is provided for scientific testing and educational purposes.

---

```
Δ|tc-repo|v2.0|Φ:e:π|ready|Ω
```
