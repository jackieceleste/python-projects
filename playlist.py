playlist1 = {
	"title": "Sleepybear",
	"author": "Crackjack",
	"songs": [
		{"title": "Apples For The Sun", "artist": ["Frankie Rose"], "album": "Interstellar", "duration in minutes": 4},
		{"title": "Forsaken Cowboy", "artist": ["Royksopp"], "album:": "Senior", "duration in minutes": 5.2}
	]
}


total_duration = playlist1["songs"][0]["duration in minutes"] + playlist1["songs"][1]["duration in minutes"]
print(total_duration)