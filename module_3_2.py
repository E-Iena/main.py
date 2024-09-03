def send_email(sender='university.help@gmail.com', recipient=[], message=[]):
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    else:
        y = True
        for i in range(1, (len(recipient) - 3)):
            if recipient[i] == '@':
                y = True
                if recipient[-4:] == '.com' or recipient[-3:] == '.ru' or recipient[-4:] == '.net':
                    if sender == 'university.help@gmail.com':
                        print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
                        break
                    else:
                        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)
                        break
                else:
                    print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
                    break
            else:
                y = False
                continue
        if y == False:
            print('Нет знака @. Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)


print('1 вариант')
send_email(recipient='university.help@gmail.com', message='текст письма')
print('2 вариант')
send_email(recipient='univ@mail.net', message='текст письма')
print('3 вариант')
send_email(recipient='univ@mail.ya', message='текст письма')
print('4 вариант')
send_email(sender='university@gmail.com', recipient='adres@gmail.ru', message='текст письма')
print('5 вариант')
send_email(recipient='un_mail.com', message='текст письма')
