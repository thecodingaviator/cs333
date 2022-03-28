# Stephanie Taylor
# Uses a concrete syntax to build an abstract syntax tree.
# Written in Python2. If you want to run with Python 3, then you will need to update the print statements.

# Concrete syntax 
# 
# Block -> { { Statement }} # where one pair of { is EBNF, and the other is literal
# Statement -> Block | Assignment | Conditional | While
# Assignment  -> Identifier = Expression ;
# Conditional -> if ( Expression ) Statement  else Statement 
# While -> while ( Expression ) Statement
# For -> for (Assignment Expression; Assignment) Statement
# Expression -> Conjunction { || Conjunction }
# Conjunction -> Equality { && Equality }
# Equality -> Relation [ EquOp Relation ]
# EquOp -> == | != 
# Relation -> Addition [ Relop Addition ]
# Relop -> < | <= | > | >=
# Addition -> Term { AddOp Term }
# AddOp -> + | -
# Term -> Primary { MulOp Primary }
# MulOp -> * | / | %
# Primary -> Identifier | Literal | ( Expression )

# Identifier -> Letter { Letter | Digit }
# Letter -> a ... z | A .. Z
# Digit -> 0 | ... | 9
# Literal -> Integer | Boolean 
# Boolean -> true | false


# Abstract syntax 
# 
# Statement = Assignment | Conditional | While
# Assignment = target (Identifier), source (Expression)
# Conditional = condition (Expression), thenBranch (Statement), elseBranch (Statement)
# While = test (Expression), body (Statement)
# For = initial (Statement), test (Expression), body (Statement), post (Statement)
# Expression = BinaryExpression | Identifier | Value | Relation
# BinaryExpression = string op (+,-,*,/), Expression left, Expression right
# Relation = string op (<,>,==,!=), Expression left, Expression right
# Conjunction = string op (AND,OR), Expression left, Expression right
# Identifier = string name
# Value = a literal integer
import tokenizer
import AST

# Whenever we enter a parseX function, we have already retrieved the first token in that statement.

class Parser:
    def __init__( self, filename ):
        self.tokenizer = tokenizer.Tokenizer( filename )
        self.ast = None
        self.token = None
        
    def getToken(self):
        self.token = self.tokenizer.getToken()
        #print "Getting Token: ", self.token
        
    def parsePrimary( self ):
        if self.token.isIdentifier():
            e =  AST.Identifier( self.token.value )
        elif self.token.isBoolean():
            e =  AST.Value( self.token.value.lower()=="true" )
        elif self.token.isInteger():
            e =  AST.Value( int(self.token.value) )
        else:
            if self.token.value != "(":
                print "expecting open paren", self.token
                return
            self.getToken() # move to first in Expression
            e = self.parseExpression()
            if self.token.value != ")":
                print "expecting close paren", self.token
                return
        self.getToken() # move to first after this expression
        return e
        
    def parseTerm( self ):
        c = self.parsePrimary()
        while self.token.value in "*/%":
            op = self.token.value
            self.getToken() # move into first token of next expression
            # and return a Tree that puts any other +/- operations we have already
            # seen in the left kid, so they are evaluated first.
            c = AST.BinaryExpression( c, op, self.parsePrimary() )
        return c       
        
    def parseAddition( self ):
        c = self.parseTerm()
        while self.token.value in "+-":
            op = self.token.value
            self.getToken() # move into first token of next expression
            # and return a Tree that puts any other +/- operations we have already
            # seen in the left kid, so they are evaluated first.
            c = AST.BinaryExpression( c, op, self.parseTerm() )
        return c       
    
    # Relation -> Addition [ Relop Addition ]
    # Relop -> < | <= | > | >=
    def parseRelation(self):
        c = self.parseAddition()
        if self.token.value == "<" or self.token.value == "<=" or self.token.value == ">" or self.token.value == ">=":
            op = self.token.value
            self.getToken()
            c = AST.Relation( c, op, self.parseAddition() )
        return c

    # Equality -> Relation [ EquOp Relation ]
    # EquOp -> == | != 
    def parseEquality( self ):
        c = self.parseRelation()
        if self.token.value == "==" or self.token.value == "!=":
            op = self.token.value
            self.getToken()
            c = AST.Conjunction( c, op, self.parseRelation() )
        return c

    # Conjunction -> Equality { && Equality }
    def parseConjunction(self):
        # For now, we skip the Relation and go straight to addition, which doesn't really make sense, but I want to test it!
        c = self.parseEquality()
        while self.token.value == "&&":
            op = self.token.value
            self.getToken() # move into first token of next expression
            # and return a Tree that puts any other +/- operations we have already
            # seen in the left kid, so they are evaluated first.
            c = AST.Conjunction( c, op, self.parseEquality() )
        return c
        
    def parseExpression(self):
        # this is a conjunction for now.
        c = self.parseConjunction()
        while self.token.value == "||":
            op = self.token.value
            self.getToken() # move into first token of next expression
            # and return a Tree that puts any other +/- operations we have already
            # seen in the left kid, so they are evaluated first.
            c = AST.Conjunction( c, op, self.parseConjunction() )
        return c
        
    # Conditional -> if ( Expression ) Statement  else Statement 
    def parseConditional( self ):
        # the current token must have been if if this was called
        self.getToken()
        if self.token.value != "(":
            print "If statement expecting open paren", self.token
            return
        self.getToken() # move to first token in expression
        cond = self.parseExpression()
        if self.token.value != ")":
            print "If statement expecting close paren", self.token
            return
        self.getToken()
        then = self.parseStatement()
        self.getToken()
        if self.token.value != "else":
            print "If statement expecting else", self.token
            return
        self.getToken()
        elsebranch = self.parseStatement()
        return AST.Condition( cond, then, elsebranch )
        
    # While -> while ( Expression ) Statement
    def parseWhile( self ):
        # the current token must have been while if this was called
        self.getToken()
        if self.token.value != "(":
            print "While loop expecting open paren", self.token
            return
        self.getToken() # move to first token in expression
        test = self.parseExpression()
        if self.token.value != ")":
            print "While loop expecting close paren", self.token
            return
        self.getToken() # move past ) to first token of statement.
        body = self.parseStatement()
        return AST.While( test, body )
        
    def parseFor( self ):
        print "parsing for"
        # the current token must have been for if this was called
        # For -> for (Assignment Expression; Assignment) Statement
        self.getToken()
        if self.token.value != "(":
            print "For loop expecting open paren", self.token
            return
        self.getToken() # move to first token in Assignment
        init = self.parseAssignment()
        test = self.parseExpression()
        if self.token.value != ";":
            print "For loop expecting semicolon after condition", self.token
        self.getToken() # move to first token in Assignment
        update = self.parseAssignment()
        if self.token.value != ")":
            print "Foor loop expecting close paren", self.token
            return
        self.getToken() # move past ) to first token of statement.
        body = self.parseStatement()
        return AST.For( init, test, update, body )
        
    def parseAssignment( self ):
        # the current token must have been an identifier
        if not self.token.isIdentifier():
            print "Expecting identifier on LHS of assignment statement", self.token
            return
        var = AST.Identifier( self.token.value )
        self.getToken()
        if not self.token.value == "=":
            print "Expecting = in assignment", self.token
            return
        self.getToken() # get the first token of the expression
        expr = self.parseExpression()
        if self.token.value != ";":
            print "Expecting semicolon", self.token
            return
        self.getToken() # move to the next
        return AST.Assignment( var, expr )
        
    def parseBlock( self ):
        # The current token must have been { or we wouldn't be here
        s = []
        self.getToken() # Get the first token in the first statement
        while (self.token.value != "}"):
            s.append( self.parseStatement() )
            
        return AST.Block(s)
        
    def parseStatement( self ):
        if self.token.value == "if":
            return self.parseConditional()
        elif self.token.value == "while":
            return self.parseWhile()
        elif self.token.value == "for":
            return self.parseFor()
        elif self.token.value == "{":
            return self.parseBlock()
        else:
            return self.parseAssignment()
        
    def buildTree( self ):
        self.getToken()
        self.ast = self.parseStatement()

if __name__ == "__main__":
    p = Parser( "test.c" )
    p.buildTree()
    p.ast.printTree( "" )