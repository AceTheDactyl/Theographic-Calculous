# Theographic Calculus - Setup Instructions

This document provides step-by-step instructions for setting up the Theographic Calculus project from GitHub and running the test suite.

## Prerequisites

- **Python 3.7+** (recommended: Python 3.9 or higher)
- **pip** (Python package installer)
- **git** (version control)
- **Virtual environment tool** (optional but recommended: `venv` or `virtualenv`)

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/AceTheDactyl/Theographic-Calculous.git
cd Theographic-Calculous

# 2. Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the test suite
pytest tests/ -v

# 5. Run full CET Vortex validation
python tests/test_cet_vortex.py
```

## Detailed Setup Instructions

### 1. Clone the Repository

Extract the project from GitHub:

```bash
git clone https://github.com/AceTheDactyl/Theographic-Calculous.git
cd Theographic-Calculous
```

### 2. Set Up Python Virtual Environment (Recommended)

Using a virtual environment isolates project dependencies from your system Python installation.

**Using venv (built-in):**
```bash
# Create virtual environment
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows (cmd)
venv\Scripts\activate.bat

# Activate on Windows (PowerShell)
venv\Scripts\Activate.ps1
```

**Using virtualenv:**
```bash
# Install virtualenv if not already installed
pip install virtualenv

# Create and activate
virtualenv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

The project requires the following Python packages:
- `numpy>=1.20.0` - Core scientific computing
- `pytest>=7.0.0` - Testing framework
- `pytest-cov>=4.0.0` - Test coverage reporting

Install all dependencies:
```bash
pip install -r requirements.txt
```

Verify installation:
```bash
pip list
```

You should see numpy, pytest, and pytest-cov in the output.

### 4. Run the Test Suite

#### Standard Test Execution

Run all tests with verbose output:
```bash
pytest tests/ -v
```

Run tests with coverage report:
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

Run specific test file:
```bash
pytest tests/test_cet_vortex.py -v
```

#### Full CET Vortex Validation

The main validation suite can be run directly as a Python script:
```bash
python tests/test_cet_vortex.py
```

This will execute:
1. **CET Constants validation** - Verifies fundamental constants (e, φ, π, T, G, SC, N)
2. **Operator Values computation** - Calculates expansion, correction, and absorber operators
3. **Stability Criteria tests** - Validates 7 stability conditions
4. **Recursive Equation tests** - Tests vortex cycle behavior and stability
5. **Cross-Scale Physics alignment** - Validates against quantum, atomic, molecular, biological, fluid, and cosmic scales
6. **Unit Tests** - Formal unittest suite with detailed assertions

Results are saved to `cet_vortex_validation_results.json`.

### 5. Verify Installation

Check that everything is working:

```bash
# Test Python installation
python --version

# Test numpy
python -c "import numpy; print(f'NumPy {numpy.__version__}')"

# Test pytest
pytest --version

# Run quick test
pytest tests/ -v --tb=short
```

## Test Suite Overview

### Test Configuration

The test suite is configured in `pytest.ini`:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

### Test Structure

```
tests/
└── test_cet_vortex.py        # Main CET Vortex validation suite
```

### What Gets Tested

1. **CET Constants** (Section 1)
   - Core constants: e, φ, π
   - Stabilizer constants: T, G, SC, N
   - Derived constants: P, ST, C_stability

2. **Vortex Operators** (Section 2)
   - Identity Operator (𝟙): Root invariant
   - Expansion Operator (𝒰): e^φ/π
   - Correction Operator (𝒟): G^SC/T
   - Absorber Operator (𝒞): e^φ/(πφ)
   - Spiral Operator (𝒮): Crown-III modulator

3. **Vortex Cycle** (Section 3)
   - Composition: V = S ∘ C ∘ D ∘ U ∘ 𝟙
   - Single cycle behavior
   - Multi-cycle iteration
   - Return error computation

4. **Stability Criteria** (Section 4)
   - ✓ Criterion 1: e^φ/π > 1 (expansion)
   - ✓ Criterion 2: G^SC/T < 1 (correction)
   - ✓ Criterion 3: e^φ/(πφ) ≈ 1 (absorber)
   - ✓ Criterion 4: |e^(iπ|x|)| = 1 (spiral phase)
   - ✓ Criterion 5: T compression constant
   - ✓ Criterion 6: SC damping coefficient
   - ✓ Criterion 7: N > 0 (null energy)

5. **Recursive Equation Tests** (Section 5)
   - Single cycle near unity
   - Multi-cycle boundedness
   - Asymptotic stability
   - Phase coherence
   - Lyapunov stability

6. **Cross-Scale Physics** (Section 6)
   - Quantum: Berry phase
   - Atomic: Fine structure constant α
   - Molecular: Golden ratio packing
   - Biological: Heart rate variability
   - Fluid: Kolmogorov cascade
   - Cosmic: Spiral galaxies & expansion

## Expected Test Results

All tests should pass with output similar to:

```
======================================================================
CET VORTEX RECURSION CYCLE - UNIFIED TEST SUITE
Validating: Ignatius James Michael Webster Sandino's Framework
======================================================================

----------------------------------------------------------------------
SECTION 1: CET CONSTANTS
----------------------------------------------------------------------
  Core Constants:
    e  = 2.718281828459045
    φ  = 1.618033988749895
    π  = 3.141592653589793
  ...

----------------------------------------------------------------------
SECTION 3: STABILITY CRITERIA
----------------------------------------------------------------------
  ✓ PASS: e^φ/π > 1
  ✓ PASS: G^SC/T < 1
  ✓ PASS: e^φ/(πφ) ≈ 1
  ...

======================================================================
OVERALL VALIDATION RESULTS
======================================================================
  Stability Criteria:     ✓ PASS
  Recursive Equation:     ✓ PASS
  Cross-Scale Physics:    100.0% alignment

  FRAMEWORK VALIDATED:    ✓ YES
```

## Troubleshooting

### Import Errors

If you see `ModuleNotFoundError`:
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### NumPy Installation Issues

If NumPy fails to install:
```bash
# Update pip
pip install --upgrade pip

# Install NumPy separately
pip install numpy>=1.20.0

# Then install remaining dependencies
pip install -r requirements.txt
```

### pytest Not Found

If `pytest` command is not found:
```bash
# Install pytest explicitly
pip install pytest>=7.0.0

# Or run via Python module
python -m pytest tests/ -v
```

### Python Version Issues

Ensure you're using Python 3.7 or higher:
```bash
python --version

# If needed, specify Python version explicitly
python3.9 -m venv venv
```

## Directory Structure

After setup, your directory should look like:

```
Theographic-Calculous/
├── .github/workflows/          # CI/CD pipelines
├── docs/                       # GitHub Pages site
├── src/                        # Python source code
│   └── tokens/                 # Token system implementation
├── tests/                      # Test suite
│   └── test_cet_vortex.py     # Main validation suite
├── latex/                      # LaTeX documentation
├── reference/                  # Reference materials
├── venv/                       # Virtual environment (created during setup)
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Test configuration
├── README.md                   # Project overview
├── SETUP.md                    # This file
└── CONTRIBUTING.md             # Contribution guidelines
```

## Continuous Integration

This repository includes GitHub Actions workflows for:
- **tests.yml**: Automated testing on push/pull request
- **pages.yml**: GitHub Pages deployment
- **compile-latex.yml**: LaTeX document compilation

Tests are automatically run in CI when you push changes.

## Next Steps

After successful setup and test execution:

1. **Explore the codebase**: Read `LLM_ONBOARDING.md` for quick reference
2. **Review documentation**: Check `README.md` for project overview
3. **Examine test results**: Open `cet_vortex_validation_results.json`
4. **Interactive visualizations**: Open `docs/index.html` in a browser
5. **LaTeX documentation**: Compile PDFs from `latex/` directory

## For Claude Code Projects

When initializing this project in Claude Code:

1. **Auto-setup hook**: Configure to run `pip install -r requirements.txt` on project open
2. **Test runner**: Set up pytest as the default test command
3. **Python interpreter**: Ensure virtual environment Python is selected
4. **Watch mode**: Enable pytest watch mode for continuous testing during development

### Recommended Claude Code Settings

```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests/", "-v"],
  "python.testing.autoTestDiscoverOnSaveEnabled": true
}
```

## Additional Resources

- **Repository**: https://github.com/AceTheDactyl/Theographic-Calculous
- **Issues**: https://github.com/AceTheDactyl/Theographic-Calculous/issues
- **Documentation**: See `docs/` directory and GitHub Pages site
- **Contributing**: See `CONTRIBUTING.md` for guidelines

---

**Signature**: `Δ|tc-setup|v1.0|ready|Ω`

For questions or issues, please open a GitHub issue or consult the documentation.
