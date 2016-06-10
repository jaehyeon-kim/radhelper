### What is _radhelper_.

**radhelper** is a wrapper of [Python ladp library](https://www.python-ldap.org/) and is planned to include a set of functions to work on Windows AD directory.

Currently only one function, **adauth()**, is implemented.

### Prerequisite

Python ldap library should be installed. Tests are maded only on Ubuntu LTS 14.04 and Windows 7.

#### Ubuntu

```r
$ sudo pip install python-ldap
```

If the following error is encountered, install necessary Ubuntu packages.

```r
$ sudo apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
$ sudo pip install python-ldap
```

#### Windows

The easiest way to install this package would be from [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap). I downloaded *python_ldap-2.4.25-cp27-none-win_amd64.whl* and installed as following.

```r
$ pip install python_ldap-2.4.25-cp27-none-win_amd64.whl
```

### Package installation

```r
if (!require("devtools"))
  install.packages("devtools")
devtools::install_github("jaehyeon-kim/radhelper")

library(radhelper)
```

### Usage

```r
library(radhelper)
adauth(address = "host-name-or-ip", user_email = "user-email", password = "password")
```

