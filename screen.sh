#!/bin/bash


echo ""
echo "Disabling Screen Locking..."
echo ""

echo ""
sudo defaults write com.apple.loginwindow DisableScreenLock -bool true
echo ""


echo ""
echo "Lock Screen is turned OFF!"
echo ""


exit 1
