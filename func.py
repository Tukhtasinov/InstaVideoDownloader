import requests


def video_download(video_path):
	url = "https://instagram-api-special.p.rapidapi.com/instagram/"

	querystring = {"url": video_path}

	headers = {
		"X-RapidAPI-Key": "4923b43de2mshc85e0dc04fca132p1f2700jsneee35b946fe7",
		"X-RapidAPI-Host": "instagram-api-special.p.rapidapi.com"
	}

	try:
		response = requests.get(url, headers=headers, params=querystring)
		data = response.json()
		result = data.get('result')
		video = result[0].get('url')
		return video
	except:
		return 'Error Occured'





