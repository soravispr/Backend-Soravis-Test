from rest_framework import serializers
from apis.models import StudentSubjectsScore, Classes, Schools, Personnel, Subjects, SchoolStructure


class StudentSubjectsScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubjectsScore
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'

class SchoolStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolStructure
        fields = '__all__'