# Case Ingestão Governada

Processo de ingestão de dados automatizado e integrado com catálogo de metadados, visando garantir consistência e governança das informações em tempo de execução.


# Tecnologias utilizadas no prototipo

- Docker Rundeck (Ferramenta de gerenciamento de automações.)
- VM Horton works (Ecosistema Hadoop.)
- Informatica Enterprise Data Catalog (Ferramenta de descoberta e catalogação dos dados.)
  - 2x VMs RHE 8.7 
  - Docker Postgres
  - Docker SQLSERVER 


# Quick installation guide

- Docker
  - Baixe e instale o Docker Desktop
>> https://docs.docker.com/desktop/install/windows-install/

- Docker Rundeck
>> docker run --name some-rundeck -p 4440:4440 -v data:/home/rundeck/server/data rundeck/rundeck:4.8.0 </sub>

- VM Horton works 
  - Baixe o virtual data box no link abaixo e instale.
>> https://www.virtualbox.org/wiki/Downloads
  - Baixe e instale o HDP
>> https://www.cloudera.com/downloads/hortonworks-sandbox.html

- Informatica Enterprise Data Catalog Trial
  - 2 VMs RHE 8.7
    - Baixe e instale no Virtual Databox ou em algum servidor que desejar
 >> https://developers.redhat.com/content-gateway/file/rhel/8.7.0/rhel-8.7-x86_64-boot.iso
  - Docker Postgres / Docker SQLSERVER
    docker-compose.yml


Python Scripts
 Twitter_Extract 
 - Script de extração do twitter para demonstrar um processo de extração e Criação de arquivos na área da stage.

 Verifica_Stage
 - Script responsável pelo monitoramento da stage e tomada de decisão da Criação do arquivo de exemplo para catalogação ou se segue para o processo de 		        ingestão.

 Ingestao (Python Script)
 - Script responsável por coletar o metadados técnico e realizar a ingestão dentro do datalake conforme informações fornecidas pelo desenvolvedor.
