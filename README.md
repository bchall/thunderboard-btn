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
Look for Thunder REACT #
Copy mac address

Change the mac address in example.py

## Run

python example.py

## Button press

* none value 00
* SW-0 value 01
* SW-1 value 04
* Both value 05

To read the temperature instead of button push change char-read-hnd to 0x002e
