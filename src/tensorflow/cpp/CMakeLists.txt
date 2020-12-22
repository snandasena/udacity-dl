cmake_minimum_required(VERSION 3.10)
project(neural)

set(CMAKE_CXX_STANDARD 14)
find_library(TENSORFLOW_LIB tensorflow )

add_executable(neural main.cpp)
target_link_libraries (neural "${TENSORFLOW_LIB}")
