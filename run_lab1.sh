#!/bin/bash

cd l1
catkin_make
source devel/setup.bash
cd src/lab1/
ls
chmod +x main.py
roslaunch lab1 lf.launch
