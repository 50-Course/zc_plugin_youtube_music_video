from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from music.utils.data_access import read_data, write_data

from music.serializers import MediaSerializer
from cent import Client, CentException
from django.confs import settings

class SidebarView(APIView):

    def get(self, request, *args, **kwargs):
        data = {

            "message": "Plugin Sidebar Retrieved",
            "data": {
                "type": "Plugin Sidebar",
                "name": "Music Plugin",
                "description": "Shows Music items",
                "plugin_id": "61360ab5e2358b02686503ad",
                "organisation_id": "6134fd770366b6816a0b75ed",
                "user_id": "6139170699bd9e223a37d91b",
                "group_name": "Music",
                "show_group": False,
                "public_rooms": {
                    "room_name": "music room",
                    "object_id": "613e906115fb2424261b6652",
                    "collection_name": "room",
                    "type": "public_rooms",
                    "unread": 2,
                    "members": 23,
                    "icon": "headphones",
                    "action": "open",
                },
                "joined_rooms": {
                    "title": "general",
                    "id": "DFGHH-EDDDDS-DFDDF",
                    "unread": 0,
                    "members": 100,
                    "icon": "shovel",
                    "action": "open",
                },
            },
            "success": "true"
        }
        return JsonResponse(data, safe=False)


class PluginInfoView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            "message": "Plugin Information Retrieved",
            "data": {
                "type": "Plugin Information",
                "plugin_info": {"name": "Music room",
                                "description": [
                                    "This is a plugin that allows individuals in an organization to add music and video links from YouTube to a  shared playlist. This allows anyone in that organization to listen to or watch any of the shared videos/songs. Users also have the option to chat with other users in the music room and the option to like a song or video that is in the music room library."]
                                },
                "version": "v1",
                "scaffold_structure": "Monolith",
                "team": "HNG 8.0/Team Music Plugin",
                "developer_name": "Zurichat Music Plugin",
                "developer_email": "musicplugin@zurichat.com",
                "icon_url": "https://drive.google.com/file/d/1KB9uSWqg0rM21ohsPxGnG8_1xbcdReio/view?usp=drivesdk",
                "photos": "https://drive.google.com/file/d/1KB9uSWqg0rM21ohsPxGnG8_1xbcdReio/view?usp=drivesdk",
                "homepage_url": "https://music.zuri.chat/",
                "sidebar_url": "https://music.zuri.chat/api/v1/sidebar/",
                "install_url": "https://music.zuri.chat/",
                'ping_url': 'http://music.zuri.chat/api/v1/ping'
            },
            "success": "true"
        }
        return JsonResponse(data, safe=False)


class PluginPingView(APIView):

    def get(self, request, *args, **kwargs):
        server = [
            {'status': 'Success',
             'Report': ['The music.zuri.chat server is working']}
        ]
        return JsonResponse({'server': server})


class MediaView(GenericAPIView):
    def get(self, request):
        payload = {"name": "hng.user01@gmail.com", "track_url": "password"}

        data = read_data('test_collection')
        # data = write_data('test_collection', object_id=id, payload=payload)
        data = data['data']

        return Response(data)

    def post(self, request):
        data = request.user
        return Response(data)


# class AddToRoomView(APIView):
#     def post(self, request):
#         data = {
#             "name": "kingsway"
#         }
#         return Response(data)


class Rtc(Client):
    req_url = "https://realtime.zuri.caht/api"
    req_token = settings.API_TOKEN
    def __init__(self, url, *args, **kwargs):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'apikey' + str(req_token)
            }
        self.url = req_url
        self.key = str(req_token)

    def publish(self, room, data):

        if settings.DEBUG != True:
            client = Client(url=self.req_url, self.req_token, timeout=15)
        else:
            client = Client(url="http://localhost:8000/api", api_key="", verify=False)

        
        payload = {
            "message-type": "0",
            "data": data
        }

        try:
            client.add("publish", payload)
        except CentException:
            pass