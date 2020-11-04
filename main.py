from lark import Lark

with open("grammer.lark") as f:
    parser = Lark(f.read())

inp = "This is a series of words. This continues."
print(parser.parse(inp).pretty())