def send_email(sender='university.help@gmail.com',recipient=[],message=[]):
    if sender==recipient:
        print('Нельзя отправить письмо самому себе!')
    else:
        y='True'
        for i in range(1,(len(recipient)-3)):
            if recipient[i]=='@':
                y='True'
                if recipient[-4:]=='.com' or recipient[-3:]=='.ru' or recipient[-4:]=='.net':
                    if sender=='university.help@gmail.com':
                        print('Письмо успешно отправлено с адреса ',sender,' на адрес ',recipient)
                    else:
                        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ',sender,' на адрес ',recipient)
                else:
                    print('Невозможно отправить письмо с адреса ',sender,' на адрес ',recipient)
            else:
                y='False'
                continue
        if y==False:
            print('2 Невозможно отправить письмо с адреса ',sender,' на адрес ',recipient)
            
send_email(recipient='university.help@gmail.com',message='письмо текст')
send_email(recipient='univ@mail.net',message='письмо текст')
send_email(recipient='univ@mail.ya',message='письмо текст')
send_email(sender='university@gmail.com',recipient='adres@gmail.ru',message='письмо текст')

send_email(recipient='unmail.com',message='письмо текст')
