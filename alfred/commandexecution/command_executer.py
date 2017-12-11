#!/usr/bin/python

# This is a prototype for the CommandExecution component of the Alfred personal assistant
# Author: ArvindRS
# Date: 04/07/2017

import time, datetime, os, subprocess, fnmatch
import settings

def get_current_time():
	# Function to get the current time in the format: HH:MM (24-hours)
	# TODO: Get time in format: HH:MM (AM/PM)

	current_time = datetime.datetime.now().time().strftime('%H:%M')
	
	return current_time

def get_current_date():
	# Function to get the current date
	# TODO: Return date in a more user friendly format

	current_date = datetime.datetime.now().date().strftime('%dth of %m')

	return current_date

def start_application(application, options):
	# Function to start an application by linux command execution through the shell
	# TODO: Add support for specific filenames

	command = [application] + options
	print command

	# Using subprocess.Popen().pid to execute the command in the background
	pid = subprocess.Popen(command,cwd=settings.default_execution_path,stdout=subprocess.PIPE,stderr=subprocess.PIPE).pid
	print pid
	

def main():
	# Main function


	# Command to start VLC application
	application = "vlc"
	filename = ""
	options = []
	options += [filename]

	# Command to start the text editor
	#application = "gedit"
	#options = []

	start_application(application,options)


if __name__ == '__main__':
	main()
