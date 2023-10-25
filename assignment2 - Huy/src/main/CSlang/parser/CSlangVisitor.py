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


    # Visit a parse tree produced by CSlangParser#class_declarelist.
    def visitClass_declarelist(self, ctx:CSlangParser.Class_declarelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_declare.
    def visitClass_declare(self, ctx:CSlangParser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_member.
    def visitList_of_member(self, ctx:CSlangParser.List_of_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#member.
    def visitMember(self, ctx:CSlangParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute.
    def visitAttribute(self, ctx:CSlangParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributeconst.
    def visitAttributeconst(self, ctx:CSlangParser.AttributeconstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributevar.
    def visitAttributevar(self, ctx:CSlangParser.AttributevarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributedecl.
    def visitAttributedecl(self, ctx:CSlangParser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute1.
    def visitAttribute1(self, ctx:CSlangParser.Attribute1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_attribute.
    def visitList_of_attribute(self, ctx:CSlangParser.List_of_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute2.
    def visitAttribute2(self, ctx:CSlangParser.Attribute2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_a.
    def visitList_of_a(self, ctx:CSlangParser.List_of_aContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method.
    def visitMethod(self, ctx:CSlangParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_param.
    def visitList_of_param(self, ctx:CSlangParser.List_of_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_param1.
    def visitList_of_param1(self, ctx:CSlangParser.List_of_param1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#primee.
    def visitPrimee(self, ctx:CSlangParser.PrimeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param_declare.
    def visitParam_declare(self, ctx:CSlangParser.Param_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_param2.
    def visitList_of_param2(self, ctx:CSlangParser.List_of_param2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#primeme.
    def visitPrimeme(self, ctx:CSlangParser.PrimemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_identifier.
    def visitList_of_identifier(self, ctx:CSlangParser.List_of_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#primy.
    def visitPrimy(self, ctx:CSlangParser.PrimyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor.
    def visitConstructor(self, ctx:CSlangParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typee.
    def visitTypee(self, ctx:CSlangParser.TypeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typev.
    def visitTypev(self, ctx:CSlangParser.TypevContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arr_type.
    def visitArr_type(self, ctx:CSlangParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_type.
    def visitClass_type(self, ctx:CSlangParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typeorarrtype.
    def visitTypeorarrtype(self, ctx:CSlangParser.TypeorarrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_exp.
    def visitList_of_exp(self, ctx:CSlangParser.List_of_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#primu.
    def visitPrimu(self, ctx:CSlangParser.PrimuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp.
    def visitExp(self, ctx:CSlangParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp1.
    def visitExp1(self, ctx:CSlangParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp2.
    def visitExp2(self, ctx:CSlangParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp3.
    def visitExp3(self, ctx:CSlangParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp4.
    def visitExp4(self, ctx:CSlangParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp5.
    def visitExp5(self, ctx:CSlangParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp6.
    def visitExp6(self, ctx:CSlangParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp7.
    def visitExp7(self, ctx:CSlangParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp8.
    def visitExp8(self, ctx:CSlangParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp9.
    def visitExp9(self, ctx:CSlangParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp10.
    def visitExp10(self, ctx:CSlangParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp11.
    def visitExp11(self, ctx:CSlangParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp12.
    def visitExp12(self, ctx:CSlangParser.Exp12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#var_const_statement.
    def visitVar_const_statement(self, ctx:CSlangParser.Var_const_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ass_statement.
    def visitAss_statement(self, ctx:CSlangParser.Ass_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assex_statement.
    def visitAssex_statement(self, ctx:CSlangParser.Assex_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhs.
    def visitLhs(self, ctx:CSlangParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_statement.
    def visitIf_statement(self, ctx:CSlangParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_statement.
    def visitFor_statement(self, ctx:CSlangParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_statement.
    def visitBreak_statement(self, ctx:CSlangParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_statement.
    def visitContinue_statement(self, ctx:CSlangParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_statement.
    def visitReturn_statement(self, ctx:CSlangParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_invocation_statement.
    def visitMethod_invocation_statement(self, ctx:CSlangParser.Method_invocation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instance_method_invocation.
    def visitInstance_method_invocation(self, ctx:CSlangParser.Instance_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_method_invocation.
    def visitStatic_method_invocation(self, ctx:CSlangParser.Static_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_statement.
    def visitBlock_statement(self, ctx:CSlangParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_statement.
    def visitList_of_statement(self, ctx:CSlangParser.List_of_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#statement.
    def visitStatement(self, ctx:CSlangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#xdd.
    def visitXdd(self, ctx:CSlangParser.XddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#superX.
    def visitSuperX(self, ctx:CSlangParser.SuperXContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrlit.
    def visitArrlit(self, ctx:CSlangParser.ArrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arr.
    def visitArr(self, ctx:CSlangParser.ArrContext):
        return self.visitChildren(ctx)



del CSlangParser