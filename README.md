[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-mc.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-mc) ![Ansible Role](https://img.shields.io/ansible/role/48533?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/48533?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/48533?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-mc&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-mc) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-mc?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-mc?color=orange&style=flat-square)

# Ansible Role: mc

Role to install (_by default_) [mc](https://github.com/minio/mc) on **Debian/Ubuntu** and **EL** systems. 'mc' is [MinIO](https://min.io/) client that supports interacting with filesystems and Amazon S3 compatible cloud storage service..

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
mc_app: mc
mc_dl_url: https://dl.min.io/client/{{ mc_app }}/release/linux-amd64/{{ mc_app }}
mc_bin_path: "/usr/local/bin/{{ mc_app }}"
mc_bin_permission_mode: '0755'
```

### Variables table:

Variable               | Value (default)                                                          | Description
---------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------
mc_app                 | mc                                                                       | Defines the app to install i.e. **mc**
mc_dl_url              | <https://dl.min.io/client/{{> mc_app }}/release/linux-amd64/{{ mc_app }} | Defines URL to download the mc binary from.
mc_bin_path            | "/usr/local/bin/{{ mc_app }}"                                            | Defined to dynamically set the appropriate path to store mc binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin/mc**
mc_bin_permission_mode | '0755'                                                                   | Defines the permission mode level for the file.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
