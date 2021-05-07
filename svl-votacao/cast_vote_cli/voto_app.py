from pprint import pprint
import random
import boto3
import logging
import sys

sys.path.insert(1, '../cast_vote')
from voto_registro import *

if __name__ == '__main__':

    logging.basicConfig(level = logging.ERROR)
    logging.info("** Aplicacao Iniciada **")
    eleitor=get_eleitor_code()
    put_voto(eleitor, "90")

    for x in range(0, 2):
        voto_resp = put_voto(get_eleitor_code(), get_candidato_code())
        logging.info(voto_resp)
        3.9pprint(voto_resp, sort_dicts=False)