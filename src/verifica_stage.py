import requests
import urllib3
import glob
import os
import shutil
from requests.exceptions import HTTPError
from os import listdir
from os.path import isfile, join

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

edc_url = 'http://infaserver.localdomain:9085'
edc_resource_like = '"rsc_STAGE_TEST"'
page_size = "2"
pass_edc = "Basic QWRtaW5pc3RyYXRvcjppbmZhQDEyMw=="

path = 'C:/users/leona/PycharmProjects/case_santander/stage'
# df: DataFrame = pd.DataFrame(columns=['table_name', 'dat_ref'])
table_name = []
table_name_dup = []
table_ref_data = []
# Cria a lista dos arquivos do diretorio.
list_files = [f for f in listdir(path) if isfile(join(path, f))]

# Caso esteja no formato esperado de table_name+datref, o nome da tabela eh separado.
for table_find in list_files:
    table_cut = table_find.split("-", 1)
    table_name.append(table_cut[0])
    table_ref_data.append(table_cut[1])

# Remove da lista arquivos da mesma tabela.
for remove_dup in table_name:
    if remove_dup not in table_name_dup:
        table_name_dup.append(remove_dup)

for table_edc in table_name_dup:
    url2 = (edc_url + "/access/2/catalog/data/objects?includeDstLinks=true&includeRefObjects=false&includeSrcLinks"
                      "=true&offset=0&pageSize=2&q=core.resourceName%3A%22rsc_STAGE_TEST%22%20AND%20core.classType%3A"
                      "%22com.infa.ldm.file.delimited.DelimitedFile%22AND%20core.name%3A%22" + table_edc + "%22")
    try:
        response2 = requests.get(url2, headers={"Authorization": pass_edc}, verify=False)
        data = response2.json()
        print(data["metadata"]["totalCount"])
        response2.raise_for_status()
    except HTTPError:
        print('Falha ao buscar as informações na lista, veriquei disponibilidade do serviço ou usuário e senha!')
        exit(2)

    if data["metadata"]["totalCount"] == 0:
        list_of_files = glob.glob('C:/users/leona/PycharmProjects/case_santander/stage/' + table_edc + '*')
        latest_file = max(list_of_files, key=os.path.getctime)
        shutil.move(latest_file, 'C:/users/leona/PycharmProjects/case_santander/temp/' + table_edc)
