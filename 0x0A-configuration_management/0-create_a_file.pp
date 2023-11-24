# Ensure the presence of the file school
node default {
  file { '/tmp/school':
    ensure  => file,
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
  }
}
