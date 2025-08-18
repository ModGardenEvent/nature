import json

import requests


def ballotbox_options():
	repo_root = common.get_repo_root()
	constants_file = repo_root / "constants.jsonc"
	constants = common.jsonc_at_home(common.read_file(constants_file))

	event_id = constants["event"]
	options = []
	submissions_url = f"https://api.modgarden.net/v1/event/{event_id}/submissions"
	print(submissions_url)
	for submission in json.loads(requests.get(submissions_url).text):
		option = {
			"id": submission["id"],
			"mod_id": submission["project"]["slug"],
			"name": submission["name"],
			# "description": submission["description"],
			# "platform": {
			# 	"type": submission["platform"]["type"]
			# }
			"project": {}
		}
		if "modrinth_id" in submission["project"]:
			option["project"]["modrinth_id"] = submission["project"]["modrinth_id"]
		# if "homepage_url" in submission["platform"]:
			# option["platform"]["homepage_url"] = submission["platform"]["homepage_url"]
		options.append(option)

	print(f"Writing {len(options)} submissions to options.json")
	with open(f"../pack/resources/datapack/required/mf_ballotbox/data/ballotbox/ballot/options.json", 'w', encoding="utf8") as out_file:
		json.dump(options, out_file, indent='\t')
	print("done!")


if __name__ == "__main__":
	ballotbox_options()
