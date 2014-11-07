# Install php5-fpm package

function ee_mod_install_php()
{
	ee_lib_echo "Installing PHP, please wait..."
	$EE_APT_GET install php5-common php5-mysqlnd php5-xmlrpc \
	php5-curl php5-gd php5-cli php5-fpm php5-imap php5-mcrypt php5-xdebug \
	php5-memcache memcached php5-geoip 2>&1 || ee_lib_error "Unable to install PHP5, exit status = " $?
}
