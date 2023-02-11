chap_loc = '''Isaiah 31:'''
import pyperclip,unidecode
clipb_paste = '''{d}'''.format(d = pyperclip.paste())
rdy_wk = unidecode.unidecode(clipb_paste)
punct_n = '''~`!@#$%^&*()_'"?[]{}\|-+=<>,./:;'''
no_punct = ''''''
for char in rdy_wk:
    if char not in punct_n:
        no_punct = no_punct + char
list_loc = no_punct.split('\n')
for j in range(0,len(list_loc),2):
    list_loc[j] = chap_loc + list_loc[j]
t_print = '\n'.join(list_loc)
pyperclip.copy(t_print)
print('Manipulated text successfully copied to clipboard')
