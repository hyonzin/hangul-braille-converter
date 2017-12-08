# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import hbcvt

def test_success():
    assert hbcvt.h2b.return0() == 0
