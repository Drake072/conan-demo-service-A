cmake_minimum_required(VERSION 3.15)
project(serviceA CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(serviceA src/serviceA.cpp)
target_include_directories(serviceA PUBLIC include)
target_link_libraries(serviceA CONAN_PKG::logger)

INSTALL (FILES "include/serviceA.h" DESTINATION ${CMAKE_BINARY_DIR}/include)
