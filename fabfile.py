from fabric.api import local

def test():
    """Ping all hosts"""
    local('ansible all -m ping -i hosts')

def deploy(inventory='hosts'):
    """Execute playbook using a given inventory file"""
    local('ansible-playbook -i %s site.yml' % inventory)

