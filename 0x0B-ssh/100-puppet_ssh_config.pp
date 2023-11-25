#!/usr/bin/env bash
# Automating my Tasks using Puppet
file { '/etc/ssh/ssh_config':
ensure => present,
content => "
# SSH configuration file
Host *
  IdentityFile ~/ssh/school
    PasswordAuthentication no
"
}
