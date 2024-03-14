exec { 'ulimit':
  command  =>"sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 10000\"/' /etc/default/nginx",
  provider => 'shell',
}
exec { 'restar nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}
