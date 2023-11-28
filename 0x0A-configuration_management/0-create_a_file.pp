#create school file with content 'I love Puppet'
file {'/tmp/school':
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
content => 'I love Puppet'
}
