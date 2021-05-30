import requests
import json

def getCreds() :

	creds = dict() # dictionary to hold everything
	creds['access_token'] = 'ACCESS-TOKEN' # access token for use with all api calls
	creds['client_id'] = 'FB-APP-CLIENT-ID' # client id from facebook app IG Graph API Test
	creds['client_secret'] = 'FB-APP-CLIENT-SECRET' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = 'v10.0' # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['page_id'] = 'FB-PAGE-ID' # users page id
	creds['instagram_account_id'] = 'INSTAGRAM-BUSINESS-ACCOUNT-ID' # users instagram account id
	creds['ig_username'] = 'IG-USERNAME' # ig username

	return creds

