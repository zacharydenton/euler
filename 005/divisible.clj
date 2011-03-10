#!/usr/bin/env clojure
(defn divisible-to-x? [n x]
  (every? #(= (rem n %) 0) (reverse (range 1 (+ x 1)))))

(defn divisible-to [x]
  (if (= x 1)
    x
    (first (filter #(divisible-to-x? % x) (iterate inc (divisible-to (- x 1)))))))

(println (divisible-to 20))
