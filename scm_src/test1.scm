(display "begin now")
(define a (list 1 2 3))
(display (map (lambda (a) (++ a)) a))
(display (filter (lambda (x) (eq? x 2)) a))
(display (reduce (lambda (accu x) (cons x accu)) (list) a))

;(py/import 'webdriver 'selenium)
;
;(define driver (.Chrome webdriver))
;
;(define <find-element
;  (lambda (driver)
;    (lambda (slctr-type slctr)
;      (.find_element driver slctr-type slctr))))
;
;(define <click
;  (lambda (driver)
;    (lambda (slctr-type slctr)
;      (.click (.find_element driver slctr-type slctr)))))
;
;(define find-element
;  (<find-element driver))
;(define click
;  (<click driver))
