# Logger Module

### Create conan recipe if not created

`conan new logger/1.0 --template=cmake_lib`

### Build and install to local cache

`conan create . -pr:b macos_x86_release`

###  Conan Profiles

```
[settings]
  os=Macos
  os_build=Macos
  arch=x86_64
  arch_build=x86_64
  compiler=apple-clang
  compiler.version=14
  compiler.libcxx=libc++
  build_type=Release
[options]
[build_requires]
[env]
```

