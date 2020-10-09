# Add a higher upper limit to Nginx configuration

file {'/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 4096"',
} ~>
service { 'nginx':
  ensure => running
}

