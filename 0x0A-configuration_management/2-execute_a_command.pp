#manifest that kills a process named killmenow.
exec {'pkill':
path     => '/usr/bin/',
command  => 'pkill -f Killmenow',
unless   => 'pkill -0 -f Killmenow'
}
