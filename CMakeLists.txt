cmake_minimum_required(VERSION 3.15)
project(serviceA CXX)

add_library(serviceA src/serviceA.cpp)
target_include_directories(serviceA PUBLIC include)
target_link_libraries(serviceA ${CMAKE_SOURCE_DIR}/lib/liblogger.a)

set_target_properties(serviceA PROPERTIES PUBLIC_HEADER "include/serviceA.h")
install(TARGETS serviceA)

add_executable(test src/serviceA.cpp)
target_include_directories(test PUBLIC include)
target_link_libraries(test ${CMAKE_SOURCE_DIR}/lib/liblogger.a)