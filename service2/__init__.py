import logging
import random
from string import ascii_lowercase
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters = ''
    for _ in range(5):
        letters += random.choice(ascii_lowercase)
    
    return func.HttpResponse( 
        letters,
        status_code=200
    )
