#!/usr/bin/env clojure
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

(println (apply max-key count (collatz-seqs 100000)))
