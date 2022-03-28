# For a language with dynamic typing, no side effects, and only one scope
# Then the State class (a dictionary)
# Then the functions for the semantics.

# Abstract syntax 
# 
# Statement = Assignment | Conditional
# Assignment = target (Variable), source (Expression)
# Conditional = condition (Expression), thenBranch (Statement), elseBranch (Statement)
# While = test (Expression), body (Statement)
# For = init (Assignment), test (Expression), update (Assignment), body (Statement)
# Expression = BinaryExpression | Variable | Value | Relation
# BinaryExpression = string op (+,-,*,/), Expression left, Expression right
# Relation = string op (<,>,==,!=), Expression left, Expression right
# Conjunction = string op (&&,II), Expression left, Expression right
# Variable = string name
# Value = a literal integer

import AST # Where the nodes are
        
class State:
    # dictionary that stores string names of vars
    # and AST.Value objects
    def __init__( self ):
        self.state = {}
        
    def update( self, var, value ):
        self.state[var.name] = value
        
    def getValue( self, var ):
        return self.state[var.name]
        
    def __str__( self ):
        retstr = ''
        for name in self.state:
            retstr += name + ": " + str(self.state[name]) + '\n'
        return retstr[:-1]
        
# expr should be a BinaryExpression
# state should be a State
# returns a AST.Value
def M_BinaryExpression( expr, state ):
    if expr.operator == '+':
        val =  M_Expression( expr.left, state ).value + M_Expression( expr.right, state ).value
    elif expr.operator == '-':
        val =  M_Expression( expr.left, state ).value - M_Expression( expr.right, state ).value
    elif expr.operator == '*':
        val =  M_Expression( expr.left, state ).value * M_Expression( expr.right, state ).value
    elif expr.operator == '/':
        val =  M_Expression( expr.left, state ).value / M_Expression( expr.right, state ).value
    return AST.Value( val )

# expr should be a Relation
# state should be a State
# returns a AST.Value
def M_Relation( expr, state ):
    if expr.operator == '<':
        val =  M_Expression( expr.left, state ).value < M_Expression( expr.right, state ).value
    elif expr.operator == '>':
        val =  M_Expression( expr.left, state ).value > M_Expression( expr.right, state ).value
    elif expr.operator == '==':
        val =  M_Expression( expr.left, state ).value == M_Expression( expr.right, state ).value
    elif expr.operator == '!=':
        val =  M_Expression( expr.left, state ).value != M_Expression( expr.right, state ).value
    return AST.Value( val )

def M_Conjunction( expr, state ):
    # with short-circuiting
    if expr.operator == '&&':
        if M_Expression( expr.left, state ).value:
            return AST.Value( M_Expression( expr.right, state ).value )
        else:
            return AST.Value( False )
    if expr.operator == '||':
        if not M_Expression( expr.left, state ).value:
            return AST.Value( M_Expression( expr.right, state ).value )
        else:
            return AST.Value( True )

# expr should be an Expression
# state should be a State
# returns a AST.Value
def M_Expression( expr, state ):
    if isinstance( expr, AST.Relation ):
        return M_Relation( expr, state )
    elif isinstance( expr, AST.Conjunction ):
        return M_Conjunction( expr, state )
    elif isinstance( expr, AST.BinaryExpression ):
        return M_BinaryExpression( expr, state )
    elif isinstance( expr, AST.Identifier ):
        return state.getValue( expr )
    elif isinstance( expr, AST.Value ):
        return expr 
    else:
        print "error!", expr
        
def M_Statement( statement, state ):
    if isinstance( statement, AST.Assignment ):
        return M_Assignment( statement, state )
    elif isinstance( statement, AST.Condition ):
        return M_Condition( statement, state )
    elif isinstance( statement, AST.Block ):
        return M_Block( statement, state )
    elif isinstance( statement, AST.While ):
        return M_While( statement, state )
    elif isinstance( statement, AST.For ):
        return M_For( statement, state )
    elif isinstance( statement, AST.Pass ):
    	return state
    else:
        print "Unknown Statement Type"
        
# statement should be an Assignment
# state should be a State
# returns a State
def M_Assignment( statement, state ):
    state.update( statement.target, M_Expression( statement.source, state ) )
    return state
    	
def M_Block( block, state ):
    if (len(block.statements) == 0):
        return state
    return M_Block( AST.Block(block.statements[1:]), M_Statement( block.statements[0], state ) )
    
# Conditional = condition (Expression), thenBranch (Statement), elseBranch (Statement)
def M_Condition( c, state ):
    if M_Expression( c.condition, state ).value:
        return M_Statement( c.thenbranch, state )
    else:
        return M_Statement( c.elsebranch, state )

# expr should be a ForLoop
# state should be a State
# returns a State
def M_For( loop, state ):
    return M_ForLoopLooper( loop, M_Statement( loop.initial, state ) )

def M_ForLoopLooper( loop, state ):
    if not M_Expression( loop.test, state ).value:
        return state
    return M_ForLoopLooper( loop, M_Statement( loop.post, M_Statement( loop.body, state ) ) )

def M_While( loop, state ):
    if not M_Expression( loop.test, state ).value:
        return state
    return M_While( loop, M_Statement( loop.body, state ) )

# These are test functions that allow you to construct the tree directly and then test 
# evaluation of the tree.	SRT is leaving them here, but this isn't the primary method
# we will use for testing.
def main1():
    # a = 3 + 5
    expr = AST.BinaryExpression( AST.Value(3), "+", AST.Value(5) )
    stmnt = AST.Assignment( AST.Identifier("a"), expr )
    state = State()
    #state.update( Variable("a"), AST.Value(1) )
    state = M_Assignment( stmnt, state )
    print( state )

def main2():
    # b = (6-2)+4
    expr = AST.BinaryExpression( AST.BinaryExpression(AST.Value(6),"-",AST.Value(2)), "+", AST.Value(4) )
    stmnt = AST.Assignment( AST.Identifier("b"), expr )
    state = State()
    state = M_Assignment( stmnt, state )
    print( state )
    
def main3():
	# if (3 < 5) {
	# 	b = 5;
	# }
	# else {
	#	c = 10;
	# }
    test = AST.Relation( AST.Value(3),"<",Value(5) )
    stmnt1 = AST.Assignment( Variable("b"), AST.Value(5) )
    stmnt2 = AST.Assignment( Variable("c"), AST.Value(10) )
    cond = AST.Condition( test, stmnt1, stmnt2 )
    state = State()
    state = M_Statement( cond, state )
    print( state )

def main4():
	# if (3 < 5) {
	#   if (6 > 2) {
	# 		b = 5;
	#   }
	# }
	# else {
	#	c = 10;
	# }
    test = AST.Relation( AST.Value(3),">",Value(5) )
    stmnt1 = AST.Assignment( Variable("b"), AST.Value(5) )
    stmnt2 = AST.Assignment( Variable("c"), AST.Value(10) )
    test2 = AST.Relation( AST.Value(6),">",Value(2) )
    cond2 = AST.Condition( test2, stmnt1, Pass() )
    cond = AST.Condition( test, cond2, stmnt2 )
    state = State()
    state = M_Statement( cond, state )
    print( state )

def main5():
	# if (3 < 5) {
	# 	b = 5;
	#   b = 6;
	#   d = 42;
	# }
	# else {
	#	c = 10;
	# }
    test = AST.Relation( AST.Value(3),"<",AST.Value(5) )
    stmnt1a = AST.Assignment( AST.Identifier("a"), AST.Value(5) )
    stmnt1b = AST.Assignment( AST.Identifier("b"), AST.Value(6) )
    stmnt1c = AST.Assignment( AST.Identifier("d"), AST.Value(42) )
    stmnt1 = AST.Block( [stmnt1a,stmnt1b,stmnt1c] )
    stmnt2 = AST.Assignment( AST.Identifier("c"), AST.Value(10) )
    cond = AST.Condition( test, stmnt1, stmnt2 )
    state = State()
    state = M_Statement( cond, state )
    print( state )
    
def main6():
    # if (3 < 4 && 4 < 5) {
    #    a = 3
    # }
    # else {
    #    b = 3
    # }
	test1 = AST.Relation( AST.Value(3), "<", AST.Value(4) )
	test2 = AST.Relation( AST.Value(4), "<", AST.Value(5) )
	overall_test = AST.Conjunction( test1, "AND", test2 )
	stmnt1 = AST.Assignment( AST.Identifier( "A" ), AST.Value(3) )
	stmnt2 = AST.Assignment( AST.Identifier( "B" ), AST.Value(3) )
	cond = AST.Condition( overall_test, stmnt1, stmnt2 )
	state = State()
	state = M_Statement( cond, state )
	print( state )
	
def main7():
    a = AST.Identifier( "a" )
    state = State()
    state.update( a, AST.Value(1) )
    test1 = AST.Relation( a, "<", AST.Value(6) )
    body = AST.Assignment( a, AST.BinaryExpression( a, "+", AST.Value(1) ) )
    w = AST.While( test1, body )
    state = M_While( w, state )
    print(state)
	
if __name__ == '__main__':
    main1()
    main2()
    main6()
    main5()
    main7()