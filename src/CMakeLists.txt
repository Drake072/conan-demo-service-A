cmake_minimum_required(VERSION 3.15)
project(serviceA CXX)

#include(${CONAN_INSTALL_DIR}/conanbuildinfo.cmake)
#conan_basic_setup(TARGETS)

MESSAGE (STATUS "----------------------- CMAKE_MODULE_PATH: ${CMAKE_MODULE_PATH}")
find_package(logger)

add_library(serviceA STATIC serviceA.cpp)
target_include_directories(serviceA PUBLIC include)

if (logger_FOUND)
    target_link_libraries(serviceA logger::logger)
else()
    message(FATAL_ERROR "lib logger not found")
endif()

MESSAGE (STATUS "----------------------- CMAKE_CURRENT_SOURCE_DIR: ${CMAKE_CURRENT_SOURCE_DIR}")
MESSAGE (STATUS "----------------------- CMAKE_BINARY_DIR: ${CMAKE_BINARY_DIR}")
MESSAGE (STATUS "----------------------- CMAKE_LIBRARY_OUTPUT_DIRECTORY: ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")
MESSAGE (STATUS "----------------------- LIBRARY_OUTPUT_PATH: ${LIBRARY_OUTPUT_PATH}")
MESSAGE (STATUS "----------------------- CMAKE_RANLIB: ${CMAKE_RANLIB}")
MESSAGE (STATUS "----------------------- CMAKE_AR: ${CMAKE_AR}")
MESSAGE (STATUS "----------------------- CMAKE_LIBRARY_OUTPUT_DIRECTORY: ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}")



add_custom_target(combined ALL 
    COMMAND echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    COMMAND rm -rf          ${CMAKE_BINARY_DIR}/tmp &&  mkdir ${CMAKE_BINARY_DIR}/tmp
    COMMAND cd              ${CMAKE_BINARY_DIR}/tmp &&  echo "Archive reconstruction in `pwd`"
    COMMAND mv              ${CMAKE_BINARY_DIR}/libserviceA.a ${CMAKE_BINARY_DIR}/tmp/libserviceAUnbundled.a
    COMMAND cd              ${CMAKE_BINARY_DIR}/tmp &&  ${CMAKE_AR} x ${CMAKE_BINARY_DIR}/tmp/libserviceAUnbundled.a
    COMMAND cd              ${CMAKE_BINARY_DIR}/tmp &&  ${CMAKE_AR} x "${logger_LIB_DIRS}/liblogger.a"
    COMMAND cd              ${CMAKE_BINARY_DIR}/tmp &&  ${CMAKE_AR} cr "${CMAKE_BINARY_DIR}/libserviceA.a"  ./*.o
    COMMAND ${CMAKE_RANLIB} ${CMAKE_BINARY_DIR}/libserviceA.a
#    COMMAND rm -rf ${CMAKE_BINARY_DIR}/tmp
    COMMAND echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    DEPENDS serviceA
    )


INSTALL (FILES "include/serviceA.h" DESTINATION ${CMAKE_BINARY_DIR}/install/include)
INSTALL (FILES "${CMAKE_BINARY_DIR}/lib/libserviceA.a" DESTINATION ${CMAKE_BINARY_DIR}/install/lib)
