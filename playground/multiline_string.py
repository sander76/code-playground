a = 10
triple_quote = f"""This
is a multiline {a}
string by triple quotes"""

bracket_quote = (
    "This is a very long "
    "multiline string of separate"
    "strings enclosed by\n"
    "brackets"
)

with_backslashes = "abc" "def" "and some more"
print(triple_quote)

print()
print(bracket_quote)
