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


    # Visit a parse tree produced by CSlangParser#classdecl.
    def visitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#memberlist.
    def visitMemberlist(self, ctx:CSlangParser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#member.
    def visitMember(self, ctx:CSlangParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute.
    def visitAttribute(self, ctx:CSlangParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributenodeclare.
    def visitAttributenodeclare(self, ctx:CSlangParser.AttributenodeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributewithdeclare.
    def visitAttributewithdeclare(self, ctx:CSlangParser.AttributewithdeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#typ.
    def visitTyp(self, ctx:CSlangParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attlist.
    def visitAttlist(self, ctx:CSlangParser.AttlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributelist.
    def visitAttributelist(self, ctx:CSlangParser.AttributelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method.
    def visitMethod(self, ctx:CSlangParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameterlist.
    def visitParameterlist(self, ctx:CSlangParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameterprime.
    def visitParameterprime(self, ctx:CSlangParser.ParameterprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameterpart1.
    def visitParameterpart1(self, ctx:CSlangParser.Parameterpart1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameterpart2.
    def visitParameterpart2(self, ctx:CSlangParser.Parameterpart2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#identifierlist.
    def visitIdentifierlist(self, ctx:CSlangParser.IdentifierlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#identifierprime.
    def visitIdentifierprime(self, ctx:CSlangParser.IdentifierprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor.
    def visitConstructor(self, ctx:CSlangParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#superpart.
    def visitSuperpart(self, ctx:CSlangParser.SuperpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arraylit.
    def visitArraylit(self, ctx:CSlangParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literallist.
    def visitLiterallist(self, ctx:CSlangParser.LiterallistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arraydecl.
    def visitArraydecl(self, ctx:CSlangParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#objdecl.
    def visitObjdecl(self, ctx:CSlangParser.ObjdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#explist.
    def visitExplist(self, ctx:CSlangParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#nullableexplist.
    def visitNullableexplist(self, ctx:CSlangParser.NullableexplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expprime.
    def visitExpprime(self, ctx:CSlangParser.ExpprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#relational.
    def visitRelational(self, ctx:CSlangParser.RelationalContext):
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


    # Visit a parse tree produced by CSlangParser#varstate.
    def visitVarstate(self, ctx:CSlangParser.VarstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constate.
    def visitConstate(self, ctx:CSlangParser.ConstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignstate.
    def visitAssignstate(self, ctx:CSlangParser.AssignstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ifstate.
    def visitIfstate(self, ctx:CSlangParser.IfstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#forstate.
    def visitForstate(self, ctx:CSlangParser.ForstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#breakstate.
    def visitBreakstate(self, ctx:CSlangParser.BreakstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continuestate.
    def visitContinuestate(self, ctx:CSlangParser.ContinuestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#returnstate.
    def visitReturnstate(self, ctx:CSlangParser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instanceattributestate.
    def visitInstanceattributestate(self, ctx:CSlangParser.InstanceattributestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#staticattributestate.
    def visitStaticattributestate(self, ctx:CSlangParser.StaticattributestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instancemethodstate.
    def visitInstancemethodstate(self, ctx:CSlangParser.InstancemethodstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#staticmethodstate.
    def visitStaticmethodstate(self, ctx:CSlangParser.StaticmethodstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#blockstate.
    def visitBlockstate(self, ctx:CSlangParser.BlockstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmtlist.
    def visitStmtlist(self, ctx:CSlangParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#noatstmt.
    def visitNoatstmt(self, ctx:CSlangParser.NoatstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#noatstmtnodeclare.
    def visitNoatstmtnodeclare(self, ctx:CSlangParser.NoatstmtnodeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#noatstmtwithdeclare.
    def visitNoatstmtwithdeclare(self, ctx:CSlangParser.NoatstmtwithdeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attlist1.
    def visitAttlist1(self, ctx:CSlangParser.Attlist1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributelist1.
    def visitAttributelist1(self, ctx:CSlangParser.Attributelist1Context):
        return self.visitChildren(ctx)



del CSlangParser