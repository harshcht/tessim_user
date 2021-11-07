cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)


set(SRC_FILES offgrid_inverter.cpp
              offgrid_inverter_interface.cpp)

add_library(inverter  SHARED ${SRC_FILES})