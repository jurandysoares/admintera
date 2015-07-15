
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Este arquivo pode ser salvo com qualquer extensão, tipo info.html
# A ser salvo em /usr/lib/cgi-bin no Debian/Ubuntu e 
# em /var/www/cgi-bin no Fedora/RedHat/CentOS.

import os

print('Content-type: text/html')
print()

print('''<table border="1">
 <tr>
   <th>Variavel</th>
   <th>Valor</th>
 </tr>
''')

chaves_amb = list(os.environ.keys())
chaves_amb.sort()

for var in chaves_amb:
    print('<tr>')
    print('<td>{}</td>'.format(var))
    print('<td>{}</td>'.format(os.environ[var]))
    print('</tr>')

print('</table>')
