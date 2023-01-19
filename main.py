import sys

import antlr4

from antlr.RhtmlLexer import RhtmlLexer
from antlr.RhtmlParser import RhtmlParser
from antlr.RhtmlVisitor import RhtmlVisitor

file_input = antlr4.FileStream(sys.argv[1])
lexer = RhtmlLexer(file_input)
tokens = antlr4.CommonTokenStream(lexer)
parser = RhtmlParser(tokens)
tree = parser.prog()
visitor = RhtmlVisitor(sys.argv[2])
visitor.visit(tree)
