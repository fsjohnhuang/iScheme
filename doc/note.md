## Scheme中`=`,`eq?`,`eqv?`和`equal?`的区别
`=`，判断两个数值类型变量的值是否相同。
`eq?`，判断两个变量是否指向同一个对象。
`equal?`，判断两个变量指向的对象是否结构相同且结构中的内容相同。
`eqv?`和`eq?`基本相同。

## Python中`==`,`is`
`is`，判断两个变量是否指向同一个对象。
```
a=1
id(a)  #=> 123
b=1
id(b)  #=> 123
a is b #=> True
```
`==`，判断两个变量指向的对象是否结构相同且结构中的内容相同。

## Scheme中的let,let\*实现
let和let\*实际上是通过lambda来实现
```
(define-syntax let
  (syntax-rules ()
    ((let ((var expr) ...) body ...)
      ((lambda (var ...) body ...) expr ...))))
```
