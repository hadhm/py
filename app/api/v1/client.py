from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, ClientEmailForm
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AddSuccess
from app.models.user import User

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
  form = ClientForm().validate_for_api()
  promise = {ClientTypeEnum.USER_EMAIL: __register_by_email}
  #
  promise[form.client_type.data]()
  return AddSuccess()


def __register_by_email():
  form = ClientEmailForm().validate_for_api()
  User.register_by_email(form.nickname.data, form.account.data,
                         form.secret.data)
