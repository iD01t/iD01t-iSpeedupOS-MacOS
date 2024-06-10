#!/bin/bash


echo ""
echo "Disabling Updates..."
echo ""

echo ""
sudo su
defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticDownload -bool false
defaults write com.apple.SoftwareUpdate AutomaticCheckEnabled -bool false
defaults write com.apple.commerce AutoUpdate -bool false
defaults write com.apple.commerce AutoUpdateRestartRequired -bool false
defaults write com.apple.SoftwareUpdate ConfigDataInstall -int 0
defaults write com.apple.SoftwareUpdate CriticalUpdateInstall -int 0
defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 0
defaults write com.apple.SoftwareUpdate AutomaticDownload -int 0
echo ""


echo ""
echo "Computer Updates are turned OFF!"
echo ""


exit 1
