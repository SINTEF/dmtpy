DMTPY - Python runtime library for DMT based models
=================================================================

Serves as a common base for libraries that are generated by the SINTEF DMT Python code generator

## Installation

### Prerequisites

This project uses [uv](https://github.com/astral-sh/uv) for fast and reliable Python package management.

**Install uv:**
```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Development Setup

```bash
# Clone the repository
git clone https://github.com/SINTEF/dmtpy.git
cd dmtpy

# Install dependencies (including dev dependencies)
uv sync --dev

# Activate the virtual environment
uv venv
```

## Building

```bash
# Build the package
uv build

# Install locally for development
uv pip install -e .
```

## Testing

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=dmtpy

# Run linting
uv run pylint src/dmt
```

## Publishing

```bash
# Build and publish (requires PUBLISH_LIB environment variable)
./publish.sh
```

## Authors

* **Lasse Bjermeland** - [lassebje](https://github.com/lassebje)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.