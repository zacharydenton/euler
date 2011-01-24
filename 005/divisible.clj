#!/usr/bin/env clojure
; 2520 is the smallest number that can be divided by each
; of the numbers from 1 to 10 without any remainder.
;
; What is the smallest positive number that is evenly divisible
; by all of the numbers from 1 to 20?

(defn divisible-to-x? [n x]
  (every? #(= (rem n %) 0) (range 1 (+ x 1))))

(def numbers (iterate inc 1))

(def divisible-to-20 (filter #(divisible-to-x? % 20) numbers))
(def divisible-to-10 (filter #(divisible-to-x? % 10) numbers))

(println (first divisible-to-20))
