# Use puppet to install flask from pip3
node default {
package {'flask':
ensure   => '2.1.0',
provider => 'pip3',
}
}
