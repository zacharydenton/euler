#!/usr/bin/env clojure 
(defn divisor? [b n]
  (= (rem n b) 0))

(defn triangle-number [n]
  (cond 
    (< n 1) nil
    (= n 1) 1
    :else (+ n (triangle-number (dec n)))))

(defn divisors [n]
  (cons n (filter #(divisor? % n) (range 1 (inc (/ n 2))))))


(defn num-divisors [n])

(def triangle-numbers (map triangle-number (range 1 1000)))
(println (first (filter #(> (num-divisors %) 500) triangle-numbers)))
