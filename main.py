from datetime import datetime
from GLMClient import GLMClient
from config import config
from jinja2 import Template
from mailer import send_mail

print('请输入邮件相关内容，例如 "GPT 教学"。输入 "s" 结束输入，并开始发送邮件。')

relative = []
while True:
    words = input('内容: ').strip()
    if words == 's':
        break
    relative.append(words)



ai_config = config['ai']
mail_template = config['template']

client = GLMClient(**ai_config)

template = Template(
    'jinja 模板为:\n\n'
    '{{template}}'
    '\n\n'
    '生成内容与以下内容相关:\n'
    '{{relative}}'
)

prompt = template.render(template=mail_template, relative='\n'.join(relative))
print(prompt)

response = ''
for chunk in client.stream(prompt):
    response += chunk
    print(chunk, end='')

code = response.split('```python')[1].split('```')[0]

jinja_param = eval(code)
print(jinja_param)

template = Template(mail_template)
content = template.render(**jinja_param)
print(content)

current_time = datetime.now()
dt = current_time.strftime(' %Y%m%d')

email_param = {**config['email']}
email_param['subject'] += dt
email_param['content'] = content + '\n\n' + config['sign']

print('邮件发送成功' if send_mail(**email_param) else '邮件发送失败')
