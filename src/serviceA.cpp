#include "logger.h"
#include "serviceA.h"


void serviceA() {
    info("ServiceA method invoked");
}

int main() {
    serviceA();
}
