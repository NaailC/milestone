import logging
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "db_endpoint"
key = 'db_secret_key'

client = CosmosClient(endpoint, key)

database_name = 'milestonedb'
database = client.create_database_if_not_exists(id=milestonedb)

container_name = 'MilestoneContainer'

container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    letters = requests.get('https://naailmilestone.azurewebsites.net/api/service2?code=BPNkyMxrIWApzFszQjBGMWyCxe4DUqYL1xsklM/paG5p4o4MFi0Mhg==')
    numbers = requests.get('https://naailmilestone.azurewebsites.net/api/service3?code=NrXxNTSbHaoLsEZisdkBYSyeMHwdsn/cj3FyPCAhdYh9yi5buW/qFA==')
    
    username = letters.text + numbers.text

    container.create_item(body={'id' : str(1), 'username' : username })

    return func.HttpResponse(
        str(username),
        status_code=200
    )
