class BaseProduct:
    name = ""
    url = ""
    page_to_run: int = 1
    stored_data_dtype = {}

    org_body = None
    org_params = None

    product_config = None

    def process_result(self, params, body, res_json, task_data):
        pass

    def crawl(self, run_date_str, index_to):
        pass
