import logging

def congig_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s::%(lineno)s %(message)s')
