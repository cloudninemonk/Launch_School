# 5. Contains Character

"""

Write code that checks whether the string char_sequence contains the character x.

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

"""

# My response:

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

char_sequence.find('x') # 26
'x' in char_sequence # True

# Extra coding:

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMux'

char_sequence.rfind('x') # 40
