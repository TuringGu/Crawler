import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''

# re.S: Match the /n modifier
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)

print(result.group(1))
