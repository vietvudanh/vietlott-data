"""
"""
__author__ = 'Viet Vu'

import itertools
import logging

import requests





def fetch_wrapper(url, headers, org_params, org_body, process_result_fn):
    """
    return a fn to fetch data for a set of params and body
    """
    def fetch(data):
        """
        perform fetching on multiple requests
        replace: org_params, org_body
        :param data: tuple of (update_params, update_body)
        :return:
        """

        with requests.session() as session:
            results = []
            for update_params, update_body in data:
                p = org_params.copy()
                b = org_body.copy()

                p.update(update_params)
                b.update(update_body)

                res = session.post(url, json=b, params=p, headers=headers)

                if not res.ok:
                    logging.info(p)
                    continue

                result = process_result_fn(p, b, res.json())
                results.append(result)
            logging.info(f'task {len(data)} done')
            return results

    return fetch
