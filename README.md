Tecnologias utilizadas no prototipo

Docker Rundeck 
	- Ferramenta de gerenciamento de automações.

VM Horton works 
- Ecosistema Hadoop


Informatica Enterprise Data Catalog 
2 VMs RHE 8.7
Docker Postgres
Docker SQLSERVER
- Ferramenta de descoberta e catalogação dos dados.

Quick installation guide

Docker Rundeck 
  Command - docker run --name some-rundeck -p 4440:4440 -v data:/home/rundeck/server/data rundeck/rundeck:4.8.0
VM Horton works 
  Baixe o virtual data box no link abaixo e instale.
  https://www.virtualbox.org/wiki/Downloads
  Baixe e instale o HDP
  https://www.cloudera.com/downloads/hortonworks-sandbox.html
Informatica Enterprise Data Catalog Trial
  2 VMs RHE 8.7
    https://developers.redhat.com/content-gateway/file/rhel/8.7.0/rhel-8.7-x86_64-boot.iso
  Docker Postgres
  Docker SQLSERVER
    Docker_COMPOSE.yaml
