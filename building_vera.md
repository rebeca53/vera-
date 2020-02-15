Step by step of how a build vera++ with success:
Warning: Command lines are expressed by '>':
> git clone https://bitbucket.org/verateam/vera.git
> cd vera/
> git submodule update --init
> git pull
> git submodule update
> sudo apt-get install libboost-all-dev
> sudo apt autoremove
> sudo apt-get install tk8.5 tcl8.5
> sudo apg-get -y install cmake
> sudo apt-get update
> sudo apt-get install pandoc
- Set VERA_USE_SYSTEM_LUA to OFF in Cmake
> mkdir build
> cd build
> cmake ..
> make -j
> sudo make install