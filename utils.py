from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('4D3749416A494A4C30624852474E4645743778316973764D61585755335A7A4D595158616B427A2B3778493D')
        params = {
            'sender': "2000660110",
            'receptor': phone_number,
            'message': f'{code}کد تایید شما:'
        }
        response = api.sms_send(params)
        print(response)

    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)


class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin