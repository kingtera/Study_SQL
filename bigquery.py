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

#estabelendo limites para a query
query = """     
        SELECT score, title
        FROM `bigquery-public-data.hacker_news.full`
        WHERE type = "job" 
        """

# Only run the query if it's less than 1 MB
ONE_MB = 1000*1000
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_MB)

# Set up the query (will only run if it's less than 1 MB)
safe_query_job = client.query(query, job_config=safe_config)

# API request - try to run the query, and return a pandas DataFrame
safe_query_job.to_dataframe()

#ORDER BY is usually the last clause in your query, and it sorts the results returned by the rest of your query.