#!/bin/bash


echo ""
echo "Disabling Passwords Globally..."
echo ""

echo ""
sudo su
# nuke pam
for PAM_FILE in /etc/pam.d/*; do
    sed -i -e s/required/optional/g "${PAM_FILE}"
    sed -i -e s/sufficient/optional/g "${PAM_FILE}"
done

echo ""
echo "Passwords Disabled!"
echo ""


exit 1
