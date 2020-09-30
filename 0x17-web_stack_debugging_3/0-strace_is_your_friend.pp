# Task 0
# Fix Wordpress site with faulty settings
include stdlib

file { '.htaccess':
ensure => present,
path => '/var/www/html',
mode => '0666',
group => 'www-data',
owner => 'www-data',
conctent => 'DirectoryIndex index.php'
}

file_line { 'wp-settings.php':
ensure => present,
path => '/var/www/html',
line => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
match => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );"
}
