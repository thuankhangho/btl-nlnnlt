# Student ID: 2011357
# Name: Ho Thuan Khang

from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    #decllist EOF;
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    # decllist: classdecl decllist | ;
    def visitDecllist(self, ctx:CSlangParser.DecllistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.classdecl())] + self.visit(ctx.decllist())

    # classdecl: CLASS (superpart | ) ID LCB memberlist RCB;
    def visitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        if ctx.superpart():
            return ClassDecl(Id(ctx.ID().getText()), self.visit(ctx.memberlist()), self.visit(ctx.superpart()))
        return ClassDecl(Id(ctx.ID().getText()), self.visit(ctx.memberlist()))
    
    # member memberlist | ;
    def visitMemberlist(self, ctx:CSlangParser.MemberlistContext):
        if ctx.getChildCount() == 0:
            return []
        res = []
        for x in self.visit(ctx.member()):
            res = res + [x]
        return res + self.visit(ctx.memberlist())
    
    # attributedecl | methoddecl;
    def visitMember(self, ctx:CSlangParser.MemberContext):
        if ctx.attributedecl():
            res = []
            for x in self.visit(ctx.attributedecl()):
                res = res + [AttributeDecl(x)]
            return res
        return [self.visit(ctx.methoddecl())]
    
    # vardecl | constdecl;
    def visitAttributedecl(self, ctx:CSlangParser.AttributedeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.constdecl())
    
    # VAR attributecheck SM;
    def visitVardecl(self, ctx:CSlangParser.VardeclContext):
        res = []
        for x, y, z in self.visit(ctx.attributecheck()):
            res = res + [VarDecl(x, y, z)]
        # print(res)
        return res
    
    # CONST attributecheck SM;
    def visitConstdecl(self, ctx:CSlangParser.ConstdeclContext):
        res = []
        for x, y, z in self.visit(ctx.attributecheck()):
            res = res + [ConstDecl(x, y, z)]
        return res

    # attributewithdeclare | attributenodeclare;
    def visitAttributecheck(self, ctx:CSlangParser.AttributecheckContext):
        if ctx.attributenodeclare():
            attributedecl = self.visit(ctx.attributenodeclare())
            res = []
            for x in attributedecl:
                res = res + [(x[0],x[1],None)]
            return res
        attributedecl = self.visit(ctx.attributewithdeclare())
        res = []
        for x in attributedecl:
            res = res + [(x[0],x[2],x[1])]
        return res

    # attributelist COLON typedecl SM;
    def visitAttributenodeclare(self, ctx:CSlangParser.AttributenodeclareContext):
        # if len(self.visit(ctx.attributelist())) == 1:
        #     return [(self.visit(ctx.attributelist())[0],self.visit(ctx.typedecl()))]
        res = []
        for x in self.visit(ctx.attributelist()):
            res.append((x,self.visit(ctx.typedecl())))
        # print(res)
        return res

    # identifier CM attributelist | identifier;
    def visitAttributelist(self, ctx:CSlangParser.AttributelistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.identifier())]
        return [self.visit(ctx.identifier())] + self.visit(ctx.attributelist())
    
##################################################################################################################################
    
    # attlist;
    def visitAttributewithdeclare(self, ctx:CSlangParser.AttributewithdeclareContext):
        attlist = self.visit(ctx.attlist())
        type = attlist[-1]
        attlist = attlist[0:len(attlist) - 1]
        attribute = []
        value = []
        for x in attlist:
            attribute = attribute + [x[0]]
            value = value + [x[1]]
        value.reverse()

        res = []
        for (x, y) in zip(attribute, value):
            res = res + [(x, y, type)]
        return res
    
    # identifier CM attlist CM exp | identifier COLON typedecl DECLARE exp;
    def visitAttlist(self, ctx:CSlangParser.AttlistContext):
        if ctx.typedecl():
            return [(self.visit(ctx.identifier()), self.visit(ctx.exp()))] + [self.visit(ctx.typedecl())]
        return [(self.visit(ctx.identifier()), self.visit(ctx.exp()))] + (self.visit(ctx.attlist()))
        
##################################################################################################################################
   
    # constructor | FUNC identifier LRB parameterlist RRB COLON typedeclwithvoid blockstate;
    def visitMethoddecl(self, ctx:CSlangParser.MethoddeclContext):
        if ctx.constructor():
            return self.visit(ctx.constructor())
        return MethodDecl(self.visit(ctx.identifier()), self.visit(ctx.parameterlist()), self.visit(ctx.typedeclwithvoid()), self.visit(ctx.blockstate()))
    
    # FUNC CONSTRUCTOR LRB parameterlist RRB blockstate;
    def visitConstructor(self, ctx:CSlangParser.ConstructorContext):
        return MethodDecl(Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.parameterlist()), VoidType(), self.visit(ctx.blockstate()))

    # typ | arraydecl | VOID;
    def visitTypedeclwithvoid(self, ctx:CSlangParser.TypedeclwithvoidContext):
        if ctx.typ():
            return self.visit(ctx.typ())
        elif ctx.arraydecl():
            return self.visit(ctx.arraydecl())
        return VoidType()

    # parameterprime | ;
    def visitParameterlist(self, ctx:CSlangParser.ParameterlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.parameterprime())
    
    # parameterpart1 | parameterpart2;
    def visitParameterprime(self, ctx:CSlangParser.ParameterprimeContext):
        if ctx.parameterpart1():
            return self.visit(ctx.parameterpart1())
        param2 = self.visit(ctx.parameterpart2())
        typ = None
        res = []
        for a in param2:
            if type(a) is not list:
                typ = a
            else:
                for b in a:
                    res = res + [VarDecl(b,typ)]
        return res
    
    # (ID COLON typ) CM parameterpart1 | (ID COLON typ);
    def visitParameterpart1(self, ctx:CSlangParser.Parameterpart1Context):
        if ctx.getChildCount() == 5:
            return [VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()))] + self.visit(ctx.parameterpart1())
        return [VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()))]
    
    # identifierlist COLON typ CM parameterpart2 | identifierlist COLON typ;
    def visitParameterpart2(self, ctx:CSlangParser.Parameterpart2Context):
        if ctx.getChildCount() == 5:
            return [self.visit(ctx.typ())] + [self.visit(ctx.identifierlist())] + self.visit(ctx.parameterpart2())
        return [self.visit(ctx.typ())] + [self.visit(ctx.identifierlist())] 
    
    # ID CM identifierlist | ID;
    def visitIdentifierlist(self, ctx:CSlangParser.IdentifierlistContext):
        if ctx.identifierlist():
            return [Id(ctx.ID().getText())] + self.visit(ctx.identifierlist())
        return [Id(ctx.ID().getText())]
    
##################################################################################################################################
    
    # exp1 CONCAT exp1 | exp1;
    def visitExp(self, ctx:CSlangParser.ExpContext):
        if ctx.CONCAT():
            return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.exp1()[0]), self.visit(ctx.exp1()[1]))
        return self.visit(ctx.exp1()[0])
    
    # exp2 relational exp2 | exp2;
    def visitExp1(self, ctx:CSlangParser.Exp1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.relational()), self.visit(ctx.exp2()[0]),self.visit(ctx.exp2()[1]))
        return self.visit(ctx.exp2()[0])
    
    # exp2 logical exp3 | exp3;
    def visitExp2(self, ctx:CSlangParser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.logical()), self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        return self.visit(ctx.exp3())
    
    # exp3 adding exp4 | exp4;
    def visitExp3(self, ctx:CSlangParser.Exp3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.adding()), self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        return self.visit(ctx.exp4())
    
    # exp4 multiplying exp5 | exp5;
    def visitExp4(self, ctx:CSlangParser.Exp4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.multiplying()), self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        return self.visit(ctx.exp5())
    
    # DIFF exp5 | exp6;
    def visitExp5(self, ctx:CSlangParser.Exp5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.DIFF().getText(), self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())
    
    # MINUS exp6 | exp7;
    def visitExp6(self, ctx:CSlangParser.Exp6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.MINUS().getText(), self.visit(ctx.exp6()))
        return self.visit(ctx.exp7())
    
    # exp8 LSB exp RSB | exp8;
    def visitExp7(self, ctx:CSlangParser.Exp7Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp()))
        return self.visit(ctx.exp8())
    
    # exp8 (LSB exp RSB | ) DOT ID (LRB nullableexplist RRB | ) | exp9;
    def visitExp8(self, ctx:CSlangParser.Exp8Context):
        if ctx.getChildCount() == 9: # exp8 LSB exp RSB DOT ID LRB nullableexplist RRB
            return CallExpr(ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp())), Id(ctx.ID().getText()), self.visit(ctx.nullableexplist()))
        elif ctx.getChildCount() == 6:
            if ctx.nullableexplist(): # exp8 DOT ID LRB nullableexplist RRB
                return CallExpr(self.visit(ctx.exp8()), Id(ctx.ID().getText()), self.visit(ctx.nullableexplist()))
            return FieldAccess(ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp())), Id(ctx.ID().getText())) # exp8 LSB exp RSB DOT ID
        elif ctx.getChildCount() == 3: # exp8 DOT ID
            return FieldAccess(self.visit(ctx.exp8()), Id(ctx.ID().getText()))
        return self.visit(ctx.exp9())
    
    # (ID DOT | ) ATIDENTIFIER (LRB nullableexplist RRB | ) | exp10;
    def visitExp9(self, ctx:CSlangParser.Exp9Context):
        if ctx.getChildCount() == 6: # ID DOT ATIDENTIFIER LRB nullableexplist RRB
            return CallExpr(Id(ctx.ID().getText()), Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.nullableexplist()))
        elif ctx.getChildCount() == 4: #ATIDENTIFIER LRB nullableexplist RRB
            return CallExpr(None, Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.nullableexplist()))
        elif ctx.getChildCount() == 3: # ID DOT ATIDENTIFIER
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.ATIDENTIFIER().getText()))
        elif ctx.ATIDENTIFIER(): # ATIDENTIFIER
            return FieldAccess(None,Id(ctx.ATIDENTIFIER().getText()))
        elif ctx.exp10():
            return self.visit(ctx.exp10())

    # NEW ID LRB nullableexplist RRB | exp11; 
    def visitExp10(self, ctx:CSlangParser.Exp10Context):
        if ctx.ID():
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.nullableexplist()))
        return self.visit(ctx.exp11())
    
    # LRB exp RRB | exp12;
    def visitExp11(self, ctx:CSlangParser.Exp11Context):
        if ctx.exp():
            return self.visit(ctx.exp())
        return self.visit(ctx.exp12())
    
    #literal | identifier | SELF | NULL | createobjectexpr;
    def visitExp12(self, ctx:CSlangParser.Exp12Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.identifier():
            return self.visit(ctx.identifier())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL(): 
            return NullLiteral()
        return self.visit(ctx.createobjectexpr())
    
    # expprime |;
    def visitNullableexplist(self, ctx:CSlangParser.NullableexplistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.expprime())
    
    # exp CM expprime | exp;
    def visitExpprime(self, ctx:CSlangParser.ExpprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.expprime())

    # EQ | NEQ | LE | GE | LEQ | GEQ;
    def visitRelational(self, ctx:CSlangParser.RelationalContext):
        if ctx.EQ():
            return ctx.EQ().getText()
        elif ctx.NEQ():
            return ctx.NEQ().getText()
        elif ctx.LE():
            return ctx.LE().getText()
        elif ctx.GE():
            return ctx.GE().getText()
        elif ctx.LEQ():
            return ctx.LEQ().getText()
        return ctx.GEQ().getText()
    
    # AND | OR;
    def visitLogical(self, ctx:CSlangParser.LogicalContext):
        if ctx.AND():
            return ctx.AND().getText()
        return ctx.OR().getText()
    
    # PLUS | MINUS;
    def visitAdding(self, ctx:CSlangParser.AddingContext):
        if ctx.PLUS():
            return ctx.PLUS().getText()
        return ctx.MINUS().getText()
    
    # MULTIPLY | DIVIDE_FLOAT | DIVIDE_INT | MOD;
    def visitMultiplying(self, ctx:CSlangParser.MultiplyingContext):
        if ctx.MULTIPLY():
            return ctx.MULTIPLY().getText()
        elif ctx.DIVIDE_FLOAT():
            return ctx.DIVIDE_FLOAT().getText()
        elif ctx.DIVIDE_INT():
            return ctx.DIVIDE_INT().getText()
        return ctx.MOD().getText()
        
##################################################################################################################################
    
    # attributedecl SM;
    def visitDeclrstate(self, ctx:CSlangParser.DeclrstateContext):
        return self.visit(ctx.attributedecl())
    
    # exp ASSIGN exp SM;
    def visitAssignstate(self, ctx:CSlangParser.AssignstateContext):
        return Assign(self.visit(ctx.exp()[0]), self.visit(ctx.exp()[1]))
    
    # stmt stmtlist | ;
    def visitStmtlist(self, ctx:CSlangParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        if (type(self.visit(ctx.stmt()))) is list:
            return self.visit(ctx.stmt()) + self.visit(ctx.stmtlist())
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
    
    # stmt: attributedecl | assignstate | ifstate | forstate | breakstate | continuestate
    # | returnstate | methodinvoke | blockstate
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        if ctx.attributedecl():
            return self.visit(ctx.attributedecl())
        elif ctx.assignstate():
            return self.visit(ctx.assignstate())
        elif ctx.ifstate():
            return self.visit(ctx.ifstate())
        elif ctx.forstate():
            return self.visit(ctx.forstate())
        elif ctx.breakstate():
            return self.visit(ctx.breakstate())
        elif ctx.continuestate():
            return self.visit(ctx.continuestate())
        elif ctx.returnstate():
            return self.visit(ctx.returnstate())
        elif ctx.methodinvoke():
            return self.visit(ctx.methodinvoke())
        return self.visit(ctx.blockstate())

    # CONTINUE SM;
    def visitContinuestate(self, ctx:CSlangParser.ContinuestateContext):
        return Continue()
    
    # BREAK SM;
    def visitBreakstate(self, ctx:CSlangParser.BreakstateContext):
        return Break()
    
    # RETURN (exp | ) SM;
    def visitReturnstate(self, ctx:CSlangParser.ReturnstateContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return(None)
    
    # LCB stmtlist RCB;
    def visitBlockstate(self, ctx:CSlangParser.BlockstateContext):
        return Block(self.visit(ctx.stmtlist()))
    
    # IF (blockstate | ) exp blockstate (ELSE blockstate | );
    def visitIfstate(self,ctx:CSlangParser.IfstateContext):
        if ctx.getChildCount() == 3:
            return If(self.visit(ctx.exp()), self.visit(ctx.blockstate()[0]))
        elif ctx.getChildCount() == 4:
            return If(self.visit(ctx.exp()), self.visit(ctx.blockstate()[1]), self.visit(ctx.blockstate()[0]))
        elif ctx.getChildCount() == 5:
            return If(self.visit(ctx.exp()), self.visit(ctx.blockstate()[0]), None, self.visit(ctx.blockstate()[1]))
        else:
            return If(self.visit(ctx.exp()), self.visit(ctx.blockstate()[1]), self.visit(ctx.blockstate()[0]), self.visit(ctx.blockstate()[2]))

    # FOR assignstate exp SM exp ASSIGN exp blockstate;
    def visitForstate(self,ctx:CSlangParser.ForstateContext):
        return For(self.visit(ctx.assignstate()), self.visit(ctx.exp()[0]), Assign(self.visit(ctx.exp()[1]),self.visit(ctx.exp()[1])), self.visit(ctx.blockstate()))

    # (instancemethodstate | staticmethodstate) SM;
    def visitMethodinvoke(self, ctx:CSlangParser.MethodinvokeContext):
        if ctx.instancemethodstate():
            return self.visit(ctx.instancemethodstate())
        else:
            return self.visit(ctx.staticmethodstate())
    
    # exp DOT ID LRB nullableexplist RRB;
    def visitInstancemethodstate(self, ctx:CSlangParser.InstancemethodstateContext):
        return CallStmt(self.visit(ctx.exp()), Id(ctx.ID().getText()), self.visit(ctx.nullableexplist()))
    
    # (ID DOT | ) ATIDENTIFIER LRB nullableexplist RRB;
    def visitStaticmethodstate(self, ctx:CSlangParser.StaticmethodstateContext):
        if ctx.getChildCount() == 6:
            return CallStmt(Id(ctx.ID().getText()), Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.nullableexplist()))
        return CallStmt(None, Id(ctx.ATIDENTIFIER().getText()), self.visit(ctx.nullableexplist()))

##################################################################################################################################
    
    # typ | arraydecl;
    def visitTypedecl(self, ctx:CSlangParser.TypedeclContext):
        return self.visit(ctx.typ()) if ctx.typ() else self.visit(ctx.arraydecl())

    # LSB INTLIT RSB typ;
    def visitArraydecl(self, ctx:CSlangParser.ArraydeclContext):
        return ArrayType(int(ctx.INTLIT().getText()), self.visit(ctx.typ()))
    
    # BOOL | INT | FLOAT | STRING | ID | arraydecl;
    def visitTyp(self, ctx:CSlangParser.TypContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.arraydecl():
            return self.visit(ctx.arraydecl())
        return ClassType(Id(ctx.ID().getText()))

    # ID | ATIDENTIFIER;
    def visitIdentifier(self, ctx:CSlangParser.IdentifierContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return Id(ctx.ATIDENTIFIER().getText())
    
    # LSB literallist RSB;
    def visitArraylit(self, ctx:CSlangParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.literallist()))

    # literalnoarray: INTLIT | FLOATLIT | boolit | STRINGLIT  | SELF | NULL;
    def visitLiteralnoarray(self, ctx:CSlangParser.LiteralnoarrayContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.boolit():
            return BooleanLiteral(self.visit(ctx.boolit()))
        elif ctx.NULL():
            return NullLiteral()
        return SelfLiteral()

    # literalnoarray CM literallist | literalnoarray;
    def visitLiterallist(self, ctx:CSlangParser.LiterallistContext):
        if ctx.literallist():
            return [self.visit(ctx.literalnoarray())] + self.visit(ctx.literallist())
        return [self.visit(ctx.literalnoarray())]

    # INTLIT | FLOATLIT | boolit | STRINGLIT | arraylit | NULL | SELF;
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.boolit():
            return BooleanLiteral(self.visit(ctx.boolit()))
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        return SelfLiteral()
    
    # ID '<-';
    def visitSuperpart(self, ctx:CSlangParser.SuperpartContext):
        return Id(ctx.ID().getText())
    
    # TRUE | FALSE;
    def visitBoolit(self, ctx:CSlangParser.BoolitContext):
        if ctx.TRUE():
            return True
        return False