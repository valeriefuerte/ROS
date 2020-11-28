# dependencies
# MRPT >1.9.9, for now from this PPA (or build from sources if preferred):
sudo add-apt-repository ppa:joseluisblancoc/mrpt
sudo apt update
sudo apt install libmrpt-dev mrpt-apps

# GTSAM >=4.0.0, from this PPA, or build it from sources:
sudo add-apt-repository ppa:joseluisblancoc/gtsam-develop
sudo apt update
sudo apt install libgtsam-dev

# Boost, yaml-cpp, etc:
sudo apt install libboost-serialization-dev libboost-system-dev \
  libboost-filesystem-dev libboost-thread-dev libboost-program-options-dev \
  libboost-date-time-dev libboost-timer-dev libboost-chrono-dev \
  libboost-regex-dev
sudo apt install libyaml-cpp-dev

# ROS1 (Optional)
# To install from the official Ubuntu repository (under /usr):
sudo apt install libroscpp-dev libsensor-msgs-dev
# Alternatively, install a particular ROS distribution (under /opt) and
# source the corresponding setup.bash file before invoking cmake:





# Mola
git clone --recurse-submodules https://github.com/MOLAorg/mola.git
cd mola/
mkdir build
cd build
cmake ..
cmake --build .

# test
make test

# add to path
echo 'set $PATH=$PATH:$HOME/mola/build/bin' >> ~/.bashrc

# Updating sources for rebuilding
# cd MOLA_SOURCE_ROOT_DIR
# git pull
# git submodule update --init
# cd build
# cmake ..
# cmake --build .

