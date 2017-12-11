
# Serializer file for specifying how to serialize the data
# Author: ArvindRS
# Date: 04/07/2017

from rest_framework import serializers

class HelloSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		fields = ('name','text')

