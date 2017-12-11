
# The action_executer process is responsible for getting the text input from the server, parse the input to extract the semantic meaning and perform the necessary action
# Author: ArvindRS
# Date: 04/07/2017

import traceback, pyttsx
import settings, command_executer


def speak(text):
	# The speak(text_to_speak) will speak the given text through the audio system using the pyttsx library (https://pyttsx.readthedocs.io/en/latest/)
	engine = pyttsx.init()
	engine.setProperty('voice','english-us')
	engine.setProperty('rate', 150)
	engine.say(text)
	engine.runAndWait()
	engine.stop()


def main(text):
	# Main function 


	# Call upon the SemanticExtractor to get the base text from the input text
	text = semantic_extractor.extract(text)

	# Check what is the requested action and perform it
	if "start app:" in text:
		application_name = settings.default_commands[text]
		command_executer.start_application(application_name,[])

	elif "time?" in text:
		current_time = command_executer.get_current_time()
		print current_time
		text = "The time is "+str(current_time)
		speak(text)
	


if __name__ == '__main__':
	text = "foo"
	main(text)
