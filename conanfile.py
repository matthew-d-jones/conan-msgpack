#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class MsgpackConan(ConanFile):
    name = "msgpack"
    version = "1.4.2"
    description = "The official C++ library for MessagePack"
    url = "https://github.com/matthew-d-jones/conan-msgpack"
    license = "BSL-1.0"
    exports = ["LICENSE-bincrafters.md"]
    source_subfolder = "source_subfolder"
        
    def source(self):
        source_url = "https://github.com/msgpack/msgpack-c"
        archive_name = self.name + "-" + self.version
        tools.get("{0}/releases/download/cpp-{1}/{2}.tar.gz"
            .format(source_url,  self.version, archive_name))
            
        os.rename(archive_name, self.source_subfolder)
        
    def build(self):
        pass # silence warning

    def package(self):
        include_dir = os.path.join(self.source_subfolder, "include")
        self.copy("LICENSE_1_0.txt", dst="license", src=self.source_subfolder)
        self.copy("*.h", dst="include", src=include_dir)
        self.copy("*.hpp", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()

