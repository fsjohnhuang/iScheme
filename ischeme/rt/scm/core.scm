(define = (lambda (a b) (let ((r (- a b)))
                          (and (not (< r 0))
                               (not (> r 0))))))
(define <= (lambda (a b) (not (> (- a b) 0))))
(define >= (lambda (a b) (not (< (- a b) 0))))
(define zero? (lambda (x) (= 0 x)))
(define positive? (lambda (x) (> x 0)))
(define negative? (lambda (x) (< x 0)))
(define odd? (lambda (x) (= 1 (% x 2))))
(define even? (lambda (x) (not (odd? x))))
(define sqrt (lambda (x) (* x x)))
(define ++ (lambda (x) (+ 1 x)))
(define -- (lambda (x) (- x 1)))
(define abs (lambda (x) (if (> 0 x) (* x -1) x)))
(define max (lambda (a b) (if (> a b) a b)))
(define min (lambda (a b) (if (> a b) b a)))