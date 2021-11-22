# just-like-https 🔒
Trabalho avaliativo de Segurança de Sistemas (2021/2)

```
git clone https://github.com/jmfantin2/just-like-https.git
cd just-like-https/
py app.py
```

feito com `python 3.7.3` e `pycrypto 2.6.1`

---
mid development helpers
---

from https://stackoverflow.com/questions/10836320/on-diffie-hellman-key-exchange
``` python 
#!/usr/bin/python
p=141301# publicly known 
g=5728435 # publicly known
x=76435 # only Alice knows this 
y=37846 # only Bob knows this
aliceSends = (g**x)%p 
aliceComputes = (bobSends**x)%p
bobSends = (g**y)%p
bobComputes = (aliceSends**y) %p
bobSends = (g**y)%p
bobComputes = (aliceSends**y) %p
print ("Alice sends    ", aliceSends )
print ("Bob computes   ", bobComputes )
print ("Bob sends      ", bobSends)
print ("Alice computes ", aliceComputes)
```
