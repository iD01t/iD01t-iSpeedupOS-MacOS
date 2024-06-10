#!/bin/bash


echo ""
echo "Reducing Reduce Motion & Transparency..."
echo ""

echo ""
sudo defaults write com.apple.Accessibility DifferentiateWithoutColor -int 1
defaults write com.apple.Accessibility ReduceMotionEnabled -int 1
defaults write com.apple.universalaccess reduceMotion -int 1
defaults write com.apple.universalaccess reduceTransparency -int 1
echo ""


echo ""
echo "Motion & Transparency are OFF!"
echo ""


exit 1
