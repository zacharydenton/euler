#!/usr/bin/env clojure
(defn divisible-to-x? [n x]
  (every? #(= (rem n %) 0) (range 1 (+ x 1))))

(println (first (filter #(divisible-to-x? % 20) (iterate inc 1))))
