pkgname = "findutils"
pkgver = "4.8.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--program-prefix=g",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
hostmakedepends = ["texinfo"]
pkgdesc = "GNU find utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/findutils"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "57127b7e97d91282c6ace556378d5455a9509898297e46e10443016ea1387164"
# FIXME
options = ["!check"]

def post_install(self):
    # we don't want this
    self.rm(self.destdir / "usr/bin/glocate")
    self.rm(self.destdir / "usr/bin/gupdatedb")
    self.rm(self.destdir / "usr/libexec", recursive = True)
    self.rm(self.destdir / "usr/share/man/man1/glocate.1")
    self.rm(self.destdir / "usr/share/man/man1/gupdatedb.1")
    self.rm(self.destdir / "usr/share/man/man5", recursive = True)
