from re import T


print('HelloWorld')

personal_info = {
    'name':'酒井潤',
    'live_in': 'サンフランシスコ',
    'python_experience_years':10,
    'occupation':'ソフトウェアエンジニア'
}

for key,value in personal_info.items():
    print(key,':',value)

is_code_style_good = True

f=False
if not f:
    print('You are fired')