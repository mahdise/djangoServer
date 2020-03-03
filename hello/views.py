from django.shortcuts import render
from django.http import HttpResponse
from ipware import get_client_ip
from rest_framework.response import Response

from rest_framework.views import APIView

# Create your views here.
def index(request):
    ip, is_routable = get_client_ip(request)

    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")



class responseAPI(APIView):
    '''
    {'user_input':'How are you'}

    '''

    def post(self, request):
        # s = request.session.session_key
        # if not s:
        #     s = request.session.create()
        # print(s)
        # ip, is_routable = get_client_ip(request)
        # active=False

        import pprint
        pprint.pprint(request.data)
        user_input = request.data.get("message")

        response_data = {
                "response_bot": {
                    "message": 'i am good'

                }
            }
        final_response = response_data
        reply_bot = final_response['response_bot']['message']
        with open("history.txt", "a") as fh:
            fh.write("{user}: {message}\nBot: {reply}\n".format(user='mahdi', message=user_input, reply=reply_bot))
        print(final_response)

        return Response(final_response)
