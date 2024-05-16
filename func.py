import requests


def video_download(video_path):
	url = "https://instagram-downloader.p.rapidapi.com/index"

	querystring = {"url": video_path}

	headers = {
		"X-RapidAPI-Key": "4923b43de2mshc85e0dc04fca132p1f2700jsneee35b946fe7",
		"X-RapidAPI-Host": "instagram-downloader.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	data = response.json()
	d1 = data.get('result')

	return d1.get('video_url')



