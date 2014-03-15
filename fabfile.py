from fabric.api import local

def test():
    """Ping all hosts"""
    local('ansible all -m ping -i hosts')

def provision(inventory='hosts', play='site.yml'):
    """Execute playbook using a given inventory file"""
    local('ansible-playbook -i %s %s' % (inventory, play))

