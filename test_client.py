
# A thin python client to test the REST API
# Author: ArvindRS
# Date: 04/08/2017

import requests, traceback

def main():
	# Main function

	link = "http://localhost:8888/submit/"

	input_text = ""
	try:
		print "You are now talking with Alfred!"
		while 1:
			
			input_text = raw_input(">> ")
			data["text"] = input_text
			
			response = requests.post(link,json=data)

			print response.status_code, response.reason

			if input_text == "exit":
				print "Goodbye, Master!"
				break		
	except Exception, e:
		print e
		print traceback.format_exc()

if __name__ == '__main__':
	main()
