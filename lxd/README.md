# LXD

## Configuração inicial
Referência: https://bayton.org/2016/05/lxd-zfs-and-bridged-networking-on-ubuntu-16-04-lts/

`sudo lxd init`

Saída:
```
[sudo] senha para jurandy: 
Do you want to configure a new storage pool (yes/no) [default=yes]? 
Name of the new storage pool [default=default]: 
Name of the storage backend to use (dir, lvm, zfs) [default=zfs]: 
Create a new ZFS pool (yes/no) [default=yes]? 
Would you like to use an existing block device (yes/no) [default=no]? 
Size in GB of the new loop device (1GB minimum) [default=18GB]: 
Would you like LXD to be available over the network (yes/no) [default=no]? 
Would you like stale cached images to be updated automatically (yes/no) [default=yes]? 
Would you like to create a new network bridge (yes/no) [default=yes]? 
What should the new bridge be called [default=lxdbr0]? 
What IPv4 address should be used (CIDR subnet notation, “auto” or “none”) [default=auto]? 
What IPv6 address should be used (CIDR subnet notation, “auto” or “none”) [default=auto]? 
LXD has been successfully configured.
```
