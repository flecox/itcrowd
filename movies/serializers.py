from rest_framework import serializers

from movies.models import Movie, Person


class PersonSerializer(serializers.ModelSerializer):
    directed = serializers.StringRelatedField(many=True, required=False)
    acted = serializers.StringRelatedField(many=True, required=False)
    produced = serializers.StringRelatedField(many=True, required=False)
    aliases = serializers.ListField(child=serializers.CharField(help_text='alias'), required=False)

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'aliases', 'directed', 'produced', 'acted')

    def create(self, validated_data):
        aliases = validated_data.pop('aliases')
        person = super(PersonSerializer, self).create(validated_data)
        for al in aliases:
            person.set_alias(al)
        return person

    def to_representation(self, instance):
        instance.aliases = instance.get_aliases()
        return super(PersonSerializer, self).to_representation(instance)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        person_fields = ('directors', 'actors', 'producers')
        fields = ('id', 'title', 'release_year') + person_fields

    def to_representation(self, instance):
        data = super(MovieSerializer, self).to_representation(instance)

        #Change the output of all person fields to return all the person's information:
        for field in self.Meta.person_fields:
            data[field] = PersonSerializer(getattr(instance, field).all(), many=True).data
        return data
