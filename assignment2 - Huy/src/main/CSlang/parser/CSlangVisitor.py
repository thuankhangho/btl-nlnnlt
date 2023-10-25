# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classi.
    def visitClassi(self, ctx:CSlangParser.ClassiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classdecl.
    def visitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#body.
    def visitBody(self, ctx:CSlangParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#member.
    def visitMember(self, ctx:CSlangParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#hder.
    def visitHder(self, ctx:CSlangParser.HderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attr.
    def visitAttr(self, ctx:CSlangParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attrdc.
    def visitAttrdc(self, ctx:CSlangParser.AttrdcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attrndc.
    def visitAttrndc(self, ctx:CSlangParser.AttrndcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attrlist.
    def visitAttrlist(self, ctx:CSlangParser.AttrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attlist.
    def visitAttlist(self, ctx:CSlangParser.AttlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typ.
    def visitTyp(self, ctx:CSlangParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#idenNoAtlist.
    def visitIdenNoAtlist(self, ctx:CSlangParser.IdenNoAtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#iden.
    def visitIden(self, ctx:CSlangParser.IdenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#methd.
    def visitMethd(self, ctx:CSlangParser.MethdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#funct.
    def visitFunct(self, ctx:CSlangParser.FunctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#functcons.
    def visitFunctcons(self, ctx:CSlangParser.FunctconsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramlist.
    def visitParamlist(self, ctx:CSlangParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramprime.
    def visitParamprime(self, ctx:CSlangParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param1.
    def visitParam1(self, ctx:CSlangParser.Param1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param2.
    def visitParam2(self, ctx:CSlangParser.Param2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#boolit.
    def visitBoolit(self, ctx:CSlangParser.BoolitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lits.
    def visitLits(self, ctx:CSlangParser.LitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array.
    def visitArray(self, ctx:CSlangParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arraylist.
    def visitArraylist(self, ctx:CSlangParser.ArraylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operators.
    def visitOperators(self, ctx:CSlangParser.OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#logical.
    def visitLogical(self, ctx:CSlangParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#adding.
    def visitAdding(self, ctx:CSlangParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#multiplying.
    def visitMultiplying(self, ctx:CSlangParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr11.
    def visitExpr11(self, ctx:CSlangParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr12.
    def visitExpr12(self, ctx:CSlangParser.Expr12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#new.
    def visitNew(self, ctx:CSlangParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprlist.
    def visitExprlist(self, ctx:CSlangParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprlst.
    def visitExprlst(self, ctx:CSlangParser.ExprlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#blkstate.
    def visitBlkstate(self, ctx:CSlangParser.BlkstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmtlist.
    def visitStmtlist(self, ctx:CSlangParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#declstmt.
    def visitDeclstmt(self, ctx:CSlangParser.DeclstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assstmt.
    def visitAssstmt(self, ctx:CSlangParser.AssstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ifstmt.
    def visitIfstmt(self, ctx:CSlangParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#initstmt.
    def visitInitstmt(self, ctx:CSlangParser.InitstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#condstmt.
    def visitCondstmt(self, ctx:CSlangParser.CondstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#poststmt.
    def visitPoststmt(self, ctx:CSlangParser.PoststmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#forstmt.
    def visitForstmt(self, ctx:CSlangParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#breakstmt.
    def visitBreakstmt(self, ctx:CSlangParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#contstmt.
    def visitContstmt(self, ctx:CSlangParser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#retstmt.
    def visitRetstmt(self, ctx:CSlangParser.RetstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#metdinvoke.
    def visitMetdinvoke(self, ctx:CSlangParser.MetdinvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#superpart.
    def visitSuperpart(self, ctx:CSlangParser.SuperpartContext):
        return self.visitChildren(ctx)



del CSlangParser