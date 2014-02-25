PHP5 Ansible Playbooks
=========================

There's hardly a better option than to use Ansible for provisioning your computing nodes.

To test that ALL hosts are reachable:

    $ ansible all -m ping -i hosts

To provision ALL machines:

    $ ansible-playbook -i hosts site.yml
