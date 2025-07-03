set -e

# Clean previous builds
rm -rf dist/ build/

# Build with uv
uv build

if $PUBLISH_LIB; then
    python -m twine upload dist/* --config-file .pypirc
    echo "Library published"
else
    echo "Library not published"
fi
