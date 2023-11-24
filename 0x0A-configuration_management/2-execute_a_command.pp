# Use puppet to kill a process
exec {'pkill':
command => 'pkill -f killmenow',
onlyif  => 'pgrep -f killmenow',
}
