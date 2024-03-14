exec {"ulimit":
  command =>"sed -i 'ULIMIT=\"-n 1000\"' /etc/default/nginx",
  provider => "shell",
}
exec {"restar nginx":
  command => "service nginx restart",
  provider => "shell",
}
