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
        4,1,25,177,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,0,
        1,1,1,1,3,1,44,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,56,
        8,3,1,3,1,3,1,3,1,3,1,3,4,3,63,8,3,11,3,12,3,64,1,3,1,3,1,4,1,4,
        3,4,71,8,4,1,4,1,4,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,6,1,
        6,3,6,85,8,6,1,6,1,6,1,7,1,7,1,7,5,7,92,8,7,10,7,12,7,95,9,7,1,8,
        1,8,1,8,5,8,100,8,8,10,8,12,8,103,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,5,9,112,8,9,10,9,12,9,115,9,9,1,9,1,9,1,10,1,10,1,10,5,10,122,
        8,10,10,10,12,10,125,9,10,1,10,1,10,5,10,129,8,10,10,10,12,10,132,
        9,10,1,10,1,10,1,10,1,10,5,10,138,8,10,10,10,12,10,141,9,10,1,10,
        3,10,144,8,10,1,11,1,11,1,11,1,11,3,11,150,8,11,1,12,1,12,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,162,8,14,10,14,12,14,165,9,
        14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,173,8,15,1,15,1,15,1,15,0,
        0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,1,1,0,23,24,185,
        0,35,1,0,0,0,2,43,1,0,0,0,4,45,1,0,0,0,6,51,1,0,0,0,8,68,1,0,0,0,
        10,74,1,0,0,0,12,82,1,0,0,0,14,88,1,0,0,0,16,96,1,0,0,0,18,106,1,
        0,0,0,20,143,1,0,0,0,22,149,1,0,0,0,24,151,1,0,0,0,26,153,1,0,0,
        0,28,157,1,0,0,0,30,168,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,
        38,39,3,16,8,0,39,40,5,0,0,1,40,1,1,0,0,0,41,44,3,20,10,0,42,44,
        3,6,3,0,43,41,1,0,0,0,43,42,1,0,0,0,44,3,1,0,0,0,45,46,5,13,0,0,
        46,47,5,24,0,0,47,48,5,15,0,0,48,49,5,24,0,0,49,50,5,14,0,0,50,5,
        1,0,0,0,51,55,5,17,0,0,52,56,3,4,2,0,53,56,3,8,4,0,54,56,3,12,6,
        0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,58,
        5,1,0,0,58,59,5,18,0,0,59,62,5,5,0,0,60,63,3,2,1,0,61,63,3,30,15,
        0,62,60,1,0,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,
        1,0,0,0,65,66,1,0,0,0,66,67,5,4,0,0,67,7,1,0,0,0,68,70,5,13,0,0,
        69,71,3,10,5,0,70,69,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,
        14,0,0,73,9,1,0,0,0,74,79,5,24,0,0,75,76,5,2,0,0,76,78,5,24,0,0,
        77,75,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,11,1,
        0,0,0,81,79,1,0,0,0,82,84,5,13,0,0,83,85,3,14,7,0,84,83,1,0,0,0,
        84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,14,0,0,87,13,1,0,0,0,88,93,5,
        23,0,0,89,90,5,2,0,0,90,92,5,23,0,0,91,89,1,0,0,0,92,95,1,0,0,0,
        93,91,1,0,0,0,93,94,1,0,0,0,94,15,1,0,0,0,95,93,1,0,0,0,96,97,5,
        6,0,0,97,101,5,5,0,0,98,100,3,18,9,0,99,98,1,0,0,0,100,103,1,0,0,
        0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,
        104,105,5,4,0,0,105,17,1,0,0,0,106,107,5,9,0,0,107,113,5,5,0,0,108,
        112,3,20,10,0,109,112,3,2,1,0,110,112,3,28,14,0,111,108,1,0,0,0,
        111,109,1,0,0,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,
        113,114,1,0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,117,5,4,0,0,
        117,19,1,0,0,0,118,119,5,10,0,0,119,123,5,5,0,0,120,122,3,26,13,
        0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,
        0,124,130,1,0,0,0,125,123,1,0,0,0,126,129,3,22,11,0,127,129,3,20,
        10,0,128,126,1,0,0,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,
        0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,130,1,0,0,0,133,144,5,4,
        0,0,134,135,5,11,0,0,135,139,5,5,0,0,136,138,3,26,13,0,137,136,1,
        0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,
        0,0,0,141,139,1,0,0,0,142,144,5,4,0,0,143,118,1,0,0,0,143,134,1,
        0,0,0,144,21,1,0,0,0,145,150,3,24,12,0,146,150,3,2,1,0,147,150,5,
        16,0,0,148,150,3,28,14,0,149,145,1,0,0,0,149,146,1,0,0,0,149,147,
        1,0,0,0,149,148,1,0,0,0,150,23,1,0,0,0,151,152,7,0,0,0,152,25,1,
        0,0,0,153,154,5,12,0,0,154,155,5,3,0,0,155,156,5,23,0,0,156,27,1,
        0,0,0,157,158,5,7,0,0,158,163,5,5,0,0,159,162,3,6,3,0,160,162,3,
        30,15,0,161,159,1,0,0,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,
        1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,
        5,4,0,0,167,29,1,0,0,0,168,169,5,8,0,0,169,172,5,5,0,0,170,173,3,
        24,12,0,171,173,5,16,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,174,
        1,0,0,0,174,175,5,4,0,0,175,31,1,0,0,0,21,35,43,55,62,64,70,79,84,
        93,101,111,113,123,128,130,139,143,149,161,163,172
    ]

class RhtmlParser ( Parser ):

    grammarFileName = "Rhtml.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "','", "'='", "'end'", "'do'", 
                     "'html'", "<INVALID>", "'li'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "'..'", "'iter'", 
                     "'for'", "'each'", "'string[]'", "'int[]'", "'str'", 
                     "'int'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "END", "DO", "HTML", "LIST", "LIST_ITEM", "MAIN_TAG", 
                      "DOUBLE_TAG", "SINGLE_TAG", "TAG_OPTION", "LEFT", 
                      "RIGHT", "DOTS", "ITER", "FOR", "EACH", "STRING_LIST_TYPE", 
                      "INT_LIST_TYPE", "STRING_TYPE", "INT_TYPE", "STRING", 
                      "INT", "WHITESPACE" ]

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
    RULE_list = 14
    RULE_list_inside = 15

    ruleNames =  [ "prog", "ruby_expr", "range", "for_loop", "int_list", 
                   "int_elems", "string_list", "string_elems", "html_expr", 
                   "main_tag_expr", "tag_expr", "tag_inside", "string_int_inside", 
                   "tag_option_expr", "list", "list_inside" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    END=4
    DO=5
    HTML=6
    LIST=7
    LIST_ITEM=8
    MAIN_TAG=9
    DOUBLE_TAG=10
    SINGLE_TAG=11
    TAG_OPTION=12
    LEFT=13
    RIGHT=14
    DOTS=15
    ITER=16
    FOR=17
    EACH=18
    STRING_LIST_TYPE=19
    INT_LIST_TYPE=20
    STRING_TYPE=21
    INT_TYPE=22
    STRING=23
    INT=24
    WHITESPACE=25

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 134144) != 0:
                self.state = 32
                self.ruby_expr()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.html_expr()
            self.state = 39
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
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.tag_expr()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
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
            self.state = 45
            self.match(RhtmlParser.LEFT)
            self.state = 46
            self.match(RhtmlParser.INT)
            self.state = 47
            self.match(RhtmlParser.DOTS)
            self.state = 48
            self.match(RhtmlParser.INT)
            self.state = 49
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


        def list_inside(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.List_insideContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.List_insideContext,i)


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
            self.state = 51
            self.match(RhtmlParser.FOR)
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 52
                self.range_()
                pass

            elif la_ == 2:
                self.state = 53
                self.int_list()
                pass

            elif la_ == 3:
                self.state = 54
                self.string_list()
                pass


            self.state = 57
            self.match(RhtmlParser.T__0)
            self.state = 58
            self.match(RhtmlParser.EACH)
            self.state = 59
            self.match(RhtmlParser.DO)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11, 17]:
                    self.state = 60
                    self.ruby_expr()
                    pass
                elif token in [8]:
                    self.state = 61
                    self.list_inside()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 134400) != 0):
                    break

            self.state = 66
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
            self.state = 68
            self.match(RhtmlParser.LEFT)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 69
                self.int_elems()


            self.state = 72
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
            self.state = 74
            self.match(RhtmlParser.INT)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 75
                self.match(RhtmlParser.T__1)
                self.state = 76
                self.match(RhtmlParser.INT)
                self.state = 81
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
            self.state = 82
            self.match(RhtmlParser.LEFT)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 83
                self.string_elems()


            self.state = 86
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
            self.state = 88
            self.match(RhtmlParser.STRING)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 89
                self.match(RhtmlParser.T__1)
                self.state = 90
                self.match(RhtmlParser.STRING)
                self.state = 95
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
            self.state = 96
            self.match(RhtmlParser.HTML)
            self.state = 97
            self.match(RhtmlParser.DO)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 98
                self.main_tag_expr()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
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


        def list_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.ListContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.ListContext,i)


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
            self.state = 106
            self.match(RhtmlParser.MAIN_TAG)
            self.state = 107
            self.match(RhtmlParser.DO)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 134272) != 0:
                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 108
                    self.tag_expr()
                    pass

                elif la_ == 2:
                    self.state = 109
                    self.ruby_expr()
                    pass

                elif la_ == 3:
                    self.state = 110
                    self.list_()
                    pass


                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
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
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(RhtmlParser.DOUBLE_TAG)
                self.state = 119
                self.match(RhtmlParser.DO)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 120
                    self.tag_option_expr()
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 25365632) != 0:
                    self.state = 128
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 126
                        self.tag_inside()
                        pass

                    elif la_ == 2:
                        self.state = 127
                        self.tag_expr()
                        pass


                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 133
                self.match(RhtmlParser.END)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(RhtmlParser.SINGLE_TAG)
                self.state = 135
                self.match(RhtmlParser.DO)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 136
                    self.tag_option_expr()
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 142
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

        def list_(self):
            return self.getTypedRuleContext(RhtmlParser.ListContext,0)


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
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.state = 145
                self.string_int_inside()
                pass
            elif token in [10, 11, 17]:
                self.state = 146
                self.ruby_expr()
                pass
            elif token in [16]:
                self.state = 147
                self.match(RhtmlParser.ITER)
                pass
            elif token in [7]:
                self.state = 148
                self.list_()
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
            self.state = 151
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
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
            self.state = 153
            self.match(RhtmlParser.TAG_OPTION)
            self.state = 154
            self.match(RhtmlParser.T__2)
            self.state = 155
            self.match(RhtmlParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(RhtmlParser.LIST, 0)

        def DO(self):
            return self.getToken(RhtmlParser.DO, 0)

        def END(self):
            return self.getToken(RhtmlParser.END, 0)

        def for_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.For_loopContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.For_loopContext,i)


        def list_inside(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.List_insideContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.List_insideContext,i)


        def getRuleIndex(self):
            return RhtmlParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = RhtmlParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(RhtmlParser.LIST)
            self.state = 158
            self.match(RhtmlParser.DO)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==17:
                self.state = 161
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17]:
                    self.state = 159
                    self.for_loop()
                    pass
                elif token in [8]:
                    self.state = 160
                    self.list_inside()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(RhtmlParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_insideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST_ITEM(self):
            return self.getToken(RhtmlParser.LIST_ITEM, 0)

        def DO(self):
            return self.getToken(RhtmlParser.DO, 0)

        def END(self):
            return self.getToken(RhtmlParser.END, 0)

        def string_int_inside(self):
            return self.getTypedRuleContext(RhtmlParser.String_int_insideContext,0)


        def ITER(self):
            return self.getToken(RhtmlParser.ITER, 0)

        def getRuleIndex(self):
            return RhtmlParser.RULE_list_inside

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_inside" ):
                listener.enterList_inside(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_inside" ):
                listener.exitList_inside(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_inside" ):
                return visitor.visitList_inside(self)
            else:
                return visitor.visitChildren(self)




    def list_inside(self):

        localctx = RhtmlParser.List_insideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_inside)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(RhtmlParser.LIST_ITEM)
            self.state = 169
            self.match(RhtmlParser.DO)
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.state = 170
                self.string_int_inside()
                pass
            elif token in [16]:
                self.state = 171
                self.match(RhtmlParser.ITER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 174
            self.match(RhtmlParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





