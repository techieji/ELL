from lark import Lark

with open("gram.lark") as f:
    parser = Lark(f.read())

inp = "This is a series of words. This continues.\nDone."
print(inp)
print(parser.parse(inp).pretty())
