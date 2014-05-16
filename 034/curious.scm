(define (factorial n)
  (apply * (iota n 1)))

(define (digits n)
  (if (zero? n)
    '()
    (cons (remainder n 10) (digits (quotient n 10)))))

(define (curious? n)
  (and (= (apply + (map factorial (digits n))) n)
       (> (length (digits n)) 1)))

(display (apply + (filter curious? (iota 50000))))
(newline)
