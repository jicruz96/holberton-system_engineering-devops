# Task 0
# Fix Wordpress site with faulty settings


exec { 'change phpps':
provider => 'shell';
command => 'cat /var/www/html/wp-settings.php | sed \'s$phpp$php$g\' | sudo tee /var/www/html/wp-settings.php',
}
