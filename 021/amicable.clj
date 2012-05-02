#!/usr/bin/env clojure
(defn divisors [n]
  (filter #(zero? (mod n %)) (range 1 (+ 1 (/ n 2)))))

(defn d [n]
  (reduce + (divisors n)))

(defn amicable? [a b]
  (and (not (= a b)) (= (d a) b) (= (d b) a)))

(println (reduce + (filter #(amicable? % (d %)) (range 10000))))
