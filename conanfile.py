from conans import ConanFile, tools

import os


class MsgpackConan(ConanFile):
    name = "msgpack"
    version = "2.1.5"
    license = "MIT"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "MessagePack is an efficient binary serialization format"
    #exports_sources = "include/*"

    @property
    def extracted_dir(self):
        return "msgpack-{0}".format(self.version)
 
    def source(self):
        archive = "msgpack.tar.gz"
        tools.download("https://github.com/msgpack/msgpack-c/releases/download"
                       "/cpp-{v}/msgpack-{v}.tar.gz".format(v=self.version),
                       archive)
        tools.untargz(archive)

    def build(self):
        pass # silence warning

    def package(self):
        self.copy("*.h", dst="include", 
                  src=os.path.join(self.extracted_dir, "include"))
        self.copy("*.hpp", dst="include", 
                  src=os.path.join(self.extracted_dir, "include"))

    def package_info(self):
        self.cpp_info.includedirs.append(os.path.join(self.package_folder, "include"))
        self.cpp_info.defines.append("MSGPACK_CONAN_PACKAGE")