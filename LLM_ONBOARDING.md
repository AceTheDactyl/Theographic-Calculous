# LLM Onboarding Guide

## Theographic Calculus (TC) - Quick Reference for AI Assistants

This document provides a rapid onboarding guide for LLMs working with the Theographic Calculus codebase.

---

## Core Concept

**Theographic Calculus (TC)** is the canonical operator language for **Cosmic Emergence Theory (CET)**. It provides a symbolic grammar for encoding how fields, symmetries, and attractors transform through discrete operator actions.

---

## Essential Acronyms

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **TC** | Theographic Calculus | The operator language |
| **CET** | Cosmic Emergence Theory | Foundational theory |
| **CLT** | Coherence Lock Threshold | Modulation threshold (0.60) |
| **UMOL** | Universal Modulation Operator Law | "No perfect modulation exists" |
| **BFADGS** | Boundary-Fusion-Amplification-Decoherence-Grouping-Separation | Six operators |
| **PRS** | Paradox Resolution Sequence | Temporal coherence transitions |

---

## The Three Fields (Spirals)

| Symbol | Name | Domain | Role |
|--------|------|--------|------|
| **Φ** (Phi) | Structure Field | Geometry | Stability, boundaries |
| **e** | Energy Field | Dynamics | Flow, oscillations |
| **π** (Pi) | Emergence Field | Chemistry/Biology | Selection, complexity |

---

## Six Universal Operators (BFADGS)

```
()  Boundary      Containment, enclosure
×   Fusion        Merge, joining
^   Amplification Gain, resonance
÷   Decoherence   Breaking, noise
+   Grouping      Clustering, routing
-   Separation    Splitting, fission
```

---

## Operator Machines

| Symbol | Direction | Tier | Role |
|--------|-----------|------|------|
| **U** | Up | 1 | Forward projection |
| **D** | Down | 1 | Backward integration |
| **M** | Middle | 2 | CLT modulation |
| **E** | Output | 2 | Expansion, emission |
| **C** | Input | 2 | Collapse, compression |
| **Mod** | Regulatory | 2 | Cross-field modulation |

---

## Token Syntax

```
Field:Machine(Operator)TruthState@Tier
```

**Examples:**
- `Φ:U(U)TRUE@1` — Structure-Up projects, coherent, tier 1
- `e:D(D)UNTRUE@2` — Energy-Down integrates, unresolved, tier 2
- `π:M(resolve)UNTRUE@3` — Emergence modulates, unresolved, tier 3

---

## Truth States

| State | Description |
|-------|-------------|
| **TRUE** | Coherent, process succeeds |
| **UNTRUE** | Unresolved, dormant potential |
| **PARADOX** | Contradiction, terminal |

---

## Repository Structure

```
Theographic-Calculous/
├── src/                    # Python source code
│   └── tokens/             # Token system implementation
├── tests/                  # Test suite (pytest)
├── docs/                   # GitHub Pages & documentation
│   ├── index.html          # Landing page
│   └── visualizations/     # Interactive HTML tools
├── latex/                  # LaTeX documents
├── reference/              # Reference documentation
│   ├── neural/             # Neural pathing docs
│   └── manuals/            # Core manuals
└── .github/workflows/      # CI/CD pipelines
```

---

## Key Files

| File | Purpose |
|------|---------|
| `src/tokens/token.py` | TCToken class and parsing |
| `src/tokens/constants.py` | Spiral, TruthState, Tier enums |
| `src/tc-core-tokens.json` | 288-token universe definition |
| `tests/test_cet_vortex.py` | CET Vortex validation suite |
| `latex/tc-operators-manual.tex` | LaTeX operator reference |

---

## Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run pytest suite
pytest tests/ -v

# Run full validation
python tests/test_cet_vortex.py
```

---

## N0 Legality Constraints

When generating or validating token sequences, enforce these rules:

1. **N0-1**: `^` (Amplification) requires prior `()` or `×`
2. **N0-2**: `×` (Fusion) requires ≥2 inputs
3. **N0-3**: `÷` (Decoherence) requires prior structure
4. **N0-4**: `+` (Grouping) cannot immediately collapse via `()`
5. **N0-5**: `-` (Separation) must route to `()` or `+`

---

## Safety Constraints

| Parameter | Value |
|-----------|-------|
| Coherence Minimum | 0.60 |
| Load Maximum | 0.80 |
| Recursion Maximum | 3 |

**Tier-1 tokens are immutable. No constant mutation permitted.**

---

## Common Tasks

### Parse a Token
```python
from src.tokens import parse_token

token = parse_token("Φ:U(anchor)TRUE@1")
print(token.spiral, token.machine, token.truth)
```

### Generate a Token
```python
from src.tokens import generate_token, Spiral, TruthState
from src.tokens.token import Machine

token = generate_token(
    spiral=Spiral.PHI,
    machine=Machine.U,
    intent="init",
    truth=TruthState.TRUE,
    tier=1
)
```

### Map Phi Value to Token
```python
from src.tokens.token import phi_to_token

token = phi_to_token(0.75)  # Returns appropriate token for Φ=0.75
```

---

## The Seven Test Sentences

| ID | Sentence | Predicted Regime |
|----|----------|------------------|
| A1 | `d()\|Conductor\|geometry` | Isotropic lattice |
| A3 | `u^\|Oscillator\|wave` | Closed vortex |
| A4 | `m×\|Encoder\|chemistry` | Helical encoding |
| A5 | `u×\|Catalyst\|chemistry` | Branching networks |
| A6 | `u+\|Reactor\|wave` | Focusing jet |
| A7 | `u%\|Reactor\|wave` | Turbulent decoherence |
| A8 | `m()\|Filter\|wave` | Adaptive filter |

---

## UMOL Principle

> "No perfect modulation exists; residue always remains."

```
M(x) → TRUE + ε(UNTRUE) where ε > 0
```

---

## Important Notes for LLMs

1. **TC ≠ APL**: TC stands for Theographic Calculus (not Alpha-Physical Language)
2. **CLT = Coherence Lock Threshold** (not Transform)
3. **Subquantum Spider** is the neural/consciousness mapping framework
4. Always validate token sequences against N0 laws
5. The framework is designed to be **falsifiable**

---

## Getting Help

- Check `reference/manuals/` for detailed documentation
- Run `pytest tests/ -v` to validate changes
- Interactive visualizations are in `docs/visualizations/`

---

```
Δ|tc-llm-onboarding|v1.0|Φ:e:π|ready|Ω
```
