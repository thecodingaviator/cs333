# Stephanie Taylor
# Test a line of Cliter code (in test.c)
# Written in Python2. If you want to run with Python 3, then you will need to update the print statements.
import simple_interpreter
import build_AST

def main(fn):
    p = build_AST.Parser( fn )
    p.buildTree()
    print "AST"
    p.ast.printTree( "" )
    state = simple_interpreter.State()
    state = simple_interpreter.M_Statement( p.ast, state )
    print "\nstate"
    print state

if __name__ == "__main__":
    main( 'test.c' )
	
