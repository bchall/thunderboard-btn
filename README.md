# thunderboard-btn

This python project reads the button press from a Silicon Labs Thunderboard REACT.

# Prerequisite

* build-essentials
* python-dev
* python-pip
* python pexpect
* bluez
* bluez-hcidump

## Setup

sudo hcitool lescan
Look for Thunder Sense #
Copy mac address

vi example.py
Change DEVICE = "00:0B:57:51:A7:61"

## Run

python example.py

## Button press

* none value 00
* SW-0 value 01
* SW-1 value 04
* Both value 05
