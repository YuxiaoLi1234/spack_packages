# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *
import shutil


class Fzvis(Package):
    """visualization software for building and understanding the effects of compression"""

    homepage = "https://szcompressor.org/next.szcompressor.github.io/"
    url = "https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.1.tar.gz"
    git = "https://github.com/YuxiaoLi1234/fzvis"

    maintainers("robertu94", "YuxiaoLi1234", "hrithikdevaiah-999")

    license("MIT")

    version("0.2.0", sha256="bd61d0210adcb70b6b2d189905b6585cd7cf3ea9840a59e6fdae14ea5bb3487d", 
	url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.0.tar.gz")

    version("0.2.1", sha256="7a42bf5d40c1e331d43a0ee1482f6104f0d5d4254e9d2d469362dcde4a7e8fc8", 
	url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.1.tar.gz")

    depends_on("npm", type="build")
    depends_on("libpressio+python+json", type=("run","link"))
    depends_on("libpressio-tools", type=("run", "link"))
    depends_on("py-websockets", type="run")
    depends_on("py-flask", type="run")
    depends_on("py-flask-cors", type="run")

    def install(self, spec, prefix):
        npm = which("npm")
        npm("install")
        npm("run", "build")
        shutil.copytree("dist", prefix.usr.libexec.fzvis.ui)
        mkdir(prefix.bin)
        shutil.copy2("src/components/main.py", prefix.bin.join("fzvis"))
        shutil.rmtree(prefix.join("npm-cache"))

