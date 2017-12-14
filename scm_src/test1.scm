(display "begin now")
(define c 1)

(define (say a b)
  (display a)
  (display c)
  (list a b))

(define a (say "a" "b"))
(define (mapper x)
  (str x "1"))

(display (map mapper a))
