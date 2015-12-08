#!/bin/bash

# This script launches the iptv 'daemon' application.

# This enables other users to connect to the current X session
xhost +

# Launch the main script as the iptv user.
sudo -u iptv python main.py

