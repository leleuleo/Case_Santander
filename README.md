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


Python Scripts
 Twitter_Extract 
 - Script de extração do twitter para demonstrar um processo de extração e Criação de arquivos na área da stage.

 Verifica_Stage
 - Script responsável pelo monitoramento da stage e tomada de decisão da Criação do arquivo de exemplo para catalogação ou se segue para o processo de 		        ingestão.

 Ingestao (Python Script)
 - Script responsável por coletar o metadados técnico e realizar a ingestão dentro do datalake conforme informações fornecidas pelo desenvolvedor.
