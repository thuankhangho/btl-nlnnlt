from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *
from functools import reduce

### Chưa xong Declaring Attribute (List in List)

class ASTGeneration(CSlangVisitor):
    ### Functions
    def flatten(self, lst):
        return reduce(lambda prev, curr: prev + curr, lst, [])

    ### AST Gen No Visiting Other Grammars
    def visitSuperpart(self,ctx:CSlangParser.SuperpartContext):
        return Id(ctx.IDENTIFIER().getText())

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
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.IDENTIFIER():
            return ClassType(Id(ctx.IDENTIFIER().getText()))
        
    def visitArrayType(self,ctx:CSlangParser.ArrayTypeContext):
        if ctx.INT():
            return ArrayType(IntLiteral(ctx.INTLIT().getText()), IntType())
        elif ctx.FLOAT():
            return ArrayType(IntLiteral(ctx.INTLIT().getText()), FloatType())
        elif ctx.BOOL():
            return ArrayType(IntLiteral(ctx.INTLIT().getText()), BoolType())
        elif ctx.STRING():
            return ArrayType(IntLiteral(ctx.INTLIT().getText()), StringType())
        elif ctx.IDENTIFIER():
            return ArrayType(IntLiteral(ctx.INTLIT().getText()), ClassType(Id(ctx.IDENTIFIER().getText())))
        
    def visitHder(self,ctx:CSlangParser.HderContext):
        if ctx.CONST():
            return ctx.CONST().getText()
        elif ctx.VAR():
            return ctx.VAR().getText()
    
    ### AST Gen Literals
    def visitBoolit(self,ctx:CSlangParser.BoolitContext):
        if ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
    
    def visitArray(self,ctx:CSlangParser.ArrayContext):
        return ArrayLiteral(self.visit(ctx.litlist()))
    
    def visitLitlist(self,ctx:CSlangParser.LitlistContext):
        if ctx.getChildCount==1:
            return [self.visit(ctx.lits)]
        else:
            return [self.visit(ctx.lits)] + self.visit(ctx.litlist())
        
    def visitLits(self,ctx:CSlangParser.LitsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.boolit():
            return BooleanLiteral(self.visit(ctx.boolit()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.iden():
            return Id(self.visit(ctx.iden()))
    
    ### AST Gen start of Program    
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
        return [self.visit(ctx.methd())]
    
    ### AST Gen of Attributes
    def visitAttr(self,ctx:CSlangParser.AttrContext):
        if ctx.attrndc():
            return self.visit(ctx.attrndc())
        else:
            return self.visit(ctx.attrdc())
        
    def visitAttrdc(self,ctx:CSlangParser.AttrdcContext):
        idenlist = self.visit(ctx.attlist())
        # print(idenlist, "A")
        # return idenlist
        # res = []
        # if self.visit(ctx.hder()) == "const":
        #     for x in idenlist:
        #         res.append(ConstDecl(Id(x), self.visit(ctx.typ()), None))
        # elif self.visit(ctx.hder()) == "var":
        #     for x in idenlist:
        #         res.append(VarDecl(Id(x), self.visit(ctx.typ())))
        # return res
        typp = idenlist[-1]
        idenlist = idenlist[0:len(idenlist)-1]
        attrbute = []
        val = []
        for x in idenlist:
            attrbute.append(x[0])
            val.append(x[1])
        val.reverse()
        res = []
        if self.visit(ctx.hder()) == "const":
            for (x, y) in zip(attrbute, val):
                res.append(ConstDecl(x, typp, y))
        elif self.visit(ctx.hder()) == "var":
            for (x, y) in zip(attrbute, val):
                res.append(VarDecl(x, typp, y))
        return res
    
    def visitAttlist(self,ctx:CSlangParser.AttlistContext):
        if ctx.typ():
            return [(Id(self.visit(ctx.iden())),self.visit(ctx.expr()))] + [self.visit(ctx.typ())]
        else:
            return [(Id(self.visit(ctx.iden())),self.visit(ctx.expr()))] + self.visit(ctx.attlist())
        
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
        
    ### AST Gen of Methods
    def visitMethd(self,ctx:CSlangParser.MethdContext):
        if ctx.funct():
            return self.visit(ctx.funct())
        else:
            return self.visit(ctx.functcons())
        
    def visitFunctcons(self,ctx:CSlangParser.FunctconsContext):
        return MethodDecl(Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.paramlist()), VoidType(), self.visit(ctx.blkstate()))

    def visitFunct(self,ctx:CSlangParser.FunctContext):
        if ctx.typ():
            return MethodDecl(Id(self.visit(ctx.iden())), self.visit(ctx.paramlist()), self.visit(ctx.typ()), self.visit(ctx.blkstate()))
        else:
            return MethodDecl(Id(self.visit(ctx.iden())), self.visit(ctx.paramlist()), VoidType(), self.visit(ctx.blkstate()))
    
        ### AST Gen of Params
    def visitParamlist(self,ctx:CSlangParser.ParamlistContext):
        if ctx.getChildCount()==0:
            return []
        else:
            return self.visit(ctx.paramprime())
        
    def visitParamprime(self,ctx:CSlangParser.ParamprimeContext):
        if ctx.param1():
            return self.visit(ctx.param1())
        else:
            par = self.visit(ctx.param2())
            typ = None
            res = []        
            for x in par:
                if type(x) is not list:
                    typ = x
                else:
                    for y in x:
                        res.append(VarDecl(y,typ))
            return res

    def visitParam1(self,ctx:CSlangParser.Param1Context):
        if ctx.param1():
            return [VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()))] + self.visit(ctx.param1())
        else:
            return [VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ()))]
     
    def visitParam2(self,ctx:CSlangParser.Param2Context):
        if ctx.getChildCount()==3:
            return [self.visit(ctx.typ())] + [self.visit(ctx.idenNoAtlist())]
        else:
            return [self.visit(ctx.typ())] + [self.visit(ctx.idenNoAtlist())] + self.visit(ctx.param2())
        
    def visitIdenNoAtlist(self,ctx:CSlangParser.IdenNoAtlistContext):
        if ctx.idenNoAtlist():
            return [Id(ctx.IDENTIFIER().getText())] + self.visit(ctx.idenNoAtlist())
        else:
            return [Id(ctx.IDENTIFIER().getText())]
        
        ### AST Gen of Blockstates
    def visitBlkstate(self,ctx:CSlangParser.BlkstateContext):
        return Block(self.visit(ctx.stmtlist()))
    
    def visitStmtlist(self,ctx:CSlangParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            if (type(self.visit(ctx.stmt()))) is list:
                return self.visit(ctx.stmt()) + self.visit(ctx.stmtlist())
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
        
    def visitStmt(self,ctx:CSlangParser.StmtContext):
        if ctx.declstmt():
            return self.visit(ctx.declstmt())
        elif ctx.assstmt():
            return self.visit(ctx.assstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.breakstmt(): #Done
            return self.visit(ctx.breakstmt())
        elif ctx.contstmt(): #Done
            return self.visit(ctx.contstmt())
        elif ctx.retstmt():
            return self.visit(ctx.retstmt())
        elif ctx.metdinvoke():
            return self.visit(ctx.metdinvoke())
        else:
            return self.visit(ctx.blkstate())
        
        ### AST Gen of Statements
    def visitBreakstmt(self,ctx:CSlangParser.BreakstmtContext):
        return Break()
    
    def visitContstmt(self,ctx:CSlangParser.ContstmtContext):
        return Continue()
    
    def visitRetstmt(self,ctx:CSlangParser.RetstmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)
        
    def visitDeclstmt(self,ctx:CSlangParser.DeclstmtContext): ### FIXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        if ctx.attrdc():
            return self.visit(ctx.attrdc())
        else:
            return self.visit(ctx.attrndc())
    
        ### Assign Stmt
    def visitAssstmt(self,ctx:CSlangParser.AssstmtContext):
        if ctx.assignNonS():
            return self.visit(ctx.assignNonS())
        else:
            return self.visit(ctx.assignS())
        
    def visitAssignS(self,ctx:CSlangParser.AssignSContext):
        return Assign(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()))
    
    def visitAssignNonS(self,ctx:CSlangParser.AssignNonSContext):
        return Assign(self.visit(ctx.leftNonS()), self.visit(ctx.expr()))
    
    def visitLeftNonS(self,ctx:CSlangParser.LeftNonSContext):
        if ctx.arrayNS():
            return self.visit(ctx.arrayNS())
        else:
            return self.visit(ctx.insAttr())
        
    def visitArrayNS(self,ctx:CSlangParser.ArrayNSContext):
        return ArrayCell(self.visit(ctx.expr8()), self.visit(ctx.expr()))
    
    def visitInsAttr(self,ctx:CSlangParser.InsAttrContext):
        if ctx.expr8():
            if ctx.expr():
                return FieldAccess(ArrayCell(self.visit(ctx.expr8()), self.visit(ctx.expr())), Id(ctx.IDENTIFIER().getText()))
            else:
                return FieldAccess(self.visit(ctx.expr8()), Id(ctx.IDENTIFIER().getText()))
        else:
            if ctx.IDENTIFIER():
                return FieldAccess(Id(ctx.IDENTIFIER().getText()), Id(ctx.ATIDENTIFIER().getText()))
            else:
                return FieldAccess(None, Id(ctx.ATIDENTIFIER().getText()))
            
        ### If Stmt
    def visitIfstmt(self,ctx:CSlangParser.IfstmtContext):
        if ctx.getChildCount()==3:
            return If(self.visit(ctx.expr()), self.visit(ctx.blkstate()[0]))
        elif ctx.getChildCount()==4:
            return If(self.visit(ctx.expr()), self.visit(ctx.blkstate()[1]), self.visit(ctx.blkstate()[0]))
        elif ctx.getChildCount()==5:
            return If(self.visit(ctx.expr()), self.visit(ctx.blkstate()[0]), None, self.visit(ctx.blkstate()[1]))
        else:
            return If(self.visit(ctx.expr()), self.visit(ctx.blkstate()[1]), self.visit(ctx.blkstate()[0]), self.visit(ctx.blkstate()[2]))
    
        ### For Stmt
    def visitInitstmt(self,ctx:CSlangParser.InitstmtContext):
        return Assign(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()))
    
    def visitForstmt(self,ctx:CSlangParser.ForstmtContext):
        return For(self.visit(ctx.initstmt()[0]), self.visit(ctx.expr()), self.visit(ctx.initstmt()[1]), self.visit(ctx.blkstate()))
    
        ### Method Invokes
    def visitMetdinvoke(self,ctx:CSlangParser.MetdinvokeContext):
        if ctx.invocInsStmt():
            return self.visit(ctx.invocInsStmt())
        else:
            return self.visit(ctx.invocStaticStmt())
        
    def visitInvocInsStmt(self,ctx:CSlangParser.InvocInsStmtContext):
        if ctx.expr():
            return CallStmt(ArrayCell(self.visit(ctx.expr8()), self.visit(ctx.expr())), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
        else:
            return CallStmt(self.visit(ctx.expr8()), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
    
    def visitInvocStaticStmt(self,ctx:CSlangParser.InvocStaticStmtContext):
        if ctx.IDENTIFIER():
            return CallStmt(Id(ctx.IDENTIFIER().getText()), Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.exprlist()))
        else:
            return CallStmt(None, Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.exprlist()))
        
        ### AST Gen of New Identifier
    def visitNew(self,ctx:CSlangParser.NewContext):  # NEW iden LB exprlist RB;
        return NewExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
    
    ### AST Gen of Expressions
    def visitExprlist(self,ctx:CSlangParser.ExprlistContext): # exprlist: exprlst | ;
        if ctx.getChildCount()==0:
            return []
        else:
            return self.visit(ctx.exprlst())
        
    def visitExprlst(self,ctx:CSlangParser.ExprlstContext): # exprlst: expr CM exprlst | expr;
        if ctx.exprlst():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprlst())
        else:
            return [self.visit(ctx.expr())]
        
    def visitExpr(self,ctx:CSlangParser.ExprContext): # expr1 SPACING expr1 | expr1
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr1()[0])
        else:
            return BinaryOp(ctx.SPACING().getText(), self.visit(ctx.expr1()[0]), self.visit(ctx.expr1()[1]))
        
    def visitExpr1(self,ctx:CSlangParser.Expr1Context): # expr2 operators expr2 | expr2
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr2()[0])
        else:
            return BinaryOp(self.visit(ctx.operators()), self.visit(ctx.expr2()[0]), self.visit(ctx.expr2()[1]))
        
    def visitExpr2(self,ctx:CSlangParser.Expr2Context): # expr2 logical expr3 | expr3
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr3())
        else:
            return BinaryOp(self.visit(ctx.logical()), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        
    def visitExpr3(self,ctx:CSlangParser.Expr3Context): # expr3 adding expr4 | expr4
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr4())
        else:
            return BinaryOp(self.visit(ctx.adding()), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        
    def visitExpr4(self,ctx:CSlangParser.Expr4Context): # expr4 multiplying expr5 | expr5
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr5())
        else:
            return BinaryOp(self.visit(ctx.multiplying()), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        
    def visitExpr5(self,ctx:CSlangParser.Expr5Context): # DIFF expr5 | expr6
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr6())
        else:
            return UnaryOp(ctx.DIFF().getText(), self.visit(ctx.expr5()))
        
    def visitExpr6(self,ctx:CSlangParser.Expr6Context): #MINUS expr6 | expr7
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr7())
        else:
            return UnaryOp(ctx.MINUS().getText(), self.visit(ctx.expr6()))
    
    def visitExpr7(self,ctx:CSlangParser.Expr7Context): # expr8 SLB expr SRB | expr8;
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr8())
        else:
            return ArrayCell(self.visit(ctx.expr8()), self.visit(ctx.expr()))
        
    def visitExpr8(self,ctx:CSlangParser.Expr8Context): # expr8 (SLB expr SRB)? DOT IDENTIFIER (LB exprlist RB)? | expr9;
        if ctx.getChildCount()==1:
            return self.visit(ctx.expr9())
        # FieldAccess(ArrayCell(),IDENTIFIER)
        # Call(ArrayCell,IDEN,exprlist)
        elif ctx.expr():
            if ctx.exprlist():
                return CallExpr(ArrayCell(self.visit(ctx.expr8()), self.visit(ctx.expr())), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
            else:
                return FieldAccess(ArrayCell(self.visit(ctx.expr8()), self.visit(ctx.expr())), Id(ctx.IDENTIFIER().getText()))
        else:
            if ctx.exprlist():
                return CallExpr(self.visit(ctx.expr8()), Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
            else:
                return FieldAccess(self.visit(ctx.expr8()), Id(ctx.IDENTIFIER().getText()))
    
    def visitExpr9(self,ctx:CSlangParser.Expr9Context): # (IDENTIFIER DOT)? ATIDENTIFIER | (IDENTIFIER DOT)? ATIDENTIFIER LB exprlist RB | expr10
        if ctx.expr10():
            return self.visit(ctx.expr10())
        elif ctx.exprlist():
            if ctx.getChildCount()==6:
                return CallExpr(Id(ctx.IDENTIFIER().getText()), Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.exprlist()))
            else:
                return CallExpr(None, Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.exprlist()))
        else:
            if ctx.getChildCount()==1:
                return FieldAccess(None, Id(ctx.ATIDENTIFIER().getText()))
            else:
                return FieldAccess(Id(ctx.IDENTIFIER().getText()), Id(ctx.ATIDENTIFIER().getText()))
            
    def visitExpr10(self,ctx:CSlangParser.Expr10Context):
        if ctx.new():
            return self.visit(ctx.new())
        else:
            return self.visit(ctx.expr11())
    
    def visitExpr11(self,ctx:CSlangParser.Expr11Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.expr12())
        
    def visitExpr12(self,ctx:CSlangParser.Expr12Context):
        if ctx.lits():
            return self.visit(ctx.lits())
        else:
            return self.visit(ctx.array())