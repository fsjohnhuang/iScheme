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
2. 支持Symbol类型，可通过`'()`构造list
3. 支持`(load 'scm.core)`和环境变量`PATH`来加载模块
4. 新增`doto`Special Form

### `v0.1.2`
2. 支持`py`模块
```
; 加载python模块
(py/import 'time)
(.sleep time 100)

; 加载python包
(py/from 'selenum
  '((webdriver wd)))

(define (make-click driver)
  (define (slctr-type slctr)
    (doto
      (.find_element driver "css selector" "button")
      (.click))))

(let* ((driver (.Chrome wd))
       (click (make-click driver)))
  (.get driver "http://www.baidu.com")
  (click "css selector" "button"))
```

### `v0.1.3`
1. 支持`require`来加载模块
```
; 加载位于$WORK_DIR/py_wrapper/core.scm
(require '(py-wrapper.core pyw (wait)))

(pyw/wait 1000)
(wait 1000)
```
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

### `v0.2.0`
1. 引入独立于Python的类型系统。

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
