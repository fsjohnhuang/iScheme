# iScheme
Implementation of Scheme interpreter in Python 

## Roadmap
### `v0.1.1`
1. 支持函数定义简写
```
(define (func-name arg1 arg2)
  (display arg1)
  (+ arg1 arg2))
```
2. 支持Symbol类型，可通过`'()`构造list。

### `v0.2.0`
1. 引入独立于Python的类型系统。
2. 支持多行注释
```
#!
  今天天气好晴朗，处处好风光，好风光～:D
!#
```
3. 支持多行字符串
```
"
  今天天气好晴朗，处处好风光，好风光～:D
"
```

### `v0.3.0`
1. 支持macro

## Log
### `v0.1.0`
1. 实现基本的解释器功能，并支持以下special form和procedure
```
define
lambda
begin
if
not
and
or
let
let*
+,-,*,/,%,**,sqrt,++,--,abs,min,max,zero?,nagetive?,positive?,even?,odd?,>,<,>=,<=,=
eq?
cons
car
cdr
list
map,filter,reduce
count
display
tap
str
```
