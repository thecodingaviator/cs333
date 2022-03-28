# Identifier -> Letter { Letter | Digit }
# Letter -> a ... z | A .. Z
# Digit -> 0 | ... | 9
# Literal -> Integer | Boolean 
# Boolean -> true | false

# List of literal values
# if, while, else, ==, !=, ...
# ";"		{ echo (); return new Token (TokenClass . SEMICOLON); }
# "{"		{ echo (); return new Token (TokenClass . LBRACE); }
# "}"		{ echo (); return new Token (TokenClass . RBRACE); }
# "("		{ echo (); return new Token (TokenClass . LPAREN); }
# ")"		{ echo (); return new Token (TokenClass . RPAREN); }
# "["		{ echo (); return new Token (TokenClass . LBRACK); }
# "]"		{ echo (); return new Token (TokenClass . RBRACK); }
# "="		{ echo (); return new Token (TokenClass . ASSIGN); }
# "||"		{ echo (); return new Token (TokenClass . OR); }
# "&&"		{ echo (); return new Token (TokenClass . AND); }
# "+"		{ echo (); return new Token (TokenClass . PLUS); }
# "-"		{ echo (); return new Token (TokenClass . MINUS); }
# "*"		{ echo (); return new Token (TokenClass . TIMES); }
# "/"		{ echo (); return new Token (TokenClass . SLASH); }
# "%"		{ echo (); return new Token (TokenClass . MOD); }
# "=="		{ echo (); return new Token (TokenClass . EQ); }
# "!="		{ echo (); return new Token (TokenClass . NE); }
# "<"		{ echo (); return new Token (TokenClass . LT); }
# "<="		{ echo (); return new Token (TokenClass . LE); }
# ">"		{ echo (); return new Token (TokenClass . GT); }
# ">="		{ echo (); return new Token (TokenClass . GE); }

# The value field will always be a string. This makes it easier for the parsing.s

class Token:
    def __init__( self, value ):
        self.value = value
        
    def isIdentifier( self ):
        return False

    def isBoolean( self ):
        return False
        
    def isInteger( self ):
        return False
        
    def __str__( self ):
        return str(self.value)
        
class IdentifierToken(Token):

    def isIdentifier( self ):
        return True
        
    def __str__( self ):
        return "id: " + str(self.value)

class BooleanToken(Token):
    def isBoolean( self ):
        return True

    def __str__( self ):
        return "bool: " + str(self.value)
        
class IntegerToken(Token):        
    def isInteger( self ):
        return True
    def __str__( self ):
        return "int: " + str(self.value)
        
class Tokenizer:

    def __init__( self, filename ):
        fobj = open( filename )
        self.lines = fobj.readlines()
        self.cur_line = 0
        self.cur_index = 0
        
    # Increment the line and column indices until they indicate the
    # beginning of a token.
    def passWhitespace(self):
        if self.cur_line == len(self.lines):
            return
        if self.cur_index == len(self.lines[self.cur_line]):
            self.cur_line += 1
            self.cur_index = 0
            self.passWhitespace()
            return
        foundIt = False
        # search this line for a non-whitespace character
        for self.cur_index in range(self.cur_index,len(self.lines[self.cur_line])):
            if self.lines[self.cur_line][self.cur_index] not in " \t\n\r":
                foundIt = True
                break
        # if we are still in whitespace, go on to the next line
        if self.cur_index == len(self.lines[self.cur_line])-1 and not foundIt:
            self.cur_line += 1
            self.cur_index = 0
            self.passWhitespace()
        # If we find a comment, then we need to skip the rest of the line
        # and go on to the next.
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+2] == '//':
            self.cur_line += 1
            self.cur_index = 0
            self.passWhitespace()
            
    def parseInt(self):
        """ advance the indices and return the int as an int"""
        b = self.cur_index
        for self.cur_index in range(b, len(self.lines[self.cur_line])):
            if self.lines[self.cur_line][self.cur_index] not in "0123456789":
                return IntegerToken( self.lines[self.cur_line][b:self.cur_index] )
        self.cur_line += 1
        self.cur_index = 0
        return IntegerToken( self.lines[self.cur_line-1][b:] )
    
    def parseIdentifier(self):
        b = self.cur_index
        for self.cur_index in range(b, len(self.lines[self.cur_line])):
            if self.lines[self.cur_line][self.cur_index] not in "0123456789qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm":
                return IdentifierToken( self.lines[self.cur_line][b:self.cur_index] )
        self.cur_line += 1
        self.cur_index = 0
        return IdentifierToken( self.lines[self.cur_line-1][b:] )

    def getToken(self):
        self.passWhitespace()
        if self.cur_line == len(self.lines):
            # We are at the end of the file. No more tokens
            return None
        cur_char  = self.lines[self.cur_line][self.cur_index]
        if cur_char in ";(){}+-/*%":
            self.cur_index += 1
            return Token( cur_char )
        elif cur_char == '=':
            if self.lines[self.cur_line][self.cur_index:self.cur_index+2] == '==':
                self.cur_index += 2
                return Token( "==" )
            else:
                self.cur_index += 1
                return Token( "=" )
        elif cur_char == '<':
            if self.lines[self.cur_line][self.cur_index:self.cur_index+2] == '<=':
                self.cur_index += 2
                return Token( "<=" )
            else:
                self.cur_index += 1
                return Token( "<" )
        elif cur_char == '>':
            if self.lines[self.cur_line][self.cur_index:self.cur_index+2] == '>=':
                self.cur_index += 2
                return Token( ">=" )
            else:
                self.cur_index += 1
                return Token( ">" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+2] == '!=':
            self.cur_index += 2
            return Token( "!=" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+2] == '||':
            self.cur_index += 2
            return Token(  "||" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+2] == '&&':
            self.cur_index += 2
            return Token( "&&" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+2] == 'if':
            self.cur_index += 2
            return Token( "if" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+5] == 'while':
            self.cur_index += 5
            return Token( "while" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+3] == 'for':
            self.cur_index += 3
            return Token( "for" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+4] == 'else':
            self.cur_index += 4
            return Token( "else" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+4] == 'true':
            self.cur_index += 4
            return BooleanToken( "true" )
        elif self.lines[self.cur_line][self.cur_index:self.cur_index+5] == 'false':
            self.cur_index += 5
            return BooleanToken( "false" )
        elif cur_char in "0123456789":
            return self.parseInt()
        else:
            return self.parseIdentifier()
        
if __name__ == '__main__':
    t = Tokenizer( 'test.c')
    while True:
        tok = t.getToken()
        if tok is None:
            break
        print tok