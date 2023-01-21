# Generated from .\Rhtml.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RhtmlParser import RhtmlParser
else:
    from antlr.RhtmlParser import RhtmlParser


# This class defines a complete generic visitor for a parse tree produced by RhtmlParser.

def tabs(ctx):
    return ctx.depth() // 2 - 1


class RhtmlVisitor(ParseTreeVisitor):

    def __init__(self, output_file):
        self.output_name = output_file
        self.file = None
        self.iter = None
        self.for_count = 0

        super(RhtmlVisitor, self).__init__()

    # Visit a parse tree produced by RhtmlParser#prog.
    def visitProg(self, ctx: RhtmlParser.ProgContext):
        self.file = open(self.output_name, "w")
        self.visitChildren(ctx)
        self.file.close()

    # Visit a parse tree produced by RhtmlParser#range.
    @staticmethod
    def visitRange(ctx: RhtmlParser.RangeContext):
        return range(int(str(ctx.INT(0))), int(str(ctx.INT(1))))

    # Visit a parse tree produced by RhtmlParser#for_loop.
    def visitFor_loop(self, ctx: RhtmlParser.For_loopContext):
        self.for_count += 1

        if ctx.range_() is not None:
            for_range = self.visitRange(ctx.range_())
        elif ctx.int_list() is not None:
            for_range = self.visitInt_list(ctx.int_list())
        else:
            for_range = self.visitString_list(ctx.string_list())

        for i in for_range:
            self.iter = i
            self.visitChildren(ctx)

        self.for_count -= 1

    # Visit a parse tree produced by RhtmlParser#int_list.
    def visitInt_list(self, ctx: RhtmlParser.Int_listContext):
        return self.visitInt_elems(ctx.int_elems())

    # Visit a parse tree produced by RhtmlParser#int_elems.
    @staticmethod
    def visitInt_elems(ctx: RhtmlParser.Int_elemsContext):
        elems = []
        for i in range(ctx.getChildCount() - 1):
            elems.append(int(str(ctx.INT(i))))
        return elems

    # Visit a parse tree produced by RhtmlParser#string_list.
    def visitString_list(self, ctx: RhtmlParser.String_listContext):
        return self.visitString_elems(ctx.string_elems())

    # Visit a parse tree produced by RhtmlParser#string_elems.
    @staticmethod
    def visitString_elems(ctx: RhtmlParser.String_elemsContext):
        elems = []
        for i in range(ctx.getChildCount() - 1):
            if str(ctx.STRING()) != 'None':
                elems.append(str(ctx.STRING(i)).replace("\"", ""))
        return elems

    # Visit a parse tree produced by RhtmlParser#html_expr.
    def visitHtml_expr(self, ctx: RhtmlParser.Html_exprContext):
        self.file.write('<html>\n')
        self.visitChildren(ctx)
        self.file.write('</html>')

    # Visit a parse tree produced by RhtmlParser#main_tag_expr.
    def visitMain_tag_expr(self, ctx: RhtmlParser.Main_tag_exprContext):
        self.file.write(f"<{ctx.MAIN_TAG()}>\n")
        self.visitChildren(ctx)
        self.file.write(f"</{ctx.MAIN_TAG()}>\n")

    # Visit a parse tree produced by RhtmlParser#tag_expr.
    def visitTag_expr(self, ctx: RhtmlParser.Tag_exprContext):
        options = ""

        for option in ctx.tag_option_expr():
            result = self.visitTag_option_expr(option)
            options += f" {result[0]}={result[1]}"

        if ctx.DOUBLE_TAG() is not None:
            self.file.write("\t" * tabs(ctx) + f"<{ctx.DOUBLE_TAG()}{options}>\n")
            self.visitChildren(ctx)
            self.file.write("\t" * tabs(ctx) + f"</{ctx.DOUBLE_TAG()}>\n")
        else:
            self.file.write("\t" * tabs(ctx) + f"<{ctx.SINGLE_TAG()}{options}")
            self.file.write('>\n')

    # Visit a parse tree produced by RhtmlParser#tag_inside.
    def visitTag_inside(self, ctx: RhtmlParser.Tag_insideContext):
        if ctx.ITER() is not None:
            self.file.write("\t" * tabs(ctx) + f"{self.iter}\n")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RhtmlParser#tag_option_expr.
    @staticmethod
    def visitTag_option_expr(ctx: RhtmlParser.Tag_option_exprContext):
        return str(ctx.TAG_OPTION()).replace('!', ''), str(ctx.STRING())

    # Visit a parse tree produced by RhtmlParser#string_int_inside.
    def visitString_int_inside(self, ctx: RhtmlParser.String_int_insideContext):
        if ctx.STRING() is not None:
            result = str(ctx.STRING()).replace("\"", "")
        else:
            result = ctx.INT()

        self.file.write("\t" * tabs(ctx) + f"{result}\n")

    # Visit a parse tree produced by RhtmlParser#list.
    def visitList(self, ctx: RhtmlParser.ListContext):
        self.file.write("\t" * tabs(ctx) + f"<{ctx.LIST()}>\n")
        self.visitChildren(ctx)
        self.file.write("\t" * tabs(ctx) + f"</{ctx.LIST()}>\n")

        # Visit a parse tree produced by RhtmlParser#list_inside.
    def visitList_inside(self, ctx: RhtmlParser.List_insideContext):
        self.file.write("\t" * tabs(ctx) + f"<{ctx.LIST_ITEM()}>")
        if ctx.string_int_inside() is not None:
            self.visitChildren(ctx)
        else:
            self.file.write(self.iter)
        self.file.write(f"</{ctx.LIST_ITEM()}>\n")


del RhtmlParser
