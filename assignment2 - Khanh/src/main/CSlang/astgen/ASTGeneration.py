from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *
from functools import reduce

class ASTGeneration(CSlangVisitor):
    
    def flatten(self, lst):
        return reduce(lambda prev, curr: prev + curr, lst, [])

    def visitSuperpart(self,ctx:CSlangParser.SuperpartContext):
        return Id(ctx.IDENTIFIER().getText())
    
    def visitBreakstmt(self,ctx:CSlangParser.BreakstmtContext):
        return Break()
    
    def visitContstmt(self,ctx:CSlangParser.ContstmtContext):
        return Continue()

    def visitOperators(self,ctx:CSlangParser.OperatorsContext):
        if ctx.COMPEQ():
            return ctx.COMPEQ().getText()
        elif ctx.DIFFROM():
            return ctx.DIFFROM().getText()
        elif ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.MOR():
            return ctx.MOR().getText()
        elif ctx.LESSEQ():
            return ctx.LESSEQ().getText()
        elif ctx.MOREEQ():
            return ctx.MOREEQ().getText()
        
    def visitLogical(self,ctx:CSlangParser.LogicalContext):
        if ctx.AND():
            return ctx.AND().getText()
        elif ctx.OR():
            return ctx.OR().getText()
        
    def visitAdding(self,ctx:CSlangParser.AddingContext):
        if ctx.PLUS():
            return ctx.PLUS().getText()
        elif ctx.MINUS():
            return ctx.MINUS().getText()
        
    def visitMultiplying(self,ctx:CSlangParser.MultiplyingContext):
        if ctx.MULTI():
            return ctx.MULTI().getText()
        elif ctx.DIVFLO():
            return ctx.DIVFLO().getText()
        elif ctx.DIVINT():
            return ctx.DIVINT().getText()
        elif ctx.MODU():
            return ctx.MODU().getText()
        
    def visitBoolit(self,ctx:CSlangParser.BoolitContext):
        if ctx.TRUE():
            return ctx.TRUE().getText()
        elif ctx.FALSE():
            return ctx.FALSE().getText()
        
    def visitIden(self,ctx:CSlangParser.IdenContext):
        if ctx.ATIDENTIFIER():
            return ctx.ATIDENTIFIER().getText()
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        
    def visitTyp(self,ctx:CSlangParser.TypContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        
    def visitHder(self,ctx:CSlangParser.HderContext):
        if ctx.CONST():
            return ctx.CONST().getText()
        elif ctx.VAR():
            return ctx.VAR().getText()
        
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program(self.visit(ctx.classi()))
    
    def visitClassi(self,ctx:CSlangParser.ClassiContext):
        if ctx.getChildCount() == 0:
            return []
        else: 
            return [self.visit(ctx.classdecl())] + self.visit(ctx.classi())

    def visitClassdecl(self,ctx:CSlangParser.ClassdeclContext):
        if ctx.superpart():
            return ClassDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.body()),self.visit(ctx.superpart()))
        else:
            return ClassDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.body()))
        
    def visitBody(self,ctx:CSlangParser.BodyContext):
        if ctx.getChildCount()==0:
            return []
        else:
            res = []
            for x in self.visit(ctx.member()):
                res = res + [x]
            return res + self.visit(ctx.body())

    def visitMember(self,ctx:CSlangParser.MemberContext):
        if ctx.attr():
            res = []
            for x in self.visit(ctx.attr()):
                res.append(AttributeDecl(x))
            return res
        return self.visit(ctx.methd())
        
    def visitAttr(self,ctx:CSlangParser.AttrContext):
        return self.visit(ctx.attrndc())#còn declare
        
    def visitAttrndc(self,ctx:CSlangParser.AttrndcContext):
        idenlist = self.visit(ctx.attrlist())
        # if len(idenlist) == 1:
        #     if self.visit(ctx.hder()) == "const":
        #         return [ConstDecl(Id(idenlist), self.visit(ctx.typ()), None)]
        #     return [VarDecl(Id(idenlist), self.visit(ctx.typ()))]
        res = []
        if self.visit(ctx.hder()) == "const":
            for x in idenlist:
                res.append(ConstDecl(Id(x), self.visit(ctx.typ()), None))
        elif self.visit(ctx.hder()) == "var":
            for x in idenlist:
                res.append(VarDecl(Id(x), self.visit(ctx.typ())))
        return res
    
    def visitAttrlist(self, ctx:CSlangParser.AttrlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.iden())]
        else:
            return [self.visit(ctx.iden())] + self.visit(ctx.attrlist())