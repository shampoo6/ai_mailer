config = {
    'ai': {
        'assistant_id': '智谱的assistant_id',
        'api_key': '智谱的api_key',
        'api_secret': '对应api_key的api_secret'
    },
    'email_common': {
        'server': '邮箱服务器',
        'port': '邮箱服务器端口，默认为: 25',
    },
    'email': {
        'sender_name': '寄件人名字',
        'sender_email': '寄件邮箱',
        'password': '邮箱密码',
        'to': ['目标邮箱'],
        'subject': '邮件主题',
        'cc': ['抄送邮箱']
    },
    'template': '邮件内容模板，模板使用 jinja 模板，可以在其中填充变量，然后 pua ai，让 ai 来填充变量',
    'sign': '签名'
}
