# Modify the maximun number of file allowed to be open
exec { 'increase-ulimit':
  command => 'sed -i "s/ULIMIT=\"-n.*\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}->
exec { 'increase-worker_connections':
  command => 'sed -i "s/worker_connections.*/worker_connections 1024;/" /etc/nginx/nginx.conf',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}->
exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
