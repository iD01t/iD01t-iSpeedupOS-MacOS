#!/bin/bash


echo ""
echo "INSTALLING DEPENDENCIES required for iSpeedup OS..."
echo ""

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
    echo "Installing homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" > /dev/null 2>&1
    echo ''

echo "Installing Pillow..."
pip3 install pillow
echo ""

fi

echo ''

echo ""
echo "Dependencies installed!!!"
echo ""


exit 1
