// Inject all shared <head> assets
(function() {
  const head = document.head;

  const tags = [
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">',
    '<link rel="stylesheet" href="/assets/css/styles.css">',
    '<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32x32.png">',
    '<link rel="icon" type="image/png" sizes="16x16" href="/assets/img/favicon-16x16.png">',
    '<link rel="shortcut icon" href="/assets/img/favicon.ico">',
    '<link rel="apple-touch-icon" sizes="180x180" href="/assets/img/apple-touch-icon.png">',
    '<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/android-chrome-192x192.png">',
    '<link rel="icon" type="image/png" sizes="512x512" href="/assets/img/android-chrome-512x512.png">'
  ];

  tags.forEach(tag => {
    const temp = document.createElement('div');
    temp.innerHTML = tag;
    head.appendChild(temp.firstChild);
  });
})();
