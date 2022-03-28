# Stephanie Taylor
# Defines a set of Classes for nodes in the Abstract Syntax Tree (AST)
# Written in Python2. If you want to run with Python 3, then you will need to update the print statements.

# For a language with dynamic typing, no side effects, and only one scope
# First set of classes are AST nodes

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

class Pass:
	def printTree( self, spaces ):
	    print spaces + "Pass"

class Assignment:
    def __init__( self, target, source ):
        self.target = target
        self.source = source
        
    def printTree( self, spaces ):
        print spaces + "Assignment"
        self.target.printTree( spaces + "  " )
        self.source.printTree( spaces + "  " )
        
class Condition:
    def __init__( self, condition, thenbranch, elsebranch ):
        self.condition = condition
        self.thenbranch = thenbranch
        self.elsebranch = elsebranch
        
    def printTree( self, spaces ):
        print spaces + "Condition"
        self.condition.printTree( spaces + "  " ) 
        self.thenbranch.printTree( spaces + "  " ) 
        self.elsebranch.printTree( spaces + "  " ) 

class Block:
	def __init__( self, statements ):
		self.statements = statements	
		
	def printTree( self, spaces ):
	    print spaces + "Block"
	    for s in self.statements:
	        s.printTree( spaces + "  " )
        
class BinaryExpression:
    def __init__( self, left, operator, right ):
        self.left = left
        self.operator = operator
        self.right = right
        
    def printTree( self, spaces ):
        print spaces + "Binary Operation: " + self.operator
        self.left.printTree( spaces + "  " )
        self.right.printTree( spaces + "  " )

class Relation:
    def __init__( self, left, operator, right ):
        self.left = left
        self.operator = operator
        self.right = right
        
    def printTree( self, spaces ):
        print spaces + "Relation: " + self.operator
        self.left.printTree( spaces + "  " )
        self.right.printTree( spaces + "  " )

class Conjunction:
    def __init__( self, left, operator, right ):
        self.left = left
        self.operator = operator
        self.right = right
        
    def printTree( self, spaces ):
        print spaces + "Conjunction: " + self.operator
        self.left.printTree( spaces + "  " )
        self.right.printTree( spaces + "  " )

class Identifier:
    def __init__( self, name ):
        self.name = name
        
    def printTree( self, spaces ):
        print spaces + "Id: " + self.name
        
class Value:
    def __init__( self, value ):
        self.value = value # should be a boolean or integer
        
    def printTree( self, spaces ):
        if self.value is True or self.value is False:
            print spaces + "Bool: " + str(self.value)
        else:
            print spaces + "Int: " + str(self.value)

    def __str__( self ):
        return str(self.value)
                                
class While:
    def __init__( self, test, body ):
        self.test = test
        self.body = body
        
    def printTree( self, spaces ):
        print spaces + "While Loop "
        self.test.printTree( spaces + "  " )
        self.body.printTree( spaces + "  " )
        
class For:
    # For = init (Assignment), test (Expression), update (Assignment), body (Statement)
    def __init__( self, initial, test, post, body ):
        self.initial = initial
        self.test = test
        self.post = post
        self.body = body
        
    def printTree( self, spaces ):
        print spaces + "For Loop "
        self.initial.printTree( spaces + "  " )
        self.test.printTree( spaces + "  " )
        self.post.printTree( spaces + "  " )
        self.body.printTree( spaces + "  " )
        
