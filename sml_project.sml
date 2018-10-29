datatype Variable = V of string;
type Integer_Constant = int;
type Boolean_Constant = bool;
datatype Arithmetic_Op = Plus | Minus | Times | Div;
datatype Relational_Op = Lt | Le | Eq | Ne | Ge | Gt;
datatype Boolean_Op = And | Or;
datatype Integer_Expression = IE1 of Integer_Constant
                            | IE2 of Variable
                            | IE3 of (Integer_Expression * Integer_Expression * Arithmetic_Op);

datatype Boolean_Expression = BE1 of Boolean_Constant
                            | BE2 of Variable
                            | BE3 of (Integer_Expression * Integer_Expression * Relational_Op)
                            | BE4 of (Boolean_Expression * Boolean_Expression * Boolean_Op);

datatype Expression = E1 of Integer_Expression
                    | E2 of Boolean_Expression;

datatype Instruction = Skip
                    | I1 of (Variable * Expression) (* Assignment *)
                    | I2 of (Instruction list) (* Compound *)
                    | I3 of (Boolean_Expression * Instruction * Instruction) (* Conditional *)
                    | I4 of (Boolean_Expression * Instruction); (* Loop *)

datatype Type = Boolean_Type | Integer_Type;
type Declaration = (Variable * Type);
type Declaration_List = Declaration list;
type Program = (Declaration_List * Instruction);

(* 1 *)
datatype ItypeRep = IntRep | BoolRep | NoDefRep;

(* 2 *)
type SymbolTable = (Variable * ItypeRep) list;

(* 3 *)
fun updatetablebyone (x:Variable, Integer_Type) ( tablebeforechange : SymbolTable) = 
					[ (x, IntRep)] @ tablebeforechange
					| updatetablebyone(x:Variable, Boolean_Type) (tablebeforechange:SymbolTable) = [(x, BoolRep)] @ tablebeforechange;

(* 4 *)
val rec CreateTable = (	  fn ([]) => ([]):SymbolTable

				|  ((declarationListHead :: declarationListTail): Declaration_List) => 
					updatetablebyone(declarationListHead)(CreateTable(declarationListTail))  
				
				);

(* 5 *)
fun SearchForVarType (x:Variable, []) = NoDefRep
  | SearchForVarType (x:Variable, ((y:Variable, z:ItypeRep)::symbolTableTail)) =
    if x = y
	then z
	else SearchForVarType(x, symbolTableTail); 


(6) VarNotInDecList: Declaration_List => Variable => Bool
Validate Variable is not in Declaration_List.
*)
fun VarNotInDecList ([]) = ( fn (z:Variable) => true )
  | VarNotInDecList (((x:Variable, y:Type)::declarationListTail):Declaration_List) =
    ( fn (z:Variable) => (x <> z) andalso VarNotInDecList(declarationListTail)(z) );


(*
(7) VDecList: Declaration_List => Bool
Validate Declaration_List.
*** Testing Required
*)
val rec VDecList = (
fn ([]) => true
 | (((x:Variable, y:Type)::declarationListTail):Declaration_List) =>
   VDecList(declarationListTail) andalso VarNotInDecList(declarationListTail)(x) );










