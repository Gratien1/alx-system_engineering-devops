# This Puppet manifest copies the 'class-wp-locale.php' file to 'class-wp-locale.phpp'
exec { 'fix-wordpress':
  command => 'cp /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  onlyif  => 'test -f /var/www/html/wp-includes/class-wp-locale.php',
  path    => ['/bin', '/usr/bin'],
}
