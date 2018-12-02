import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chrony_is_installed(host):
    package = host.package('chrony')

    assert package.is_installed


def test_chronyd_running_and_enabled(host):
    chronyd = host.service('chronyd')

    assert chronyd.is_running
    assert chronyd.is_enabled


def test_centos_release_openstack_rocky_is_installed(host):
    package = host.package('centos-release-openstack-rocky')

    assert package.is_installed


def test_python_openstackclient_is_installed(host):
    package = host.package('python2-openstackclient')

    assert package.is_installed


def test_openstack_selinux_is_installed(host):
    package = host.package('openstack-selinux')

    assert package.is_installed
