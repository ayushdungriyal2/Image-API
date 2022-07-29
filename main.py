# Import API class from pexels_api package
from pexels_api import API
# Type your Pexels API
PEXELS_API_KEY = '563492ad6f91700001000001f81ef0ee5d0b4e8f9f5a8f8f9dc6ea22'
# Create API object
api = API(PEXELS_API_KEY)
# Search five 'kitten' photos
api.search('Python Programmer', page=1, results_per_page=80)
# Get photo entries
photos = api.get_entries()
# Loop the five photos
for photo in photos:
    # Print large2x size url
    print('Photo large2x size: ', photo.large2x)
