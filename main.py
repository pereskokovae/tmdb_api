import requests


response = requests.get('https://api.themoviedb.org/3/movie/11?api_key=API_KEY')
response.raise_for_status()
