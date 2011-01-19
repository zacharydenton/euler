#!/usr/bin/env clojure
; The following iterative sequence is defined for the set of positive integers:
;
; n -> n/2 (n is even)
; n -> 3n + 1 (n is odd)
;
; Using the rule above and starting with 13, we generate the following sequence:
;
; 13  40  20  10  5  16  8  4  2  1
;
; It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 
; terms. Although it has not been proved yet (Collatz Problem), it is thought that all
; starting numbers finish at 1.
;
; Which starting number, under one million, produces the longest chain?
;
; NOTE: Once the chain starts the terms are allowed to go above one million.

(defn collatz [start]
  (defn next-collatz [n]
    (if (even? n)
      (/ n 2)
      (+ (* 3 n) 1)))
  (def memo-collatz
    (memoize next-collatz))
  (defn not-one? [n]
    (not (= n 1)))
  (concat (take-while not-one? (iterate next-collatz start)) [1]))

(defn collatz-seqs [limit]
  (map collatz (range 1 limit)))

(time (apply max-key count (collatz-seqs 100000)))
