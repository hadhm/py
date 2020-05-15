from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
  return 'i am book'


@api.route('/add')
def add_book():
  return 'i add book'
