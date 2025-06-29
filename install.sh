#!/bin/bash

set -e

echo "🚀 Installing forgefetch..."

BIN_PATH="/usr/local/bin/forgefetch"
PROJECT_DIR="$(pwd)"

echo "#!/bin/bash
python3 \"$PROJECT_DIR/main.py\" \"\$@\"" | sudo tee "$BIN_PATH" > /dev/null

sudo chmod +x "$BIN_PATH"

CFG_FILE="$HOME/.forgefetch"

if [ ! -f "$CFG_FILE" ]; then
    cat <<EOF > "$CFG_FILE"
{
    "renderer": "richdata",
    "instance": "standard",
    "accent_color": "\u001b[38;5;33m",
    "secondary_color": "\u001b[38;5;251m",
    "reset_color": "\u001b[0m",
    "logo_color": "\u001b[38;5;79m",
    "clear": true
}
EOF
    echo "✅ Created default config at $CFG_FILE"
else
    echo "ℹ️  Config already exists at $CFG_FILE"
fi

echo "✅ forgefetch installed. Run 'forgefetch' from anywhere."
