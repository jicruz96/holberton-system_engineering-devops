# Task 0
# Fix Wordpress site with faulty settings

file { '.htaccess':
ensure => 'present',
path => '/var/www/html/.htaccess',
mode => '0666',
group => 'www-data',
owner => 'www-data',
content => 'DirectoryIndex index.php'
}

file_line { 'replace phpp':
ensure => 'present',
path => '/var/www/html/wp-settings.php',
line => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
match => 'class-wp-locale.phpp'
}


exec { 'restart apache':
path => '/usr/bin/',
command => 'sudo service apache2 restart'
}
