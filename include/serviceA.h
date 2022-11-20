#pragma once

#ifndef CONAN_DEMO_SERVICE_A_LIBRARY_H
#define CONAN_DEMO_SERVICE_A_LIBRARY_H

#ifdef _WIN32
  #define serviceA_EXPORT __declspec(dllexport)
#else
  #define serviceA_EXPORT
#endif

serviceA_EXPORT void serviceA();

#endif //CONAN_DEMO_SERVICE_A_LIBRARY_H
