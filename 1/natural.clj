#!/usr/bin/env clojure
; If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
; get 3, 5, 6 and 9. The sum of these multiples is 23.
;
; Find the sum of all the multiples of 3 or 5 below 1000.

(defn multiple? [n]
  (or (= (rem n 3) 0) (= (rem n 5) 0)))

(def numbers (filter multiple? (range 1000)))
(def sum-numbers (apply + numbers))
(println sum-numbers)
