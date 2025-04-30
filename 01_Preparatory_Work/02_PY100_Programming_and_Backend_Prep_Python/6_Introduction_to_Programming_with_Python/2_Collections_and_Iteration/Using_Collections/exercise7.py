# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'


# My response:

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
my_list = info.split(':')                           # ['xyz', '*', '42', '42', 'Lee Kim', '/home/xyz', '/bin/zsh']
info_new = '+'.join(my_list)                        # 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'   

info_new = info.replace(':', '+')                   # 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh' 


# Launch School's answer:

info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)
# 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(':', '+')
print(result)
# 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'