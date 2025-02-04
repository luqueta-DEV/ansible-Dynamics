# Ansibles-Inventorys

## Visão Geral
Este projeto contém configurações de **inventorys** para o **Ansible**, facilitando a automação e gerenciamento de servidores.


## Pré-requisitos
- **Ansible** instalado ([guia de instalação](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))
- Acesso SSH aos servidores gerenciados

## Como Usar
### 1. Definir Inventário
Edite os arquivos dentro de `inventory/` para definir os hosts e grupos.

### 2. Configurar Variáveis
- `group_vars/` contém variáveis por grupo.
- `host_vars/` contém variáveis específicas por host.

### 3. Executar um Playbook
Para rodar um playbook específico, use o comando:
```sh
ansible-playbook -i inventory/production playbooks/deploy.yml
```

### 4. Testar Conectividade
Para testar a conexão com os servidores definidos no inventário:
```sh
ansible all -i inventory/production -m ping
```

## Contribuição
Se quiser contribuir, faça um fork do projeto e envie um pull request!

## Licença
Este projeto é distribuído sob a licença MIT. Consulte `LICENSE` para mais detalhes.
