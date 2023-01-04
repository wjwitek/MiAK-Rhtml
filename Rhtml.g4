grammar Rhtml;

prog: ruby_expr* html_expr EOF;

ruby_expr: arithmetic_expr | var_decl | tag_expr | for_loop;

// loop
range: '['INT'..'INT']';
for_loop: (range | int_list | string_list | VAR)'.' EACH DO '|'VAR'|' ruby_expr+ END;

// general ruby

var_decl: INT_TYPE VAR '=' (INT | arithmetic_expr) | STRING_TYPE VAR '=' STRING | STRING_LIST_TYPE VAR '=' string_list | INT_LIST_TYPE VAR '=' int_list;

int_list: '[' int_elems? ']';
int_elems: INT ( ',' INT)*;

string_list: '[' string_elems? ']';
string_elems: STRING ( ',' STRING)*;

// arithmetic
arithmetic_expr: arithmetic_expr '*' arithmetic_expr
                | arithmetic_expr '+' arithmetic_expr
                | arithmetic_expr '-' arithmetic_expr
                | arithmetic_expr '/' arithmetic_expr
                | INT;

// html expression

html_expr: HTML DO main_tag_expr* END;

main_tag_expr: MAIN_TAG DO tag_expr* END;

tag_expr: (DOUBLE_TAG DO tag_option_expr* (tag_inside | tag_expr)* END) | (SINGLE_TAG DO tag_option_expr* END);

tag_inside: (STRING | INT | ruby_expr);

tag_option_expr: TAG_OPTION '=' STRING;

// tokens
// general tokens
END : 'end';
DO : 'do';

// html related tokens
HTML : 'html';

// tags
MAIN_TAG: 'body' | 'footer' | 'head' | 'main' | 'nav';
DOUBLE_TAG: 'a' | 'abbr' | 'address' | 'area' | 'article' | 'aside' | 'b' | 'bdi' | 'bdo' | 'blockquote' | 'button' | 'cite' | 'del' | 'details' | 'div' 
            | 'em' | 'h'[1-6] | 'header' | 'hr' | 'i' | 'iframe' | 'ins' | 'kbd' | 'mark' | 'meta' | 'meter' | 'noscript' | 'object' | 'p' | 'pre' | 'progress'
            | 'q' | 's' | 'script' | 'section' | 'small' | 'span' | 'strong' | 'sub' | 'summary' | 'sup' | 'textarea' | 'time' | 'title' | 'u' | 'var' | 'wbr';
SINGLE_TAG: 'base' | 'br' | 'embed' | 'img' | 'link' | 'param';

// tag options
TAG_OPTION: '!'[a-z]+;


// data types
EACH: 'each';
STRING_LIST_TYPE: 'string[]';
INT_LIST_TYPE: 'int[]';
STRING_TYPE: 'str';
INT_TYPE: 'int';
VAR: [a-zA-Z][a-zA-Z0-9]*;
STRING: '"'[a-z]*'"';
INT: '0' | '-'?[1-9][0-9]*;
WHITESPACE: [ \t\n\r] -> skip;
