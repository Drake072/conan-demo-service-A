from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class LoggerConan(ConanFile):
    name = "serviceA"
    version = "1.0"

    # Optional metadata
    license = "MIT"
    author = "keda"
    url = "https://github.com/Drake072/conan-demo-logger.git"
    description = "A simple service for demo purpose"
    topics = ("demo", "service")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "src/CMakeLists.txt", "src/*.cpp", "src/include/*"

    generators = "cmake_find_package"

    def requirements(self):
        self.requires("logger/1.0")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self, src_folder="src")
        # self.folders.source = "src"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        # self.run('cd src && cmake . %s' % cmake.command_line)
        # self.run("cd src && cmake --build . %s" % cmake.build_config)
        cmake = CMake(self)
        # print("install_folder -----------------------" + self.install_folder)
        # print("build_folder -----------------------" + self.build_folder)
        # print("package_folder-----------------------" + self.package_folder)
        # print("generators_folder-----------------------" + self.generators_folder)
        print("CMAKE_MODULE_PATH:-----------------------" + self.build_folder)
        cmake.configure({'CMAKE_MODULE_PATH': self.build_folder})
        # cmake.configure({'CMAKE_MODULE_PATH': self.folders.generators_folder})
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.a", dst="lib")
        self.copy("*.h")

    def package_info(self):
        # self.cpp_info.libs = ["serviceA"]
        self.cpp_info.libs = self.collect_libs()
