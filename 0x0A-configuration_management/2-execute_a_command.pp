# Task 2
# Executes a command
exec { 'killmenow':
command => '/usr/bin/pkill killmenow'
}
