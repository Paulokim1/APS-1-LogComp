import re

class PrePro:
    def filter(source):
        source = re.sub(r'#.*\n', '\n', source) # remove comentários de uma linha
        source = re.sub(r'#.*', '', source) # remove comentários de uma linha
        source = re.sub(r'\n\s*\n', '\n', source) # remove linhas vazias
        source = source.strip()  # remove linhas vazias no início e final do texto
        return source