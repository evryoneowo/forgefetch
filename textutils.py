# text utils

def connecttext(text1, text2, indent):
    length = max(map(len, text1.split('\n')))

    txt = ''
    for i, line in enumerate(text2.split('\n')):
        if i >= len(text1.split('\n')):
            txt += length*' ' + indent*' ' + line + '\n'
        
        else:
            txt += text1.split('\n')[i] + (length-len(text1.split('\n')[i]))*' ' + indent*' ' + line + '\n'
    
    return txt