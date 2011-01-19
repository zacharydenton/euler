#!/usr/bin/env clojure
; The sum of the squares of the first ten natural numbers is,
; 1^(2) + 2^(2) + ... + 10^(2) = 385
; 
; The square of the sum of the first ten natural numbers is,
; (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
;
; Hence the difference between the sum of the squares of the first ten natural 
; numbers and the square of the sum is 3025 − 385 = 2640.

; Find the difference between the sum of the squares of the first one hundred 
; natural numbers and the square of the sum.
(defn square [x]
  (* x x))

(defn sum-squares [limit]
  (apply + (map square (range 1 (+ limit 1)))))

(defn square-sum [limit]
  (square (apply + (range 1 (+ limit 1)))))

(println (- (square-sum 100) (sum-squares 100)))
