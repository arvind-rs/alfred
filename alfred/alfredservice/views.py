# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .serializers import HelloSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import multiprocessing
from commandexecution import action_executer

'''
Sample Input:
{
"name":"arvind",
"text":"hello"
}
'''

@api_view(['POST'])
def submit_message(request):

	print request.data

	input_text = ""
	for key in request.data:
		print request.data[key]
		if key == "text":
			input_text = request.data[key]

	if input_text != "":
		process = start_process(input_text)

	return Response(status=200)



def start_process(input_text):
	# The start_process() will spawn a new action_executer process for each input text

	process = multiprocessing.Process(target=action_executer.main,args=(input_text,))

	process.start()
	
	return process  
