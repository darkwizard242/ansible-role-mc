import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mc_binary_exists(host):
    assert host.file('/usr/local/bin/mc').exists


def test_mc_binary_file(host):
    assert host.file('/usr/local/bin/mc').is_file


def test_mc_binary_which(host):
    assert host.check_output('which mc') == '/usr/local/bin/mc'
