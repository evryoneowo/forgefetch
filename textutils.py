# text utils

import re

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def visible_length(s):
    return len(ansi_escape.sub('', s))

def connecttext(text1, text2, indent):
    length = max(map(visible_length, text1.split('\n')))

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def visible_length(s):
    return len(ansi_escape.sub('', s))

def connecttext(text1, text2, indent):
    length = max(map(visible_length, text1.split('\n')))
    txt = ''
    if len(text1.split('\n')) > len(text2.split('\n')):
        for i, line in enumerate(text1.split('\n')):
            if i >= len(text2.split('\n')):
                txt += line + '\n'
            
            else:
                txt += line + text2.split('\n')[i] + (length-visible_length(text1.split('\n')[i]))*' ' + indent*' ' + '\n'
    else:
        for i, line in enumerate(text2.split('\n')):
            if i >= len(text1.split('\n')):
                txt += length*' ' + indent*' ' + line + '\n'
            
            else:
                txt += text1.split('\n')[i] + (length-visible_length(text1.split('\n')[i]))*' ' + indent*' ' + line + '\n'
        
        else:
            txt += text1.split('\n')[i] + (length-visible_length(text1.split('\n')[i]))*' ' + indent*' ' + line + '\n'
    
    return txt
