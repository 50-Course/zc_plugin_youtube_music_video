from rest_framework import serializers


class MediaSerializer(serializers.Serializer):
    media_id = serializers.CharField()
    name = serializers.CharField()
    url = serializers.CharField()

class RoomSerializer(serializers.Serializer):
    title = serializers.CharField()
    creator = serializers.CharField()
    url = serializers.URLField(blank=False, null=False)
    room_id = serializers.SerializerMethodField('_get_room_id')

    def _get_room_id(self, room):
        _id = requests.get("https://music.zuri.chat/api/v1/sidebar/").json()["object_id"]
        return str(_id)



    