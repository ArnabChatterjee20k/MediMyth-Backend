from algoliasearch.search_client import SearchClient
from system.Config import Config
def connect_to_algolia_client():
    app_id = Config.ALGOLIA_APP_ID
    api_key = Config.ALOGOLIA_API_KEY_ADMIN
    return SearchClient.create(app_id,api_key)