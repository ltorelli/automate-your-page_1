def generate_project_HTML(section_number, subheadline, section_text):
    part_1 = '''
    <h1 class="headline">''' + section_number + '</h1>'
    part_2 = '''
        <h2 class="subhead">''' + subheadline + '</h2>'
    part_3 = '''
            <div class="section"> 
             '''
    part_4 = '   <p class="smcap">'+ section_text 
    part_5 = '</p>'        
    part_6 = '''
            </div>'''
    
    complete_HTML = part_1 + part_2 + part_3 + part_4 + part_5 + part_6
    return complete_HTML
     
last = 2

def get_section_number(project):
    start = project.find('Section')
    end = project.find('Title:')
    section_number = project[start : end-last]
    return section_number

def get_subheadline(project):
    start = project.find('Title:')
    end = project.find('Notes:')
    subheadline = project[start : end-last]
    return subheadline

def get_section_text(project):
    start = project.find('Notes:')
    end = project.find('Section')
    section_text = project[start: end-last]
    return section_text

advance = 1
count_start = 0

def get_section_by_number(text, section_number):
    counter = count_start
    while counter < section_number:
        counter = counter + advance
        next_section_start = text.find('Section')
        next_section_end   = text.find('Section', next_section_start + advance)
        if next_section_end >= count_start:
            section = text[next_section_start:next_section_end]
        else:
            next_section_end = len(text)
            section = text[next_section_start: ]
        text = text[next_section_end:]
    return section

HTML_TEXT = '''
Section 1 
Title: The Basics of Web and HTML 
Notes: This is the beginning of my site for the Nanodegree class. The first thing I learned was how to use tags in order to make words <b>bold</b> or <em>italicized</em>. <span class="link">This image is also a link to Grantland.com, which has many interesting articles about sports and pop-culture, and therefore I visit it frequently:<br><br><a href = "http://www.grantland.com" target=_blank><img src="images/grantland.png" alt="Sorry!"></a></span>I also learned the difference between <b>inline</b> and <b>block</b> elements. Examples of inline tags are the break tag, the form tag and the span tag. Examples of block tags, <em>which are intended to make a box of text</em>, are the paragraph tag, the strong tag and the div tag. 
Section 2 
Title: Creating a Structured Document 
Notes: Websites are structured using a 'tree' with matching elements that get lined up using "tags" in a computer language called HTML. The computer then interprets the HTML in order to identify how the page should look using style sheets (CSS). Most browsers have developer tools that allow you to see the source code as well as the style sheets, which is helpful for learning how to code a site. Basically everything on a website is just a series of boxes made to look like other things, even <b class="green">circles</b>. Websites can also be thought of as one big grid with many boxes within them. 
Section 3 
Title: Adding CSS Style and Structure 
Notes: Cascading style sheets (CSS) can be added to your code as a linked file <b>or</b> at the top of the HTML document <b>or</b> within the tag itself (very repetitive, not recommended). Not repeating yourself is important because it will save time and ensure that site formatting and appearance is consistent throughout. "Cascading" means that rules are applied not only to the elements they directly match, but also to all of those elements' child elements. However, if a child element has multiple, overlapping rules defined for it, the more specific rule takes effect. That idea is known as inheritance and understanding it requires abstract thinking. As mentioned above, HTML elements are placed into boxes and each box has 4 main components, but can also have many sub-components. Because there are so many components to each box, it can often be hard to get the size of a box just right. Adding the rule "display: flex;" to the appropriate CSS will let 'divs' appear next to each other instead of taking up the whole page. 
Section 4 
Title: Introduction to Serious Programming 
Notes: Most machines do one or a few things with some settings/options, computers on the other hand, can do anything based on how it is programmed...and very fast. Python is a high level language to interpret & execute programs into a language the computer understands. Why not use English or any spoken language? Because language is too ambiguous (not specific) and verbose (not precise). Python grammar: expression --> expression operator expression where non-terminal values are replaced until only terminal values remain. Computer processors need to be small so that light can be sent across fast enough for a cycle to complete. 
Section 5 
Title: Variables and Strings 
Notes: Using names to keep track of values in order to know what numbers and other things mean is known as a variable (name = expression). Variables start with a letter or underscore. Variables can vary based on the most recent assignment. You have to assign/introduce a value to each variable before adding or changing it to another variable. Strings are sequences of characters surrounded by quotes. Use double or single quotes to put the opposite as text in your string. Put strings together using a '+' sign to concatenate. Index strings extract subsequences from a string using brackets. Remember that indexes start at 0. Use negative numbers to count from the back. You can multiply with strings, but not add.  Subsequences can be found using expression strings that are a subsequence of all characters in the variable. Leave the ':' open to count to end, start with ':' to count from the beginning. Find is a method/procedure used to find specific substrings in a string. If a string isn't found in the search, the value returned will be -1. Python notes start with '#' and Python cares about capitalization. 
Section 6 
Title: Functions/Procedures 
Notes: Functions take input and produce output using the keywords 'def' and 'return'. There is a difference between how functions are defined (inputs) vs how they are used (print lines & output are different for example). In code like the following, the code in parenthesis defines the function: <em>def rest_of_string(s):</em> versus code like this where it defines the variable to be used when running the function: <em>print rest_of_string("audacity").</em> Functions allow programs to perform the same activity multiple times for different sets of variables, saving time so that each activity doesn't need to be coded separately. If a function doesn't have a return call, then there isn't any outcome ("none" is returned). 
Section 7 
Title: Control Flow and Loops 
Notes: Code can make decisions by using operators such as 'if', 'else' and 'or' to allow for comparisons to be done within a block. Boolean decisions return a 'true' or 'false' value. For an 'or' statement, if the first expression evaluates to true, the value is true and the second expression is not evaluated. If the value of the first expression is false, then the value of the <b>or</b> is the value of the second expression. Loops, such as the "while" operator allow for a function to run as many times as needed and can even run forever if not written correctly. A "break" operator stops a loop when a test condition becomes true. Bugs are inevitable and it is important to develop a strategy for finding and getting rid of them. 
Section 8 
Title: Lists and For Loops 
Notes: Lists are sequences of anything. Lists are formatted using square brackets where the elements are separated by commas. Lists are indexed starting at 0. Mutation changes the value of a list after it has been created it by replacing the value and changing the assignment. Changing a value affects other values that reference the same object (aliasing). In mutation procedures, there's no need to have a return statement of the changed value. Append: method for adding a new element to the end of a list (list stays the same). Plus: add/concatenate two lists, produces new list. Len: finding the length or number of elements or characters in a string. For: for each element in the list, assign that element to the name and evaluate the block. Index can find the position in a list where the value occurs. Gives error if the value is not found. In: true or false if a value is in a list; not in: true or false if a value is not in a list. Learning how technology actually works is how you build your technological empathy. This empathy will help you diagnose and fix bugs that otherwise would have been a mystery to you. 
Section 9 
Title: How to Solve Problems 
Notes: For solving complex problems, first make sure you understand the problem. In a computational problem, it can be defined by possible inputs and the relationship between inputs and desired outputs. First rule: what are the inputs? What is the set of valid inputs? How are inputs represented? Second rule: what are the outputs? Third rule: solve the problem. Work out examples to understand the relationship between inputs and outputs. Consider systematically how a human would solve the problem. Write an algorithm and/or "pseudo code" that solves the problem. Decide, should I implement the algorithm? Or try to find a better way by determining what isn't handled in pseudo code. Find a simple mechanical solution and don't optimize prematurely. Once you start coding, start with the portion of the procedure that solves the main/simple case. Write small pieces of code so you know what they do (develop incrementally).  '''

def generate_project(text):
    current_section_number = advance
    section = get_section_by_number(text, current_section_number)
    project = """ """
    while section != '':
        section_number = get_section_number(section)
        subheadline = get_subheadline(section)
        section_text = get_section_text(section)
        project_html = generate_project_HTML(section_number, subheadline, section_text)
        project = project + project_html
        current_section_number = current_section_number + advance
        section = get_section_by_number(text, current_section_number)
    return project

print "<body>" + generate_project(HTML_TEXT) 
print "</body>"


