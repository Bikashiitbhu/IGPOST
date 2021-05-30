  
def getEndPointParams( params ) :
	""" 
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
	
	"""

	endpointParams = dict() 
	endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' 
	endpointParams['access_token'] = params['access_token']
	return endpointParams



def getUrl(params):
	url = params['endpoint_base'] + params['instagram_account_id']
	return url


#params = getCreds() # get creds
#response = getMedia( params ) # hit the api for the data

