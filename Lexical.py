import re


token_specification = [
    ('NUMBER',   r'\d+(\.\d+)?'),          
    ('ASSIGN',   r':='),                  
    ('PLUS',     r'\+'),                  
    ('MINUS',    r'-'),                    
    ('TIMES',    r'\*'),                  
    ('DIV',      r'/'),                    
    ('LPAREN',   r'\('),                  
    ('RPAREN',   r'\)'),                  
    ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
    ('INVALID_ID', r'\d+[A-Za-z_]+'),      
    ('COMMENT',  r'/\*(?:[^*]|\*(?!/))*\*/|//.*'),  
    ('NEWLINE',  r'\n'),                  
    ('SKIP',     r'[ \t]+'),              
    ('MISMATCH', r'.'),                    
]


token_re = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)


class Tokenizer:
    def __init__(self, code):
        self.code = code
        self.line = 1
        self.current_pos = 0


    def generate_tokens(self):
        for match in re.finditer(token_re, self.code):
            kind = match.lastgroup
            value = match.group(kind)
            column = match.start() - self.current_pos


            if kind == 'NEWLINE':
                self.line += 1
                self.current_pos = match.end()
            elif kind == 'SKIP' or kind == 'COMMENT':
                pass  
            elif kind == 'INVALID_ID':
                print(f'Line {self.line} Column {column}: invalid identifier {value}')
            elif kind == 'MISMATCH':
                print(f'Line {self.line} Column {column}: unknown token {value}')
            else:
                yield kind, value, self.line, column


def main():
    code = """
3Celsius := 100.0
Fahrenheit$ := (9../5)*Celsius+%32
"""


    scanner = Tokenizer(code)
   
    for token in scanner.generate_tokens():
        kind, value, line, column = token
        if kind in ('ID', 'NUMBER', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIV', 'LPAREN', 'RPAREN'):
            print(f'{kind}: {value}')
        else:
            print(f'Line {line} Column {column}: unknown token {value}')


if __name__ == '__main__':
    main()
