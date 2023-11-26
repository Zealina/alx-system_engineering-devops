# make ~/.ssh/school the name of the private key on server 54.236.30.99
# refuse authentication using a password

include ::stdlib

file { '/etc/ssh/ssh_config':
  ensure  => present,
} ~>
file_line { 'Off Pwd Auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '.*PasswordAuthentication yes.*',
  replace => true,
} ~>
file_line { 'Change Identity File':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '.*IdentityFile ~/.ssh/id_rsa.*',
  replace => true,
}
