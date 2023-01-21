grammar Rhtml;

// enter point for a program
prog: html_expr EOF;

// integer range of for loop
range: LEFT INT '..' INT RIGHT;

// for loop, it iterates either through integers from number a to b, list of ints, or list of strings
// inside of a for loop can be another for loop, a list or tag
for_loop: FOR (range | int_list | string_list)'.' EACH DO (tag_expr | for_loop | list_inside)+ END;

// list of integers
int_list: LEFT int_elems? RIGHT;
int_elems: INT ( ',' INT)*;

// list of strings
string_list: LEFT string_elems? RIGHT;
string_elems: STRING ( ',' STRING)*;

// html block
html_expr: HTML DO main_tag_expr* END;

// main tag block
main_tag_expr: MAIN_TAG DO (tag_expr | tag_expr | for_loop | list)* END;

// double or single tag block, both can have options, but only double can have a tag_inside
tag_expr: (DOUBLE_TAG DO tag_option_expr* tag_inside* END) | (SINGLE_TAG DO tag_option_expr* END);

// options of what can be inside a tag block: string or int, another tag block, a for loop, value from for loop on
// higher level or a list
tag_inside: (string_int_inside | tag_expr | for_loop | ITER | list);

// string or an int, for easier displaying in visitor
string_int_inside: STRING | INT;

// tag attribute
tag_option_expr: TAG_OPTION '=' STRING;

// unordered or ordered list block, can have only for loop op list_inside
list: LIST DO (for_loop | list_inside)* END;

// point of list
list_inside: LIST_ITEM DO (string_int_inside | ITER) END;

// TOKENS
// html related tokens: html
HTML : 'html';

// html related tokens: lists
LIST: 'ul' | 'ol';
LIST_ITEM: 'li';

// html related tokens: tags
MAIN_TAG: 'body' | 'footer' | 'head' | 'main' | 'nav';
DOUBLE_TAG: 'a' | 'abbr' | 'address' | 'area' | 'article' | 'aside' | 'b' | 'bdi' | 'bdo' | 'blockquote' | 'button' | 'cite' | 'del' | 'details' | 'div' 
            | 'em' | 'h'[1-6] | 'header' | 'hr' | 'i' | 'iframe' | 'ins' | 'kbd' | 'mark' | 'meta' | 'meter' | 'noscript' | 'object' | 'p' | 'pre' | 'progress'
            | 'q' | 's' | 'script' | 'section' | 'small' | 'span' | 'strong' | 'sub' | 'summary' | 'sup' | 'textarea' | 'time' | 'title' | 'u' | 'var' | 'wbr';
SINGLE_TAG: 'base' | 'br' | 'embed' | 'img' | 'link' | 'param';
TAG_OPTION: '!'[a-z]+;

// for loop tokens
LEFT: '[';
RIGHT: ']';
ITER: 'iter';
FOR: 'for';
EACH: 'each';

// general tokens
END : 'end';
DO : 'do';
INT: '0' | '-'?[1-9][0-9]*;
STRING: '"'[a-zA-Z0-9 \n?!.,:;]*'"';
WHITESPACE: [ \t\n\r] -> skip;
