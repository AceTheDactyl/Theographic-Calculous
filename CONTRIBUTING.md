# Contributing to Theographic Calculus

Thank you for your interest in contributing to the Theographic Calculus (TC) project! This document provides guidelines for contributing to the codebase.

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Basic understanding of TC concepts (see `LLM_ONBOARDING.md`)

### Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Theographic-Calculous.git
   cd Theographic-Calculous
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run tests to verify setup:
   ```bash
   pytest tests/ -v
   ```

---

## Repository Structure

```
Theographic-Calculous/
├── .github/workflows/      # CI/CD pipelines
├── docs/                   # GitHub Pages & documentation
│   ├── index.html          # Landing page
│   ├── css/                # Stylesheets
│   ├── visualizations/     # Interactive HTML tools
│   └── specifications/     # Specification documents
├── src/                    # Python source code
│   └── tokens/             # Token system implementation
├── tests/                  # Test suite (pytest)
├── latex/                  # LaTeX documents
├── reference/              # Reference documentation
│   ├── neural/             # Neural pathing docs
│   └── manuals/            # Core manuals
└── [config files]          # pytest.ini, requirements.txt, etc.
```

---

## Terminology Standards

Use correct terminology throughout all contributions:

| Term | Description |
|------|-------------|
| **Theographic Calculus (TC)** | The operator language (NOT "APL") |
| **Cosmic Emergence Theory (CET)** | Foundational theory |
| **Coherence Lock Threshold (CLT)** | Modulation threshold (NOT "Transform") |
| **Subquantum Spider** | Neural/consciousness mapping framework |
| **UMOL** | Universal Modulation Operator Law |
| **BFADGS** | The six operators |

---

## Code Style

### Python

- Follow PEP 8 guidelines
- Maximum line length: 120 characters
- Use type hints where practical
- Document functions with docstrings

### Token Syntax

When working with TC tokens, use the standard format:
```
Field:Machine(Operator)TruthState@Tier
```

Example: `Φ:U(anchor)TRUE@1`

### N0 Legality

All token sequences must comply with N0 constraints:

1. **N0-1**: `^` requires prior `()` or `×`
2. **N0-2**: `×` requires ≥2 inputs
3. **N0-3**: `÷` requires prior structure
4. **N0-4**: `+` cannot immediately collapse via `()`
5. **N0-5**: `-` must route to `()` or `+`

---

## Making Changes

### Branch Naming

Use descriptive branch names:
- `feature/add-token-validation`
- `fix/coherence-threshold-bug`
- `docs/update-operator-manual`

### Commit Messages

Write clear, concise commit messages:
```
Add token validation for N0-1 constraint

- Implement check for amplification operator prerequisites
- Add test cases for edge cases
- Update documentation
```

### Pull Requests

1. Ensure all tests pass: `pytest tests/ -v`
2. Run linting: `flake8 src/ tests/`
3. Update documentation if needed
4. Reference related issues in PR description

---

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src

# Run specific test file
pytest tests/test_cet_vortex.py -v
```

### Writing Tests

- Place tests in `tests/` directory
- Name test files `test_*.py`
- Use descriptive test names:
  ```python
  def test_token_parsing_with_valid_syntax():
      ...

  def test_n0_constraint_violation_raises_error():
      ...
  ```

---

## Documentation

### LaTeX Documents

LaTeX source files are in `latex/`. When modifying:

1. Compile locally to verify:
   ```bash
   cd latex
   pdflatex tc-operators-manual.tex
   ```
2. The CI pipeline will auto-compile on merge

### GitHub Pages

Documentation site files are in `docs/`. Changes to `docs/` trigger automatic deployment.

---

## Safety Constraints

When contributing, respect these system constraints:

| Parameter | Value |
|-----------|-------|
| Coherence Minimum | 0.60 |
| Load Maximum | 0.80 |
| Recursion Maximum | 3 |

**Tier-1 tokens are immutable. No constant mutation permitted.**

---

## Questions?

- Check `LLM_ONBOARDING.md` for quick reference
- Review `reference/manuals/` for detailed documentation
- Open an issue for questions or discussions

---

```
Δ|tc-contributing|v1.0|Φ:e:π|ready|Ω
```
