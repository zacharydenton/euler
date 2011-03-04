#!/usr/bin/env clojure
(defn divisible-to-x? [n x]
  (every? #(= (rem n %) 0) (range 1 (+ x 1))))

(def numbers (iterate inc 1))

(def divisible-to-20 (filter #(divisible-to-x? % 20) numbers))
(def divisible-to-10 (filter #(divisible-to-x? % 10) numbers))

(println (first divisible-to-20))
