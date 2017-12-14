(define (= a b)
  (let ((r (- a b)))
    (and (not (< r 0))
         (not (> r 0)))))

(define (<= a b)
  (not (> (- a b) 0)))

(define (>= a b)
  (not (< (- a b) 0)))

(define (zero? x)
  (= 0 x))

(define (positive? x)
  (< 0 x))

(define (negative? x)
  (> 0 x))

(define (odd? x)
  (= 1 (% x 2)))

(define (even? x)
  (not (odd? x)))

(define (sqrt x)
  (* x x))

(define (++ x)
  (+ 1 x))

(define (-- x)
  (- x 1))

(define (abs x)
  (if (> 0 x)
    (* x -1)
    x))

(define (max a b)
  (if (> a b) a b))

(define (min a b)
  (if (> a b) b a))

(define (count xs)
  (if (eq? '() xs)
    0
    (+ 1 (count (cdr xs)))))

(define (reduce f accu xs)
  (if (eq? (list) xs)
    accu
    (reduce f (f accu (car xs)) (cdr xs))))

(define (map f xs)
  (if (eq? '() xs)
    '()
    (cons (f (car xs)) (map f (cdr xs)))))

(define (filter f xs)
  (if (eq? '() xs)
    '()
    (let ((a (car xs)))
      (if (f a)
        (cons a (filter f (cdr xs)))
        (filter f (cdr xs))))))

(define (tap a)
  (display a)
  a)
