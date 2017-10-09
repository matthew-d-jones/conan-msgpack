project(msgpack_test)

set(CMAKE_CXX_STANDARD 11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(msgpack_test main.cpp)
target_include_directories(msgpack_test PRIVATE ${CONAN_INCLUDE_DIRS})
target_compile_definitions(msgpack_test PRIVATE ${CONAN_DEFINES})