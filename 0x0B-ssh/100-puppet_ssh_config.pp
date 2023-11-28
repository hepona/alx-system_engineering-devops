#!/usr/bin/env puppet
# puppet automatisation

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => '
      # SSH configuration file
      Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
',
}
