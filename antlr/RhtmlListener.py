# Generated from .\Rhtml.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RhtmlParser import RhtmlParser
else:
    from RhtmlParser import RhtmlParser

# This class defines a complete listener for a parse tree produced by RhtmlParser.
class RhtmlListener(ParseTreeListener):

    # Enter a parse tree produced by RhtmlParser#prog.
    def enterProg(self, ctx:RhtmlParser.ProgContext):
        pass

    # Exit a parse tree produced by RhtmlParser#prog.
    def exitProg(self, ctx:RhtmlParser.ProgContext):
        pass


    # Enter a parse tree produced by RhtmlParser#range.
    def enterRange(self, ctx:RhtmlParser.RangeContext):
        pass

    # Exit a parse tree produced by RhtmlParser#range.
    def exitRange(self, ctx:RhtmlParser.RangeContext):
        pass


    # Enter a parse tree produced by RhtmlParser#for_loop.
    def enterFor_loop(self, ctx:RhtmlParser.For_loopContext):
        pass

    # Exit a parse tree produced by RhtmlParser#for_loop.
    def exitFor_loop(self, ctx:RhtmlParser.For_loopContext):
        pass


    # Enter a parse tree produced by RhtmlParser#int_list.
    def enterInt_list(self, ctx:RhtmlParser.Int_listContext):
        pass

    # Exit a parse tree produced by RhtmlParser#int_list.
    def exitInt_list(self, ctx:RhtmlParser.Int_listContext):
        pass


    # Enter a parse tree produced by RhtmlParser#int_elems.
    def enterInt_elems(self, ctx:RhtmlParser.Int_elemsContext):
        pass

    # Exit a parse tree produced by RhtmlParser#int_elems.
    def exitInt_elems(self, ctx:RhtmlParser.Int_elemsContext):
        pass


    # Enter a parse tree produced by RhtmlParser#string_list.
    def enterString_list(self, ctx:RhtmlParser.String_listContext):
        pass

    # Exit a parse tree produced by RhtmlParser#string_list.
    def exitString_list(self, ctx:RhtmlParser.String_listContext):
        pass


    # Enter a parse tree produced by RhtmlParser#string_elems.
    def enterString_elems(self, ctx:RhtmlParser.String_elemsContext):
        pass

    # Exit a parse tree produced by RhtmlParser#string_elems.
    def exitString_elems(self, ctx:RhtmlParser.String_elemsContext):
        pass


    # Enter a parse tree produced by RhtmlParser#html_expr.
    def enterHtml_expr(self, ctx:RhtmlParser.Html_exprContext):
        pass

    # Exit a parse tree produced by RhtmlParser#html_expr.
    def exitHtml_expr(self, ctx:RhtmlParser.Html_exprContext):
        pass


    # Enter a parse tree produced by RhtmlParser#main_tag_expr.
    def enterMain_tag_expr(self, ctx:RhtmlParser.Main_tag_exprContext):
        pass

    # Exit a parse tree produced by RhtmlParser#main_tag_expr.
    def exitMain_tag_expr(self, ctx:RhtmlParser.Main_tag_exprContext):
        pass


    # Enter a parse tree produced by RhtmlParser#tag_expr.
    def enterTag_expr(self, ctx:RhtmlParser.Tag_exprContext):
        pass

    # Exit a parse tree produced by RhtmlParser#tag_expr.
    def exitTag_expr(self, ctx:RhtmlParser.Tag_exprContext):
        pass


    # Enter a parse tree produced by RhtmlParser#tag_inside.
    def enterTag_inside(self, ctx:RhtmlParser.Tag_insideContext):
        pass

    # Exit a parse tree produced by RhtmlParser#tag_inside.
    def exitTag_inside(self, ctx:RhtmlParser.Tag_insideContext):
        pass


    # Enter a parse tree produced by RhtmlParser#string_int_inside.
    def enterString_int_inside(self, ctx:RhtmlParser.String_int_insideContext):
        pass

    # Exit a parse tree produced by RhtmlParser#string_int_inside.
    def exitString_int_inside(self, ctx:RhtmlParser.String_int_insideContext):
        pass


    # Enter a parse tree produced by RhtmlParser#tag_option_expr.
    def enterTag_option_expr(self, ctx:RhtmlParser.Tag_option_exprContext):
        pass

    # Exit a parse tree produced by RhtmlParser#tag_option_expr.
    def exitTag_option_expr(self, ctx:RhtmlParser.Tag_option_exprContext):
        pass


    # Enter a parse tree produced by RhtmlParser#list.
    def enterList(self, ctx:RhtmlParser.ListContext):
        pass

    # Exit a parse tree produced by RhtmlParser#list.
    def exitList(self, ctx:RhtmlParser.ListContext):
        pass


    # Enter a parse tree produced by RhtmlParser#list_inside.
    def enterList_inside(self, ctx:RhtmlParser.List_insideContext):
        pass

    # Exit a parse tree produced by RhtmlParser#list_inside.
    def exitList_inside(self, ctx:RhtmlParser.List_insideContext):
        pass



del RhtmlParser