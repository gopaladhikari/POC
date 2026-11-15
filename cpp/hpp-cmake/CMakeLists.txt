cmake_minimum_required(VERSION 3.16)

set(CMAKE_CXX_COMPILER "C:/Users/gopua/AppData/Local/Microsoft/WinGet/Packages/BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe/mingw64/bin/g++.exe")

project(cmake_test VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Point CMake directly to your WinLibs GCC 14+ compiler

# Include header directory
include_directories(include)

# Build executable from source files
add_executable(cmake_test
    src/main.cpp
    src/KeyValueStore.cpp
)