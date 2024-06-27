[![build-test](https://github.com/darkwizard242/ansible-role-mc/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-mc/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-mc/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-mc/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/mc) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-mc&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-mc) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-mc&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-mc) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-mc&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-mc) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-mc?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-mc?color=orange&style=flat-square)

# Ansible Role: mc

Role to install (_by default_) [mc](https://github.com/minio/mc) on **Debian/Ubuntu** and **EL** systems. **mc** is [MinIO](https://min.io/) client that supports interacting with filesystems and Amazon S3 compatible cloud storage service..

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
mc_app: mc
mc_os: "{{ ansible_system | lower }}"
mc_architecture_map:
  amd64: amd64
  arm: arm64
  x86_64: amd64
  armv6l: armv6
  armv7l: armv7
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
mc_dl_url: https://dl.min.io/client/{{ mc_app }}/release/{{ mc_os }}-{{ mc_architecture_map[ansible_architecture] }}/{{ mc_app }}
mc_bin_path: "/usr/local/bin/{{ mc_app }}"
mc_file_owner: root
mc_file_group: root
mc_file_mode: '0755'
```

### Variables table:

Variable            | Description
------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------
mc_app              | Defines the app to install i.e. **mc**
mc_os               | Defines os type. Used for obtaining the correct type of binaries based on OS type.
mc_architecture_map | Defines os architecture. Used to set the correct type of binaries based on OS System Architecture.
mc_dl_url           | Defines URL to download the mc binary from.
mc_bin_path         | Defined to dynamically set the appropriate path to store mc binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin/mc**
mc_file_owner       | Owner for the binary file of mc.
mc_file_group       | Group for the binary file of mc.
mc_file_mode        | Mode for the binary file of mc.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **mc**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.mc
```

For customizing behavior of role (i.e. specifying the desired persmissions for **mc** binary file) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.mc
  vars:
    mc_bin_permission_mode: '0700'
```

For customizing behavior of role (i.e. placing binary of **mc** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.mc
  vars:
    mc_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-mc/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
