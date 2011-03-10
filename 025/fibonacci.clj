#!/usr/bin/env clojure
(defn fib [n]
  (loop [a 1 b 0 count n]
    (if (= count 0)
      b
      (recur (+ a b) a (dec count)))))

(defn digits [n]
  (map #(- (int %) 48) (str n)))

(println (first (filter #(= (count (digits (fib %))) 1000) (iterate inc 1))))
