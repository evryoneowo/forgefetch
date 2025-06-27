def richdata(data, indent, accent, secondary, reset):
    if not data: return

    txt = ''
    for i, key in enumerate(data):
        txt += secondary
        if i == 0:
            txt += '┌ '
        elif i < len(data) - 1:
            txt += '├ '
        else:
            txt += '└ '
            txt += f'{secondary}{key}:{reset}\n'

            if str(data[key]).split('\n'):
                for datak in str(data[key]).split('\n'):
                    txt += f'{accent} {indent*' '}{datak}{reset}\n'
            else:
                txt += f'{accent} {indent*' '}{str(data[key])}{reset}\n'
            
            continue
            
        txt += f'{secondary}{key}:{reset}\n'

        if str(data[key]).split('\n'):
                for datak in str(data[key]).split('\n'):
                    txt += f'{secondary}│{indent*' '}{accent}{datak}{reset}\n'
        else:
            txt += f'{secondary}│{indent*' '}{accent}{str(data[key])}{reset}\n'

        txt += f'{secondary}│{reset}\n'
    
    return txt