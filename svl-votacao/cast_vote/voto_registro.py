import random
import boto3
import logging 

def put_voto(eleitor, candidato):
    logging.info("** Novo Voto incluido **")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EleicoesPresidente')
    response = table.put_item(
       Item={
            'eleitor': eleitor,
            'candidato': candidato
        }
    )
    return response

def get_eleitor_code():
    logging.info("** Obtido codigo do Eleitor **")
    eleitor_id = random.randint(0, 10000000)
    return str(eleitor_id)

def get_candidato_code():
    logging.info("** Obtido Numero do Candidato **")
    candidatos = ['13', '45', '10']
    candidatos_id = random.choice(candidatos)
    return str(candidatos_id)