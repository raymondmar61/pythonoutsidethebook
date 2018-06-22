#Sources:  https://pymotw.com/3/textwrap/, https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/
import textwrap
sampletext = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
print(sampletext)
'''print

    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.

'''

#The fill() function takes text as input and produces formatted text as output.
print(textwrap.fill(sampletext, width=50))
'''print
     The textwrap module can be used to format
text for output in     situations where pretty-
printing is desired.  It offers     programmatic
functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

#dedent() removes whitespace prefix for all lines, embedded tabs, and extra spaces mixed into the middle.  However, if one line is indented more than another, some of the whitespace are not removed.
dendentedtext = textwrap.dedent(sampletext)
print(dendentedtext)
'''print

The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.

'''
dendentedtext = textwrap.dedent(sampletext).strip()
print(dendentedtext)
'''print
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''
dendentedtext = textwrap.dedent(sampletext).strip()
print(textwrap.fill(dendentedtext, width=45))
'''print
The textwrap module can be used to format
text for output in situations where pretty-
printing is desired.  It offers programmatic
functionality similar to the paragraph
wrapping or filling features found in many
text editors.
'''
dendentedtext = textwrap.dedent(sampletext).strip()
print(textwrap.fill(dendentedtext, width=60))
'''print
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

#indent() function add consistent prefix text to all the lines
print(textwrap.indent(sampletext, '> '))
'''print

>     The textwrap module can be used to format text for output in
>     situations where pretty-printing is desired.  It offers
>     programmatic functionality similar to the paragraph wrapping
>     or filling features found in many text editors.

'''
dendentedtext = textwrap.dedent(sampletext).strip()
print(textwrap.indent(dendentedtext, '> '))
'''print
> The textwrap module can be used to format text for output in
> situations where pretty-printing is desired.  It offers
> programmatic functionality similar to the paragraph wrapping
> or filling features found in many text editors.
'''
dendentedtext = textwrap.dedent(sampletext).strip()
width50 = textwrap.fill(dendentedtext, width=50)
print(textwrap.indent(width50, '> '))
'''print
> The textwrap module can be used to format text for
> output in situations where pretty-printing is
> desired.  It offers programmatic functionality
> similar to the paragraph wrapping or filling
> features found in many text editors.
'''

#control which lines receive the new prefix, pass a callable as the predicate argument to indent().  The callable is invoked for each line of text in turn and the prefix is added for lines where the return value is true.  The prefix 'even line' is added to lines containing an even number of characters.
def indentevencharacterlines(line):
	print("Indent {!r}?".format(line))
	return len(line.strip()) % 2 == 0
dendentedtext = textwrap.dedent(sampletext).strip()
width50 = textwrap.fill(dendentedtext, width=50)
print(textwrap.indent(width50, 'even line ', predicate=indentevencharacterlines))
'''print
Indent 'The textwrap module can be used to format text for\n'?
Indent 'output in situations where pretty-printing is\n'?
Indent 'desired.  It offers programmatic functionality\n'?
Indent 'similar to the paragraph wrapping or filling\n'?
Indent 'features found in many text editors.'?
even line The textwrap module can be used to format text for
output in situations where pretty-printing is
even line desired.  It offers programmatic functionality
even line similar to the paragraph wrapping or filling
even line features found in many text editors.
'''
#RM:  if I commented out print("Indent {!r}?".format(line)), then the even line output is printed only.

#indent the first line can be controlled independently of subsequent lines
dendentedtext = textwrap.dedent(sampletext).strip()
print(textwrap.fill(dendentedtext, initial_indent="", subsequent_indent=" "*4, width=50))
'''print
The textwrap module can be used to format text for
    output in situations where pretty-printing is
    desired.  It offers programmatic functionality
    similar to the paragraph wrapping or filling
    features found in many text editors.
'''

#shorten() to truncate text to create a summary or preview.  All existing whitespace, such as tabs, newlines, and series of multiple spaces, will be standardized to a single space. Then the text will be truncated to a length less than or equal to what is requested, between word boundaries so that no partial words are included.  RM:  [...] is placed at the end of the text.
dendentedtext = textwrap.dedent(sampletext).strip()
shortentext = textwrap.shorten(dendentedtext, 100)
print(shortentext)
'''print
The textwrap module can be used to format text for output in situations where pretty-printing [...]
'''
dendentedtext = textwrap.dedent(sampletext).strip()
shortentext = textwrap.shorten(dendentedtext, 100)
print(textwrap.fill(shortentext, width=30))
'''print
The textwrap module can be
used to format text for output
in situations where pretty-
printing [...]
'''
dendentedtext = textwrap.dedent(sampletext).strip()
shortentext = textwrap.shorten(dendentedtext, 100, placeholder = " (cont)")
print(textwrap.fill(shortentext, width=30))
'''print
The textwrap module can be
used to format text for output
in situations where pretty-
printing (cont)
'''

#wrap() returns a list of the output lines.  RM:  a string text to a list and each list item is a line in a string text
print(textwrap.wrap(sampletext))
'''print
['     The textwrap module can be used to format text for output in', 'situations where pretty-printing is desired.  It offers', 'programmatic functionality similar to the paragraph wrapping     or', 'filling features found in many text editors.']
'''
dendentedtext = textwrap.dedent(sampletext).strip()
print(textwrap.wrap(dendentedtext))
'''print
['The textwrap module can be used to format text for output in', 'situations where pretty-printing is desired.  It offers programmatic', 'functionality similar to the paragraph wrapping or filling features', 'found in many text editors.']
'''

print(textwrap.fill(sampletext, replace_whitespace=False)) #all whitespace is not single-spaced
'''print

    The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
    or
filling features found in many text editors.
'''
print(textwrap.fill(sampletext, drop_whitespace=False)) #whitespaces begin and end of every line is kept
'''print
     The textwrap module can be used to format text for output in     
situations where pretty-printing is desired.  It offers     
programmatic functionality similar to the paragraph wrapping     or 
filling features found in many text editors. 
'''
dendentedtext = textwrap.dedent(sampletext).strip()
print(textwrap.fill(dendentedtext, max_lines=3))
'''print
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers programmatic
functionality similar to the paragraph wrapping or filling [...]
'''