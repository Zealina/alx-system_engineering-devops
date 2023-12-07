# Install Nginx on a system using puppet
package {'nginx':
  ensure  => 'installed',
}
file {'/usr/share/nginx/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}
file {'/usr/share/nginx/html/error-404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
}
$block = @(END)
server {
    listen 80;
    server_name _;

    location / {
        root /usr/share/nginx/html;
        index index.html;

        rewrite ^/redirect_me  https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
    error_page 404 /error-404.html;
}
END
file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $block,
  replace => true,
}
service {'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
