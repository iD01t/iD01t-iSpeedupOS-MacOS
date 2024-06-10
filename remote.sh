#!/bin/bash


echo ""
echo "Turning ON Remote Access..."
echo ""

echo ""
sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart \
    -activate \
    -configure \
    -access \
    -off \
    -restart \
    -agent \
    -privs \
    -all \
    -allowAccessFor -allUserss
echo ""


echo ""
echo "Remote Access is turned ON!"
echo ""


exit 1
