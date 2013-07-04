Sublime Text - Configuration files
==================================

## Sublime Text 3

Icon and links are automatically added by the `.deb` package.

### Preferences
My preferences + Theme Soda little modification.

### Packages
- Theme - Soda: https://github.com/buymeasoda/soda-theme.git

## Sublime Text 2

### Install Package Control
    import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'

### Links
    ln -s $HOME/Sublime\ Text\ 2/sublime_text /usr/bin/sublime
    copy icons to .local/share/icons/

### Packages
- Sass
- Djaneiro
- jQuery Snippets pack
- ZenCoding
- Theme - Soda: https://github.com/buymeasoda/soda-theme.git

### Theme - Soda changes
Soda Dark.sublime-theme:378

from: "viewport_color": [255, 255, 255, 35]

to:   "viewport_color": [0, 0, 0, 35]
