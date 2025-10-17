"""
fetch data utilities
"""

import json
import re
from typing import Callable, Optional, Tuple

import requests
from loguru import logger

from vietlott.crawler.requests_helper.config import TIMEOUT


def get_vietlott_cookie() -> Tuple[str, dict]:
    """
    Get cookies and tokens from vietlott.vn
    Returns: (cookie_string, cookies_dict)
    """
    # First, get the main page to obtain session cookies
    res = requests.get("https://vietlott.vn/")
    logger.debug(f"Initial cookies from vietlott.vn: {res.cookies}")
    
    # Extract cookies from response
    cookies = {}
    cookie_parts = []
    for cookie_name, cookie_value in res.cookies.items():
        cookies[cookie_name] = cookie_value
        cookie_parts.append(f"{cookie_name}={cookie_value}")
    
    # Try to extract cookie from JavaScript if present
    match = re.search(r'document.cookie="(.*?)"', res.text)
    if match:
        extra_cookie = match.group(1)
        cookie_key, cookie_val = extra_cookie.split("=", 1)
        cookies[cookie_key] = cookie_val
        cookie_parts.append(extra_cookie)
        logger.debug(f"Found JS cookie: {extra_cookie}")
    
    cookie_string = "; ".join(cookie_parts) if cookie_parts else ""
    logger.debug(f"Final cookie string: {cookie_string}")
    logger.debug(f"Final cookies dict: {cookies}")
    
    return cookie_string, cookies


def fetch_wrapper(
    url: str,
    headers: Optional[dict],
    org_params: Optional[dict],
    org_body: dict,
    process_result_fn: Callable,
    cookies: Optional[dict],
):
    """
    return a fn to fetch data for a set of params and body
    """

    def fetch(tasks):
        """
        perform fetching on multiple requests
        replace: org_params, org_body
        :param tasks: list of dict(task_id, task_data{params, body})
        :return:
        """
        tasks_str = ",".join(str(t["task_id"]) for t in tasks)
        logger.debug(f"worker start, tasks_ids={tasks_str}")
        _headers = headers.copy() if headers is not None else {}

        results = []
        for task in tasks:
            task_id, task_data = task["task_id"], task["task_data"]
            params = org_params.copy() if org_params is not None else {}
            body = org_body.copy()

            params.update(task_data["params"])
            body.update(task_data["body"])

            logger.debug(f"Request URL: {url}")
            logger.debug(f"Request headers: {_headers}")
            logger.debug(f"Request cookies: {cookies}")
            logger.debug(f"Request body: {json.dumps(body)[:500]}")
            logger.debug(f"Request params: {params}")

            res = requests.post(
                url,
                data=json.dumps(body),
                params=params,
                headers=_headers,
                cookies=cookies,
                timeout=TIMEOUT,
            )

            logger.debug(f"Response status: {res.status_code}")
            logger.debug(f"Response headers: {dict(res.headers)}")
            logger.debug(f"Response text: {res.text[:500]}")

            if not res.ok:
                logger.error(
                    f"req fail, args={task_data}, code={res.status_code}, text={res.text[:200]}, headers={_headers}, body={body}, params={params}"
                )
                continue
            try:
                result = process_result_fn(params, body, res.json(), task_data)
                results.append(result)
                logger.debug(f"task {task_id} done")
            except json.JSONDecodeError as e:
                logger.error(
                    f"json decode error, args={task_data}, text={res.text[:200]}, headers={headers}, cookies={cookies}, body={body}, params={params}"
                )
                raise e
        logger.debug(f"worker done, tasks={tasks_str}")
        return results

    return fetch
