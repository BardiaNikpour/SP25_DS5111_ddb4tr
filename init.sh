# Exit on any error
set -e

# Update package lists
echo "Updating package lists..."
sudo apt update

# Install necessary packages
echo "Installing make..."
sudo apt install make -y

echo "Installing Python venv..."
sudo apt install python3.12-venv -y

echo "Installing tree..."
sudo apt install tree -y

echo "All necessary packages installed successfully!"
