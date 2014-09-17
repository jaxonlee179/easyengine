# Install mail scanner packages

function ee_mod_setup_mailscaner()
{
	# Configure Amavis

	ee_lib_echo "Setting up Amavis, please wait..."
	sed -i "s'#@'@'" /etc/amavis/conf.d/15-content_filter_mode && \
	sed -i "s'#   '   '" /etc/amavis/conf.d/15-content_filter_mode \
	|| ee_lib_error "Unable to setup Amavis, exit status = " $?

	# Add mail filtering rules
	sed -i "s/use strict;/use strict;\n\$sa_spam_subject_tag = undef;\n\$spam_quarantine_to  = undef;\n\$sa_tag_level_deflt  = undef;\n\n# Prevent spams from automatically rejected by mail-server\n\$final_spam_destiny  = D_PASS;\n# We need to provide list of domains for which filtering need to be done\n@lookup_sql_dsn = (\n    ['DBI:mysql:database=vimbadmin;host=127.0.0.1;port=3306',\n     'vimbadmin',\n     'password']);\n\n\$sql_select_policy = 'SELECT domain FROM domain WHERE CONCAT("@",domain) IN (%k)';/" /etc/amavis/conf.d/50-user \
	|| ee_lib_error "Unable to setup Amavis, exit status = " $?

	sed -i "s'\@local_domains_acl = ( \".\$mydomain\" );'\@local_domains_acl = ( \".\" );'" /etc/amavis/conf.d/05-domain_id \
	|| ee_lib_error "Unable to setup Amavis, exit status = " $?

	# Configure Postfix to use Amavis
	# For postfix main.cf
	postconf -e "content_filter = smtp-amavis:[127.0.0.1]:10024"

	# For postfix master.cf
	sed -i "s/1       pickup/1       pickup\n        -o content_filter=\n        -o receive_override_options=no_header_body_checks/" /etc/postfix/master.cf \
	|| ee_lib_error "Unable to setup Amavis, exit status = " $?
	cat /usr/share/easyengine/mail/amavis-master.cf >> /etc/postfix/master.cf

	# Grep ViMbAdmin host and Password from Postfix Configuration
	ee_vimbadmin_host=$(grep hosts /etc/postfix/mysql/virtual_alias_maps.cf | awk '{ print $3 }')
	ee_vimbadmin_password=$(grep password /etc/postfix/mysql/virtual_alias_maps.cf | awk '{ print $3 }')
	
	# Changing hosts and password of ViMbAdmin database in Amavis configuration
	sed -i "s/127.0.0.1/$ee_vimbadmin_host/" /etc/amavis/conf.d/50-user &&
	sed -i "s/password/$ee_vimbadmin_password/" /etc/amavis/conf.d/50-user \
	|| ee_lib_error "Unable to setup ViMbAdmin database details in Amavis configuration, exit status = " $?

	# Configure ClamAv and Amavis to each other files
	adduser clamav amavis &>> $EE_COMMAND_LOG
	adduser amavis clamav &>> $EE_COMMAND_LOG
	chmod -R 775 /var/lib/amavis/tmp &>> $EE_COMMAND_LOG

	# Update ClamAV database (freshclam)
	ee_lib_echo "Updating ClamAV database, please wait..."
	freshclam &>> $EE_COMMAND_LOG

	service clamav-daemon restart &>> $EE_COMMAND_LOG \
	|| ee_lib_echo "Unable to start ClamAV deamon"

}
