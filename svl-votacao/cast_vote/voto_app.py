from pprint import pprint
import random
import boto3

from voto_registro import *
import logging

if __name__ == '__main__':

    logging.basicConfig(level = logging.ERROR)
    logging.info("** Aplicacao Iniciada **")

    for x in range(0, 5):
        voto_resp = put_voto(get_eleitor_code(), get_candidato_code())
        logging.info(voto_resp)
        #pprint(voto_resp, sort_dicts=False)