from google.cloud import bigquery

#criar um Client que vai receber as infos dos datasets que estão dentro do BiqQuery
#Client objects são a conexão com o BigQuery service
client = bigquery.Client();

#constroi uma referencia ao dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data"); #projects são coleções de datasets
dataset = client.get_dataset(dataset_ref); #dataset são coleções de tables

tables = list(client.list_tables(dataset));

for table in tables:
    print(table.table_id);

#constroi uma referencia a uma das tabelas do dataset
table_ref = dataset_ref.table("full");
table = client.get_table(table_ref);

#schema é a estrutura de uma tabela