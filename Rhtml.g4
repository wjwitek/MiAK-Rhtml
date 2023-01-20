grammar Rhtml;

prog: ruby_expr* html_expr EOF;

ruby_expr: tag_expr | for_loop;

// loop
range: LEFT INT DOTS INT RIGHT;
for_loop: FOR (range | int_list | string_list)'.' EACH DO (ruby_expr | list_inside)+ END;

// general ruby
int_list: '[' int_elems? ']';
int_elems: INT ( ',' INT)*;

string_list: '[' string_elems? ']';
string_elems: STRING ( ',' STRING)*;

// html expression

html_expr: HTML DO main_tag_expr* END;

main_tag_expr: MAIN_TAG DO (tag_expr | ruby_expr | list)* END;

tag_expr: (DOUBLE_TAG DO tag_option_expr* (tag_inside | tag_expr)* END) | (SINGLE_TAG DO tag_option_expr* END);

tag_inside: (string_int_inside | ruby_expr | ITER | list);

string_int_inside: STRING | INT;

tag_option_expr: TAG_OPTION '=' STRING;

list: LIST DO (for_loop | list_inside)* END;

list_inside: LIST_ITEM DO (string_int_inside | ITER) END;

// tokens
// general tokens
END : 'end';
DO : 'do';

// html related tokens
HTML : 'html';

// lists
LIST: 'ul' | 'ol';
LIST_ITEM: 'li';

// tags
MAIN_TAG: 'body' | 'footer' | 'head' | 'main' | 'nav';
DOUBLE_TAG: 'a' | 'abbr' | 'address' | 'area' | 'article' | 'aside' | 'b' | 'bdi' | 'bdo' | 'blockquote' | 'button' | 'cite' | 'del' | 'details' | 'div' 
            | 'em' | 'h'[1-6] | 'header' | 'hr' | 'i' | 'iframe' | 'ins' | 'kbd' | 'mark' | 'meta' | 'meter' | 'noscript' | 'object' | 'p' | 'pre' | 'progress'
            | 'q' | 's' | 'script' | 'section' | 'small' | 'span' | 'strong' | 'sub' | 'summary' | 'sup' | 'textarea' | 'time' | 'title' | 'u' | 'var' | 'wbr';
SINGLE_TAG: 'base' | 'br' | 'embed' | 'img' | 'link' | 'param';

// tag options
TAG_OPTION: '!'[a-z]+;


// data types
LEFT: '[';
RIGHT: ']';
DOTS: '..';
ITER: 'iter';
FOR: 'for';
EACH: 'each';
STRING_LIST_TYPE: 'string[]';
INT_LIST_TYPE: 'int[]';
STRING_TYPE: 'str';
INT_TYPE: 'int';
STRING: '"'[a-zA-Z0-9 \n]*'"';
INT: '0' | '-'?[1-9][0-9]*;
WHITESPACE: [ \t\n\r] -> skip;
