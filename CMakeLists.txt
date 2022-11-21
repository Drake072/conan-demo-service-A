cmake_minimum_required(VERSION 3.15)
project(serviceA CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(serviceA src/serviceA.cpp)
target_include_directories(serviceA PUBLIC include)
target_link_libraries(serviceA CONAN_PKG::logger)

MESSAGE (STATUS "----------------------- CMAKE_CURRENT_SOURCE_DIR: ${CMAKE_CURRENT_SOURCE_DIR}")
MESSAGE (STATUS "----------------------- CMAKE_BINARY_DIR: ${CMAKE_BINARY_DIR}")
MESSAGE (STATUS "----------------------- CMAKE_LIBRARY_OUTPUT_DIRECTORY: ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")
MESSAGE (STATUS "----------------------- LIBRARY_OUTPUT_PATH: ${LIBRARY_OUTPUT_PATH}")
MESSAGE (STATUS "----------------------- CMAKE_RANLIB: ${CMAKE_RANLIB}")
MESSAGE (STATUS "----------------------- CMAKE_AR: ${CMAKE_AR}")


add_custom_target(combined ALL 
    COMMAND rm -rf ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/tmp    
    COMMAND mkdir ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/tmp
    COMMAND mv   "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/libserviceA.a" "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/tmp/libserviceAUnbundled.a"
    COMMAND rm -f *.o
    COMMAND ar x "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/tmp/libserviceAUnbundled.a"
    COMMAND ar x "${CONAN_LIB_DIRS_LOGGER}/liblogger.a"
    COMMAND ar cr  "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/libserviceA.a"  ./*.o
    COMMAND ranlib ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/libserviceA.a
    DEPENDS serviceA
    )


INSTALL (FILES "include/serviceA.h" DESTINATION ${CMAKE_BINARY_DIR}/include)
