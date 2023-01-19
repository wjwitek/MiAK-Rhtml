# Generated from .\Rhtml.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,0,1,1,1,1,3,1,40,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,52,8,3,1,3,1,3,1,3,1,3,
        4,3,58,8,3,11,3,12,3,59,1,3,1,3,1,4,1,4,3,4,66,8,4,1,4,1,4,1,5,1,
        5,1,5,5,5,73,8,5,10,5,12,5,76,9,5,1,6,1,6,3,6,80,8,6,1,6,1,6,1,7,
        1,7,1,7,5,7,87,8,7,10,7,12,7,90,9,7,1,8,1,8,1,8,5,8,95,8,8,10,8,
        12,8,98,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,106,8,9,10,9,12,9,109,9,
        9,1,9,1,9,1,10,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,10,1,10,
        1,10,5,10,123,8,10,10,10,12,10,126,9,10,1,10,1,10,1,10,1,10,5,10,
        132,8,10,10,10,12,10,135,9,10,1,10,3,10,138,8,10,1,11,1,11,1,11,
        3,11,143,8,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,0,0,14,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,0,1,1,0,21,22,155,0,31,1,0,0,0,2,39,
        1,0,0,0,4,41,1,0,0,0,6,47,1,0,0,0,8,63,1,0,0,0,10,69,1,0,0,0,12,
        77,1,0,0,0,14,83,1,0,0,0,16,91,1,0,0,0,18,101,1,0,0,0,20,137,1,0,
        0,0,22,142,1,0,0,0,24,144,1,0,0,0,26,146,1,0,0,0,28,30,3,2,1,0,29,
        28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,
        0,33,31,1,0,0,0,34,35,3,16,8,0,35,36,5,0,0,1,36,1,1,0,0,0,37,40,
        3,20,10,0,38,40,3,6,3,0,39,37,1,0,0,0,39,38,1,0,0,0,40,3,1,0,0,0,
        41,42,5,11,0,0,42,43,5,22,0,0,43,44,5,13,0,0,44,45,5,22,0,0,45,46,
        5,12,0,0,46,5,1,0,0,0,47,51,5,15,0,0,48,52,3,4,2,0,49,52,3,8,4,0,
        50,52,3,12,6,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,53,1,
        0,0,0,53,54,5,1,0,0,54,55,5,16,0,0,55,57,5,5,0,0,56,58,3,2,1,0,57,
        56,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,
        0,61,62,5,4,0,0,62,7,1,0,0,0,63,65,5,11,0,0,64,66,3,10,5,0,65,64,
        1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,12,0,0,68,9,1,0,0,0,
        69,74,5,22,0,0,70,71,5,2,0,0,71,73,5,22,0,0,72,70,1,0,0,0,73,76,
        1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,11,1,0,0,0,76,74,1,0,0,0,
        77,79,5,11,0,0,78,80,3,14,7,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,
        1,0,0,0,81,82,5,12,0,0,82,13,1,0,0,0,83,88,5,21,0,0,84,85,5,2,0,
        0,85,87,5,21,0,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,
        1,0,0,0,89,15,1,0,0,0,90,88,1,0,0,0,91,92,5,6,0,0,92,96,5,5,0,0,
        93,95,3,18,9,0,94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,
        0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,99,100,5,4,0,0,100,17,1,0,0,0,
        101,102,5,7,0,0,102,107,5,5,0,0,103,106,3,20,10,0,104,106,3,2,1,
        0,105,103,1,0,0,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,
        0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,5,4,0,
        0,111,19,1,0,0,0,112,113,5,8,0,0,113,117,5,5,0,0,114,116,3,26,13,
        0,115,114,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,
        0,118,124,1,0,0,0,119,117,1,0,0,0,120,123,3,22,11,0,121,123,3,20,
        10,0,122,120,1,0,0,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,
        0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,138,5,4,
        0,0,128,129,5,9,0,0,129,133,5,5,0,0,130,132,3,26,13,0,131,130,1,
        0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,
        0,0,0,135,133,1,0,0,0,136,138,5,4,0,0,137,112,1,0,0,0,137,128,1,
        0,0,0,138,21,1,0,0,0,139,143,3,24,12,0,140,143,3,2,1,0,141,143,5,
        14,0,0,142,139,1,0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,23,1,
        0,0,0,144,145,7,0,0,0,145,25,1,0,0,0,146,147,5,10,0,0,147,148,5,
        3,0,0,148,149,5,21,0,0,149,27,1,0,0,0,17,31,39,51,59,65,74,79,88,
        96,105,107,117,122,124,133,137,142
    ]

class RhtmlParser ( Parser ):

    grammarFileName = "Rhtml.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "'='", "'end'", "'do'", 
                     "'html'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'['", "']'", "'..'", "'iter'", "'for'", "'each'", 
                     "'string[]'", "'int[]'", "'str'", "'int'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "END", "DO", "HTML", "MAIN_TAG", "DOUBLE_TAG", "SINGLE_TAG", 
                      "TAG_OPTION", "LEFT", "RIGHT", "DOTS", "ITER", "FOR", 
                      "EACH", "STRING_LIST_TYPE", "INT_LIST_TYPE", "STRING_TYPE", 
                      "INT_TYPE", "STRING", "INT", "WHITESPACE" ]

    RULE_prog = 0
    RULE_ruby_expr = 1
    RULE_range = 2
    RULE_for_loop = 3
    RULE_int_list = 4
    RULE_int_elems = 5
    RULE_string_list = 6
    RULE_string_elems = 7
    RULE_html_expr = 8
    RULE_main_tag_expr = 9
    RULE_tag_expr = 10
    RULE_tag_inside = 11
    RULE_string_int_inside = 12
    RULE_tag_option_expr = 13

    ruleNames =  [ "prog", "ruby_expr", "range", "for_loop", "int_list", 
                   "int_elems", "string_list", "string_elems", "html_expr", 
                   "main_tag_expr", "tag_expr", "tag_inside", "string_int_inside", 
                   "tag_option_expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    END=4
    DO=5
    HTML=6
    MAIN_TAG=7
    DOUBLE_TAG=8
    SINGLE_TAG=9
    TAG_OPTION=10
    LEFT=11
    RIGHT=12
    DOTS=13
    ITER=14
    FOR=15
    EACH=16
    STRING_LIST_TYPE=17
    INT_LIST_TYPE=18
    STRING_TYPE=19
    INT_TYPE=20
    STRING=21
    INT=22
    WHITESPACE=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def html_expr(self):
            return self.getTypedRuleContext(RhtmlParser.Html_exprContext,0)


        def EOF(self):
            return self.getToken(RhtmlParser.EOF, 0)

        def ruby_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Ruby_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Ruby_exprContext,i)


        def getRuleIndex(self):
            return RhtmlParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RhtmlParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33536) != 0:
                self.state = 28
                self.ruby_expr()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.html_expr()
            self.state = 35
            self.match(RhtmlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ruby_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tag_expr(self):
            return self.getTypedRuleContext(RhtmlParser.Tag_exprContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(RhtmlParser.For_loopContext,0)


        def getRuleIndex(self):
            return RhtmlParser.RULE_ruby_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuby_expr" ):
                listener.enterRuby_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuby_expr" ):
                listener.exitRuby_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuby_expr" ):
                return visitor.visitRuby_expr(self)
            else:
                return visitor.visitChildren(self)




    def ruby_expr(self):

        localctx = RhtmlParser.Ruby_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ruby_expr)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.tag_expr()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.for_loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(RhtmlParser.LEFT, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(RhtmlParser.INT)
            else:
                return self.getToken(RhtmlParser.INT, i)

        def DOTS(self):
            return self.getToken(RhtmlParser.DOTS, 0)

        def RIGHT(self):
            return self.getToken(RhtmlParser.RIGHT, 0)

        def getRuleIndex(self):
            return RhtmlParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = RhtmlParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(RhtmlParser.LEFT)
            self.state = 42
            self.match(RhtmlParser.INT)
            self.state = 43
            self.match(RhtmlParser.DOTS)
            self.state = 44
            self.match(RhtmlParser.INT)
            self.state = 45
            self.match(RhtmlParser.RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(RhtmlParser.FOR, 0)

        def EACH(self):
            return self.getToken(RhtmlParser.EACH, 0)

        def DO(self):
            return self.getToken(RhtmlParser.DO, 0)

        def END(self):
            return self.getToken(RhtmlParser.END, 0)

        def range_(self):
            return self.getTypedRuleContext(RhtmlParser.RangeContext,0)


        def int_list(self):
            return self.getTypedRuleContext(RhtmlParser.Int_listContext,0)


        def string_list(self):
            return self.getTypedRuleContext(RhtmlParser.String_listContext,0)


        def ruby_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Ruby_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Ruby_exprContext,i)


        def getRuleIndex(self):
            return RhtmlParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = RhtmlParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(RhtmlParser.FOR)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 48
                self.range_()
                pass

            elif la_ == 2:
                self.state = 49
                self.int_list()
                pass

            elif la_ == 3:
                self.state = 50
                self.string_list()
                pass


            self.state = 53
            self.match(RhtmlParser.T__0)
            self.state = 54
            self.match(RhtmlParser.EACH)
            self.state = 55
            self.match(RhtmlParser.DO)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.ruby_expr()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 33536) != 0):
                    break

            self.state = 61
            self.match(RhtmlParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(RhtmlParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(RhtmlParser.RIGHT, 0)

        def int_elems(self):
            return self.getTypedRuleContext(RhtmlParser.Int_elemsContext,0)


        def getRuleIndex(self):
            return RhtmlParser.RULE_int_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_list" ):
                listener.enterInt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_list" ):
                listener.exitInt_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_list" ):
                return visitor.visitInt_list(self)
            else:
                return visitor.visitChildren(self)




    def int_list(self):

        localctx = RhtmlParser.Int_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_int_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(RhtmlParser.LEFT)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 64
                self.int_elems()


            self.state = 67
            self.match(RhtmlParser.RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_elemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(RhtmlParser.INT)
            else:
                return self.getToken(RhtmlParser.INT, i)

        def getRuleIndex(self):
            return RhtmlParser.RULE_int_elems

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_elems" ):
                listener.enterInt_elems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_elems" ):
                listener.exitInt_elems(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_elems" ):
                return visitor.visitInt_elems(self)
            else:
                return visitor.visitChildren(self)




    def int_elems(self):

        localctx = RhtmlParser.Int_elemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_int_elems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(RhtmlParser.INT)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 70
                self.match(RhtmlParser.T__1)
                self.state = 71
                self.match(RhtmlParser.INT)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(RhtmlParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(RhtmlParser.RIGHT, 0)

        def string_elems(self):
            return self.getTypedRuleContext(RhtmlParser.String_elemsContext,0)


        def getRuleIndex(self):
            return RhtmlParser.RULE_string_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_list" ):
                listener.enterString_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_list" ):
                listener.exitString_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_list" ):
                return visitor.visitString_list(self)
            else:
                return visitor.visitChildren(self)




    def string_list(self):

        localctx = RhtmlParser.String_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_string_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(RhtmlParser.LEFT)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 78
                self.string_elems()


            self.state = 81
            self.match(RhtmlParser.RIGHT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_elemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(RhtmlParser.STRING)
            else:
                return self.getToken(RhtmlParser.STRING, i)

        def getRuleIndex(self):
            return RhtmlParser.RULE_string_elems

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_elems" ):
                listener.enterString_elems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_elems" ):
                listener.exitString_elems(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_elems" ):
                return visitor.visitString_elems(self)
            else:
                return visitor.visitChildren(self)




    def string_elems(self):

        localctx = RhtmlParser.String_elemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string_elems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(RhtmlParser.STRING)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 84
                self.match(RhtmlParser.T__1)
                self.state = 85
                self.match(RhtmlParser.STRING)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Html_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HTML(self):
            return self.getToken(RhtmlParser.HTML, 0)

        def DO(self):
            return self.getToken(RhtmlParser.DO, 0)

        def END(self):
            return self.getToken(RhtmlParser.END, 0)

        def main_tag_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Main_tag_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Main_tag_exprContext,i)


        def getRuleIndex(self):
            return RhtmlParser.RULE_html_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtml_expr" ):
                listener.enterHtml_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtml_expr" ):
                listener.exitHtml_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHtml_expr" ):
                return visitor.visitHtml_expr(self)
            else:
                return visitor.visitChildren(self)




    def html_expr(self):

        localctx = RhtmlParser.Html_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_html_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(RhtmlParser.HTML)
            self.state = 92
            self.match(RhtmlParser.DO)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 93
                self.main_tag_expr()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(RhtmlParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_tag_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN_TAG(self):
            return self.getToken(RhtmlParser.MAIN_TAG, 0)

        def DO(self):
            return self.getToken(RhtmlParser.DO, 0)

        def END(self):
            return self.getToken(RhtmlParser.END, 0)

        def tag_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Tag_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Tag_exprContext,i)


        def ruby_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Ruby_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Ruby_exprContext,i)


        def getRuleIndex(self):
            return RhtmlParser.RULE_main_tag_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_tag_expr" ):
                listener.enterMain_tag_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_tag_expr" ):
                listener.exitMain_tag_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_tag_expr" ):
                return visitor.visitMain_tag_expr(self)
            else:
                return visitor.visitChildren(self)




    def main_tag_expr(self):

        localctx = RhtmlParser.Main_tag_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_main_tag_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(RhtmlParser.MAIN_TAG)
            self.state = 102
            self.match(RhtmlParser.DO)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33536) != 0:
                self.state = 105
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 103
                    self.tag_expr()
                    pass

                elif la_ == 2:
                    self.state = 104
                    self.ruby_expr()
                    pass


                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(RhtmlParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_TAG(self):
            return self.getToken(RhtmlParser.DOUBLE_TAG, 0)

        def DO(self):
            return self.getToken(RhtmlParser.DO, 0)

        def END(self):
            return self.getToken(RhtmlParser.END, 0)

        def tag_option_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Tag_option_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Tag_option_exprContext,i)


        def tag_inside(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Tag_insideContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Tag_insideContext,i)


        def tag_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Tag_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Tag_exprContext,i)


        def SINGLE_TAG(self):
            return self.getToken(RhtmlParser.SINGLE_TAG, 0)

        def getRuleIndex(self):
            return RhtmlParser.RULE_tag_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_expr" ):
                listener.enterTag_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_expr" ):
                listener.exitTag_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag_expr" ):
                return visitor.visitTag_expr(self)
            else:
                return visitor.visitChildren(self)




    def tag_expr(self):

        localctx = RhtmlParser.Tag_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tag_expr)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(RhtmlParser.DOUBLE_TAG)
                self.state = 113
                self.match(RhtmlParser.DO)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 114
                    self.tag_option_expr()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 6341376) != 0:
                    self.state = 122
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        self.state = 120
                        self.tag_inside()
                        pass

                    elif la_ == 2:
                        self.state = 121
                        self.tag_expr()
                        pass


                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 127
                self.match(RhtmlParser.END)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(RhtmlParser.SINGLE_TAG)
                self.state = 129
                self.match(RhtmlParser.DO)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 130
                    self.tag_option_expr()
                    self.state = 135
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 136
                self.match(RhtmlParser.END)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_insideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_int_inside(self):
            return self.getTypedRuleContext(RhtmlParser.String_int_insideContext,0)


        def ruby_expr(self):
            return self.getTypedRuleContext(RhtmlParser.Ruby_exprContext,0)


        def ITER(self):
            return self.getToken(RhtmlParser.ITER, 0)

        def getRuleIndex(self):
            return RhtmlParser.RULE_tag_inside

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_inside" ):
                listener.enterTag_inside(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_inside" ):
                listener.exitTag_inside(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag_inside" ):
                return visitor.visitTag_inside(self)
            else:
                return visitor.visitChildren(self)




    def tag_inside(self):

        localctx = RhtmlParser.Tag_insideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tag_inside)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22]:
                self.state = 139
                self.string_int_inside()
                pass
            elif token in [8, 9, 15]:
                self.state = 140
                self.ruby_expr()
                pass
            elif token in [14]:
                self.state = 141
                self.match(RhtmlParser.ITER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_int_insideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(RhtmlParser.STRING, 0)

        def INT(self):
            return self.getToken(RhtmlParser.INT, 0)

        def getRuleIndex(self):
            return RhtmlParser.RULE_string_int_inside

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_int_inside" ):
                listener.enterString_int_inside(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_int_inside" ):
                listener.exitString_int_inside(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_int_inside" ):
                return visitor.visitString_int_inside(self)
            else:
                return visitor.visitChildren(self)




    def string_int_inside(self):

        localctx = RhtmlParser.String_int_insideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_string_int_inside)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_option_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_OPTION(self):
            return self.getToken(RhtmlParser.TAG_OPTION, 0)

        def STRING(self):
            return self.getToken(RhtmlParser.STRING, 0)

        def getRuleIndex(self):
            return RhtmlParser.RULE_tag_option_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_option_expr" ):
                listener.enterTag_option_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_option_expr" ):
                listener.exitTag_option_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag_option_expr" ):
                return visitor.visitTag_option_expr(self)
            else:
                return visitor.visitChildren(self)




    def tag_option_expr(self):

        localctx = RhtmlParser.Tag_option_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tag_option_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(RhtmlParser.TAG_OPTION)
            self.state = 147
            self.match(RhtmlParser.T__2)
            self.state = 148
            self.match(RhtmlParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





