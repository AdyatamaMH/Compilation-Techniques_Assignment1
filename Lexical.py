import re

# Token
token_patterns = [
    ('invalid_id', r'\d+[a-zA-Z_]+[a-zA-Z0-9_]*'),  
    ('invalid_number', r'\d*\.\d*\.\d*|\d*\.\.\d*|\.\d+\.'), 
    ('number', r'\d+(\.\d+)?'),                 
    ('id', r'[a-zA-Z_][a-zA-Z0-9_]*'),          
    ('assign', r':='),                          
    ('plus', r'\+'),                            
    ('minus', r'-'),                            
    ('times', r'\*'),                           
    ('div', r'/'),                              
    ('lparen', r'\('),                          
    ('rparen', r'\)'),                          
    ('whitespace', r'[ \t]+'),                  
    ('newline', r'\n'),                         
    ('unknown', r'[^a-zA-Z0-9_ \t\n:=+\-*/()]+'),  
]

# Regex
token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
token_re = re.compile(token_re)

# Scanner
def scanner(input_code):
    line_num = 1
    col_num = 1
    for match in token_re.finditer(input_code):
        token_type = match.lastgroup
        token_value = match.group()
        
        if token_type == 'whitespace' or token_type == 'newline':
            if token_type == 'newline':
                line_num += 1
                col_num = 1
            else:
                col_num += len(token_value)
            continue

        if token_type == 'invalid_id':
            print(f"Error: Line {line_num}, Column {col_num}: invalid id '{token_value}'")
        elif token_type == 'invalid_number':
            print(f"Error: Line {line_num}, Column {col_num}: invalid number '{token_value}'")
        elif token_type == 'unknown':
            print(f"Error: Line {line_num}, Column {col_num}: unknown token '{token_value}'")
        else:
            print(f"Token: {token_type}, Value: '{token_value}', Line: {line_num}, Column: {col_num}")

        col_num += len(token_value)

# Input
input_code = """
3Celsius := 100.0
Fahrenheit$ := (9../5)*Celsius+%32
"""

scanner(input_code)
