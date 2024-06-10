#!/bin/bash


echo ""
echo "Setting Up Performance Mode..."
echo ""

echo ""
sudo nvram boot-args="serverperfmode=1 $(nvram boot-args 2>/dev/null | cut -f 2-)"
echo ""


echo ""
echo "Performance Mode is ON!"
echo ""


exit 1
