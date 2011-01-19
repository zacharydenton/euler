#!/usr/bin/env clojure
; The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
;
; Find the sum of all the primes below two million.
(defn primes [n]
  (defn improve [p nums]
    (filter #(or 
               (not (= (rem % p) 0))
               (= % p))
            nums))
  (defn prime-iter [p nums i]
    (if (> (* p p) n)
      nums
      (prime-iter (nth nums (+ i 1)) (improve (nth nums (+ i 1)) nums) (+ i 1))))
  (prime-iter 2 (range 2 (+ n 1)) -1))

(println (apply + (primes 2000000)))
