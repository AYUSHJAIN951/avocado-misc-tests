#!/usr/bin/env python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: 2021 IBM
# Author: Nageswara R Sastry <rnsastry@linux.ibm.com>

from avocado import Test
from avocado.utils import process
from avocado.utils import distro
from avocado import skipIf
from avocado.utils.software_manager.manager import SoftwareManager

IS_KVM_GUEST = 'qemu' in open('/proc/cpuinfo', 'r').read()


class lparstat(Test):

    """
    Test case to validate lparstat functionality. lparstat is
    a tool to display logical partition related information and
    statistics

    :avocado: tags=ras,ppc64le
    """

    @skipIf(IS_KVM_GUEST, "This test is not supported on KVM guest platform")
    def setUp(self):
        sm = SoftwareManager()
        detected_distro = distro.detect()
        if 'SuSE' in detected_distro.name:
            package = "powerpc-utils"
        elif 'rhel' in detected_distro.name:
            package = "powerpc-utils-core"
        elif detected_distro.name in ['Ubuntu', 'debian']:
            package = "powerpc-ibm-utils"
        else:
            self.cancel('Unsupported OS %s' % detected_distro.name)

        if not sm.check_installed(package) and not sm.install(package):
            self.cancel("Failed to install %s" % package)

    def test_list(self):
        """
        Test supported command line options
        """
        lists = self.params.get('list',
                                default=['-i', '-x', '-E', '-l', '1 2'])
        for list_item in lists:
            cmd = "lparstat %s" % list_item
            if process.system(cmd, ignore_status=True, sudo=True):
                self.log.info("%s command failed" % cmd)
                self.fail("lparstat: %s command failed to execute" % cmd)

    def test_nlist(self):
        """
        Negative tests
        """
        lists = self.params.get('nlist', default=['--nonexistingoption'])
        for list_item in lists:
            cmd = "lparstat %s" % list_item
            if not process.system(cmd, ignore_status=True, sudo=True):
                self.log.info("%s command passed" % cmd)
                self.fail("lparstat: Expected failure, %s command exeucted \
                          successfully." % cmd)
