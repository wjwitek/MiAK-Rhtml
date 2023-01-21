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
        4,1,21,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,
        2,44,8,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,52,8,2,11,2,12,2,53,1,2,1,2,
        1,3,1,3,3,3,60,8,3,1,3,1,3,1,4,1,4,1,4,5,4,67,8,4,10,4,12,4,70,9,
        4,1,5,1,5,3,5,74,8,5,1,5,1,5,1,6,1,6,1,6,5,6,81,8,6,10,6,12,6,84,
        9,6,1,7,1,7,1,7,5,7,89,8,7,10,7,12,7,92,9,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,8,5,8,102,8,8,10,8,12,8,105,9,8,1,8,1,8,1,9,1,9,1,9,5,
        9,112,8,9,10,9,12,9,115,9,9,1,9,5,9,118,8,9,10,9,12,9,121,9,9,1,
        9,1,9,1,9,1,9,5,9,127,8,9,10,9,12,9,130,9,9,1,9,3,9,133,8,9,1,10,
        1,10,1,10,1,10,1,10,3,10,140,8,10,1,11,1,11,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,5,13,152,8,13,10,13,12,13,155,9,13,1,13,1,13,
        1,14,1,14,1,14,1,14,3,14,163,8,14,1,14,1,14,1,14,0,0,15,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,0,1,1,0,19,20,176,0,30,1,0,0,0,2,
        33,1,0,0,0,4,39,1,0,0,0,6,57,1,0,0,0,8,63,1,0,0,0,10,71,1,0,0,0,
        12,77,1,0,0,0,14,85,1,0,0,0,16,95,1,0,0,0,18,132,1,0,0,0,20,139,
        1,0,0,0,22,141,1,0,0,0,24,143,1,0,0,0,26,147,1,0,0,0,28,158,1,0,
        0,0,30,31,3,14,7,0,31,32,5,0,0,1,32,1,1,0,0,0,33,34,5,12,0,0,34,
        35,5,19,0,0,35,36,5,1,0,0,36,37,5,19,0,0,37,38,5,13,0,0,38,3,1,0,
        0,0,39,43,5,15,0,0,40,44,3,2,1,0,41,44,3,6,3,0,42,44,3,10,5,0,43,
        40,1,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,45,1,0,0,0,45,46,5,2,0,
        0,46,47,5,16,0,0,47,51,5,18,0,0,48,52,3,18,9,0,49,52,3,4,2,0,50,
        52,3,28,14,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,53,1,0,
        0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,17,0,0,56,
        5,1,0,0,0,57,59,5,12,0,0,58,60,3,8,4,0,59,58,1,0,0,0,59,60,1,0,0,
        0,60,61,1,0,0,0,61,62,5,13,0,0,62,7,1,0,0,0,63,68,5,19,0,0,64,65,
        5,3,0,0,65,67,5,19,0,0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,
        68,69,1,0,0,0,69,9,1,0,0,0,70,68,1,0,0,0,71,73,5,12,0,0,72,74,3,
        12,6,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,76,5,13,0,0,
        76,11,1,0,0,0,77,82,5,20,0,0,78,79,5,3,0,0,79,81,5,20,0,0,80,78,
        1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,13,1,0,0,0,
        84,82,1,0,0,0,85,86,5,5,0,0,86,90,5,18,0,0,87,89,3,16,8,0,88,87,
        1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,
        92,90,1,0,0,0,93,94,5,17,0,0,94,15,1,0,0,0,95,96,5,8,0,0,96,103,
        5,18,0,0,97,102,3,18,9,0,98,102,3,18,9,0,99,102,3,4,2,0,100,102,
        3,26,13,0,101,97,1,0,0,0,101,98,1,0,0,0,101,99,1,0,0,0,101,100,1,
        0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,
        0,0,0,105,103,1,0,0,0,106,107,5,17,0,0,107,17,1,0,0,0,108,109,5,
        9,0,0,109,113,5,18,0,0,110,112,3,24,12,0,111,110,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,119,1,0,0,0,115,113,
        1,0,0,0,116,118,3,20,10,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,133,
        5,17,0,0,123,124,5,10,0,0,124,128,5,18,0,0,125,127,3,24,12,0,126,
        125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,
        131,1,0,0,0,130,128,1,0,0,0,131,133,5,17,0,0,132,108,1,0,0,0,132,
        123,1,0,0,0,133,19,1,0,0,0,134,140,3,22,11,0,135,140,3,18,9,0,136,
        140,3,4,2,0,137,140,5,14,0,0,138,140,3,26,13,0,139,134,1,0,0,0,139,
        135,1,0,0,0,139,136,1,0,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,
        21,1,0,0,0,141,142,7,0,0,0,142,23,1,0,0,0,143,144,5,11,0,0,144,145,
        5,4,0,0,145,146,5,20,0,0,146,25,1,0,0,0,147,148,5,6,0,0,148,153,
        5,18,0,0,149,152,3,4,2,0,150,152,3,28,14,0,151,149,1,0,0,0,151,150,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,156,
        1,0,0,0,155,153,1,0,0,0,156,157,5,17,0,0,157,27,1,0,0,0,158,159,
        5,7,0,0,159,162,5,18,0,0,160,163,3,22,11,0,161,163,5,14,0,0,162,
        160,1,0,0,0,162,161,1,0,0,0,163,164,1,0,0,0,164,165,5,17,0,0,165,
        29,1,0,0,0,18,43,51,53,59,68,73,82,90,101,103,113,119,128,132,139,
        151,153,162
    ]

class RhtmlParser ( Parser ):

    grammarFileName = "Rhtml.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "'.'", "','", "'='", "'html'", 
                     "<INVALID>", "'li'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'['", "']'", "'iter'", "'for'", "'each'", 
                     "'end'", "'do'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "HTML", "LIST", "LIST_ITEM", "MAIN_TAG", 
                      "DOUBLE_TAG", "SINGLE_TAG", "TAG_OPTION", "LEFT", 
                      "RIGHT", "ITER", "FOR", "EACH", "END", "DO", "INT", 
                      "STRING", "WHITESPACE" ]

    RULE_prog = 0
    RULE_range = 1
    RULE_for_loop = 2
    RULE_int_list = 3
    RULE_int_elems = 4
    RULE_string_list = 5
    RULE_string_elems = 6
    RULE_html_expr = 7
    RULE_main_tag_expr = 8
    RULE_tag_expr = 9
    RULE_tag_inside = 10
    RULE_string_int_inside = 11
    RULE_tag_option_expr = 12
    RULE_list = 13
    RULE_list_inside = 14

    ruleNames =  [ "prog", "range", "for_loop", "int_list", "int_elems", 
                   "string_list", "string_elems", "html_expr", "main_tag_expr", 
                   "tag_expr", "tag_inside", "string_int_inside", "tag_option_expr", 
                   "list", "list_inside" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    HTML=5
    LIST=6
    LIST_ITEM=7
    MAIN_TAG=8
    DOUBLE_TAG=9
    SINGLE_TAG=10
    TAG_OPTION=11
    LEFT=12
    RIGHT=13
    ITER=14
    FOR=15
    EACH=16
    END=17
    DO=18
    INT=19
    STRING=20
    WHITESPACE=21

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

        def getRuleIndex(self):
            return RhtmlParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = RhtmlParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.html_expr()
            self.state = 31
            self.match(RhtmlParser.EOF)
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




    def range_(self):

        localctx = RhtmlParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(RhtmlParser.LEFT)
            self.state = 34
            self.match(RhtmlParser.INT)
            self.state = 35
            self.match(RhtmlParser.T__0)
            self.state = 36
            self.match(RhtmlParser.INT)
            self.state = 37
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


        def tag_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.Tag_exprContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.Tag_exprContext,i)


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
            return RhtmlParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)




    def for_loop(self):

        localctx = RhtmlParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(RhtmlParser.FOR)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 40
                self.range_()
                pass

            elif la_ == 2:
                self.state = 41
                self.int_list()
                pass

            elif la_ == 3:
                self.state = 42
                self.string_list()
                pass


            self.state = 45
            self.match(RhtmlParser.T__1)
            self.state = 46
            self.match(RhtmlParser.EACH)
            self.state = 47
            self.match(RhtmlParser.DO)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9, 10]:
                    self.state = 48
                    self.tag_expr()
                    pass
                elif token in [15]:
                    self.state = 49
                    self.for_loop()
                    pass
                elif token in [7]:
                    self.state = 50
                    self.list_inside()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 34432) != 0):
                    break

            self.state = 55
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




    def int_list(self):

        localctx = RhtmlParser.Int_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_int_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(RhtmlParser.LEFT)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 58
                self.int_elems()


            self.state = 61
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




    def int_elems(self):

        localctx = RhtmlParser.Int_elemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_int_elems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(RhtmlParser.INT)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 64
                self.match(RhtmlParser.T__2)
                self.state = 65
                self.match(RhtmlParser.INT)
                self.state = 70
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




    def string_list(self):

        localctx = RhtmlParser.String_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_string_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(RhtmlParser.LEFT)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 72
                self.string_elems()


            self.state = 75
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




    def string_elems(self):

        localctx = RhtmlParser.String_elemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_string_elems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(RhtmlParser.STRING)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 78
                self.match(RhtmlParser.T__2)
                self.state = 79
                self.match(RhtmlParser.STRING)
                self.state = 84
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




    def html_expr(self):

        localctx = RhtmlParser.Html_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_html_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(RhtmlParser.HTML)
            self.state = 86
            self.match(RhtmlParser.DO)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 87
                self.main_tag_expr()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
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


        def for_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RhtmlParser.For_loopContext)
            else:
                return self.getTypedRuleContext(RhtmlParser.For_loopContext,i)


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




    def main_tag_expr(self):

        localctx = RhtmlParser.Main_tag_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_main_tag_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(RhtmlParser.MAIN_TAG)
            self.state = 96
            self.match(RhtmlParser.DO)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 34368) != 0:
                self.state = 101
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 97
                    self.tag_expr()
                    pass

                elif la_ == 2:
                    self.state = 98
                    self.tag_expr()
                    pass

                elif la_ == 3:
                    self.state = 99
                    self.for_loop()
                    pass

                elif la_ == 4:
                    self.state = 100
                    self.list_()
                    pass


                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
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




    def tag_expr(self):

        localctx = RhtmlParser.Tag_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tag_expr)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(RhtmlParser.DOUBLE_TAG)
                self.state = 109
                self.match(RhtmlParser.DO)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 110
                    self.tag_option_expr()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1623616) != 0:
                    self.state = 116
                    self.tag_inside()
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 122
                self.match(RhtmlParser.END)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(RhtmlParser.SINGLE_TAG)
                self.state = 124
                self.match(RhtmlParser.DO)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 125
                    self.tag_option_expr()
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 131
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


        def tag_expr(self):
            return self.getTypedRuleContext(RhtmlParser.Tag_exprContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(RhtmlParser.For_loopContext,0)


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




    def tag_inside(self):

        localctx = RhtmlParser.Tag_insideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tag_inside)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20]:
                self.state = 134
                self.string_int_inside()
                pass
            elif token in [9, 10]:
                self.state = 135
                self.tag_expr()
                pass
            elif token in [15]:
                self.state = 136
                self.for_loop()
                pass
            elif token in [14]:
                self.state = 137
                self.match(RhtmlParser.ITER)
                pass
            elif token in [6]:
                self.state = 138
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




    def string_int_inside(self):

        localctx = RhtmlParser.String_int_insideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_string_int_inside)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
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




    def tag_option_expr(self):

        localctx = RhtmlParser.Tag_option_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tag_option_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(RhtmlParser.TAG_OPTION)
            self.state = 144
            self.match(RhtmlParser.T__3)
            self.state = 145
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




    def list_(self):

        localctx = RhtmlParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(RhtmlParser.LIST)
            self.state = 148
            self.match(RhtmlParser.DO)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==15:
                self.state = 151
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 149
                    self.for_loop()
                    pass
                elif token in [7]:
                    self.state = 150
                    self.list_inside()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
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




    def list_inside(self):

        localctx = RhtmlParser.List_insideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_inside)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(RhtmlParser.LIST_ITEM)
            self.state = 159
            self.match(RhtmlParser.DO)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20]:
                self.state = 160
                self.string_int_inside()
                pass
            elif token in [14]:
                self.state = 161
                self.match(RhtmlParser.ITER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 164
            self.match(RhtmlParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





