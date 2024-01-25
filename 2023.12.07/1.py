email = input('Введите email: ')

if email.count('@') == 1 \
      and email[0] != '@' \
      and email.count('.') > 0 \
      and email.find('.') > email.find('@'):
            print('Да')
else:
      print('Нет')

# Введите email: BOCEMb@mail.ru
# Да

# Введите email: 3xd@mail
# Нет