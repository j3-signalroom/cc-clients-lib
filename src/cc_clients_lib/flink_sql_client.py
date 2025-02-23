from typing import Tuple
import requests
from requests.auth import HTTPBasicAuth


__copyright__  = "Copyright (c) 2025 Jeffrey Jonathan Jennings"
__license__    = "MIT"
__credits__    = ["Jeffrey Jonathan Jennings (J3)"]
__maintainer__ = "Jeffrey Jonathan Jennings (J3)"
__email__      = "j3@thej3.com"
__status__     = "dev"


# Flink SQL Config Keys.
FLINK_API_KEY = "flink_api_key"
FLINK_API_SECRET = "flink_api_secret"
ORGANIZATION_ID="organization_id"
ENVIRONMENT_ID="environment_id"
CLOUD_PROVIDER="cloud_provider"
CLOUD_REGION="cloud_region"
COMPUTE_POOL_ID="compute_pool_id"


class FlinkSqlClient():
    def __init__(self, flink_sql_config: dict):
        self.organization_id = flink_sql_config[ORGANIZATION_ID]
        self.environment_id = flink_sql_config[ENVIRONMENT_ID]
        self.flink_api_key = str(flink_sql_config[FLINK_API_KEY])
        self.flink_api_secret = str(flink_sql_config[FLINK_API_SECRET])
        self.cloud_provider = flink_sql_config[CLOUD_PROVIDER]
        self.cloud_region = flink_sql_config[CLOUD_REGION]
        self.compute_pool_id = flink_sql_config[COMPUTE_POOL_ID]
        self.flink_sql_base_url = f"https://flink.${self.cloud_region}.${self.cloud_provider}.confluent.cloud/sql/v1/organizations/${self.organization_id}/environments/${self.environment_id}/"

    def delete_flink_statement(self, statement_name: str) -> Tuple[int, str]:
        """This function submits a RESTful API call to delete a Flink SQL statement.

        Arg(s):
            statement_name (str):  The Flink SQL statement name.

        Returns:
            int:    HTTP Status Code.
            str:    HTTP Error, if applicable.
        """
        # The Flink SQL endpoint to delete a statement.
        endpoint = f"{self.flink_sql_base_url}statements/{statement_name}"

        try:
            # Send a DELETE request to delete the statement.
            response = requests.delete(endpoint, auth=HTTPBasicAuth(self.flink_api_key, self.flink_api_secret))
            return response.status_code, response.text
        except Exception as e:
            return 500, str(e)