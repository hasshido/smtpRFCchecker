import socket

# SMTP server details
smtp_server = 'mightocho.com'
port = 25  # Default port for SMTP (non-SSL)

# Email details
sender_email = 'your_email@mightocho.com'
recipient_emails = [
    # Simple Internationalized Domain Names (IDN)
    'user@xn--exmple-cua.com',
    'admin@xn--bcher-kva.com',
    '用户@例子.广告',
    'δοκιμή@παράδειγμα.δοκιμή',
    'test@例子.测试',
    'admin@例子.广告',
    'user@sub.例子.网络',
    'usuario@ejemplo.com',
    'usuario@prueba.empresa',
    'χρήστης@παράδειγμα.δοκιμή',

    # Unicode in Local Parts
    'user@mydomain.com',
    '用户@mydomain.com',
    'χρήστης@mydomain.com',
    '使用者@域名.cn',
    'test@mydomain.cn',
    'имя@пример.рф',
    'имя@xn--d1acj3b.xn--p1ai',
    '簡體@電子郵件.cn',
    '測試@例子.tw',
    'χρήστης@subdomain.gr',

    # Emojis in Local Parts and Domains
    '🎉@example.com',
    '🎂🎈@birthday.example',
    '😀@emoji.email',
    '😍@love.email',
    'emoji🤖@robots.email',
    'smile😊@happy.example',
    'test@emoji.🎉',
    'mail@domain.😀',
    '😜@face.emoji',
    'emoji🎁@example.邮件',

    # Quoted Local Parts with Special Characters
    '"quoted.local.part"@example.com',
    '"this.is.very.unusual.@.unusual.com"@example.com',
    '"quoted@local"@example.com',
    '"space in local"@example.com',
    '"backslash\\in.local"@example.com',
    '"double\\"quote"@example.com',
    '"leading.quote"@example.com',
    '"dot.at.end."@example.com',
    '"quoted.dot."@example.com',
    '"emoji🤖quoted"@example.com',

    # Local Parts with Special Characters
    'abc.def@example.com',
    'test.email+alex@example.com',
    'test.email@example.com',
    'admin@mailserver1',
    'test@sub.domain.com',
    'user@[IPv6:2001:db8::1]',
    'local-part_with-symbols@example.com',
    'underscore_in@domain.com',
    'test@sub.domain.网络',
    'info@[IPv6:2001:db8:85a3::8a2e:370:7334]',

    # Internationalized Domain Names with UTF-8 Local Parts
    '使用者@例子.中国',
    'χρήστης@παράδειγμα.ελ',
    'utilisateur@exemple.فرنسا',
    'test@例子.公務',
    'тест@пример.рф',
    '使用者@例子.公司',
    'test@例子.组織機構',
    '用户@例子.电子邮件',
    'пользователь@пример.рус',
    'مثال@مثال.مصر',

    # Local Parts with Dashes and Special Characters
    'user-name@example.com',
    'user+mailbox/department=shipping@example.com',
    'customer/department=shipping@example.com',
    "!$%&'*+-/=?^_`{|}~@example.org",
    'user%example.com@example.org',
    "!#$%&'*+/=?^_`{}|~@example.org",
    'john..doe@example.com',
    'mail--box@domain.com',
    'user@local-name.com',
    'john.smith@domain.local',

    # Numeric Local Parts and Domains
    '1234567890@example.com',
    'local123@domain123.com',
    '12345678@number.com',
    'user@numbers1234.com',
    '987654@domain567.com',
    'user@domain-with-123.com',
    '1234@myemail.数字',
    '654321@numeros.com',
    'num123@sub.num.com',
    'test@123.example',

    # IPv6 Addresses in Domains
    'user@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]',
    'admin@[IPv6:1234:5678:9abc:def0:1234:5678:9abc]',
    'info@[IPv6:2001:db8::ff00:42:8329]',
    'test@[IPv6:abcd:ef01:2345:6789:abcd:ef01:2345]',
    'user@[IPv6:0:0:0:0:0:0:0:1]',
    'mailbox@[IPv6::1]',
    'test@[IPv6:2001:db8:0:1:0:0:1:1]',
    'ipuser@[IPv6:2607:f8b0:4005:0800:0000:0000:0000:200e]',
    'address@[IPv6:2404:6800:4003:c01::65]',
    'ipv6mail@[IPv6:3ffe:1900:4545:3:200:f8ff:fe21:67cf]',

    # ASCII Special Characters and Edge Cases
    'abc@example.com',
    'test@sub-domain.example.com',
    'test@sub_domain.example.com',
    'customer/department=shipping@example.org',
    "!#$%&'*+-/=?^_`{|}~@example.org",
    'john.doe@domain-with-hyphens.com',
    'user@company-name.com',
    '"user"@example.com',
    'user@sub-domain-with-dash.com',
    'dotted.name@example.com',

    # Multi-Domain Emails and Edge Cases
    'john.doe@first.last.example.com',
    'user@sub.subdomain.example.com',
    'local@domain-with-many.parts.example',
    'mail@sub.domain.within.domain.com',
    'test@deep.nested.subdomain.example.com',
    'user@multiple.domains.in.address.com',
    'final@deeply.nested.sub.subdomain.com',
    'first.last@sub.subsub.example.com',
    'longlocal@very-long.sub-domain.example.com',
    'multi@deep.subdomain.example',

    # Long Local Parts and Domains
    'this.is.a.very.long.localpart@example.com',
    'longlocalpart.with.many.parts@example.com',
    'long.local-part@deep.sub.domain.example.com',
    'longpart.with.many.dots@example.com',
    'verylongemailaddress@domain.com',
    'long-local-part@long.sub.domain.example',
    'test@very.very.long.domain.name.example',
    'long-email@deep.sub-domain.example.com',
    'user@really.long.tld',
    'admin@veryverylong.domain.with.many.parts',

    # Email Addresses with Extended Unicode Characters
    '例子@例子.公司',
    'δοκιμή@παράδειγμα.δοκιμή',
    '用户@电子邮件.cn',
    '使用者@例子.中国',
    'пример@пример.рф',
    '测试@例子.中国',
    'имя@пример.рус',
    'имя@пример.москва',
    '使用者@例子.公司',
    'test@例子.互联网',

    # Local Parts with Mixed Unicode and ASCII
    'user用户@example.com',
    'χρήστηςuser@example.com',
    'اسم@user.example.com',
    'примерuser@domain.рф',
    'ejemplo用户@domain.com',
    'test用户@domain.com',
    'usuario用户名@dominio.com',
    '测试test@domain.com',
    'testПример@пример.рф',
    'اسمuser@domain.com',

    # Emojis and Symbols in Domain Names
    'email@📧.example',
    'mail@🍕.pizza',
    'hello@🎉.celebration',
    'admin@🏠.home',
    'contact@🐶.dog',
    'user@🐱.cat',
    'test@💡.ideas',
    'info@🍎.apple',
    'hello@🎵.music',
    'support@📱.mobile',

    # Edge Cases with Email Length
    'verylongemailaddress@domain.com',
    'very.long.email.address@very.long.domain.com',
    'longlocalpart.with.many.parts@deep.domain.com',
    'long.local.part@very.long.domain.name.example.com',
    'even.longer.email.address@sub.domain.with.many.parts.example.com',
    'local@sub.sub.sub.sub.domain.example',
    'mail@deep.deep.deep.deep.subdomain.example',
    'deepdeepdeepdeep@subdomain.example.com',
    'longlocal@deeply.nested.sub.sub.domain.example.com',
    'user@long.long.long.long.subdomain.example.com',

    # Random Mix of All Cases
    'hello@例子'
]
subject = 'Test Email with RFC 6531 Addresses'
message_body = 'This is a test email sent from Python using RFC 6531 compliant addresses.'

# Function to send raw SMTP commands via socket
def send_email_via_socket(sender, recipient, subject, body):
    try:
        # Create a socket connection to the SMTP server
        smtp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        smtp_socket.connect((smtp_server, port))

        # Receive the initial server greeting (e.g., "220 ...")
        response = smtp_socket.recv(1024).decode('utf-8')

        # Send EHLO command
        smtp_socket.send(b"EHLO mightocho.com\r\n")
        response = smtp_socket.recv(1024).decode('utf-8')

        # Send MAIL FROM command
        smtp_socket.send(f"MAIL FROM:<{sender}>\r\n".encode('utf-8'))
        response = smtp_socket.recv(1024).decode('utf-8')

        # Send RCPT TO command
        smtp_socket.send(f"RCPT TO:<{recipient}>\r\n".encode('utf-8'))
        response = smtp_socket.recv(1024).decode('utf-8')

        # Send DATA command
        smtp_socket.send(b"DATA\r\n")
        response = smtp_socket.recv(1024).decode('utf-8')

        # Send the email headers and body
        headers = f"From: {sender}\r\nTo: {recipient}\r\nSubject: {subject}\r\n\r\n"
        message = headers + body + "\r\n.\r\n"
        smtp_socket.send(message.encode('utf-8'))

        # Receive the final server response
        response = smtp_socket.recv(1024).decode('utf-8')
 
        if "250" in response:
            # 250 response means success
            print(f"Email accepted for recipient: {recipient}")
        else:
            # Any other response means failure
            print(f"Email rejected for recipient: {recipient}")

        # Send QUIT command
        smtp_socket.send(b"QUIT\r\n")
        response = smtp_socket.recv(1024).decode('utf-8')

        # Close the socket connection
        smtp_socket.close()

    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

# Loop through each recipient and send an email
for recipient in recipient_emails:
    send_email_via_socket(sender_email, recipient, subject, message_body)
