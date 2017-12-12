;just fot test

(define x 2)
(define ++ (lambda (x y) 
             (begin
               (display "x:{0}" x)
               (display "y:{0}" y)
               (+ x y))))
(display (++ 4 1))
(display x)
