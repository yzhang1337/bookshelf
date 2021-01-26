cmake_minimum_required(VERSION 3.10)

# set the project name
project(bookshelf)

#include_directories(${PROJECT_SOURCE_DIR}/include/bookshelf)
find_package(nlohmann_json 3.2.0 REQUIRED)

#add_subdirectory(src)
find_package(grpc)
# add the executable
add_executable(bookshelf src/main.cpp)
