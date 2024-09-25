import json

college = {
	"college": "Engineering College",
	"objectives": "Mastering Electrical and Computer Engineering",
	"departments": {
		"dep1": "Electrical",
		"dep2": "Computer"
	},
	"years": ["year 1", "year 2", "year 3", "year 4"],
	"numbers": [1, 2, 3, 4],
	"ID": [10, 20, 30, 40]
}
json.dump(college, open("college.json", "w"))
reading_json = json.load(open("college.json", "r"))
print(reading_json)
