#!/usr/bin/env clojure
(defn fib-recursive [n]
  (cond (= n 0) 0
        (= n 1) 1
        :else (+ (fib-recursive (- n 1))
                 (fib-recursive (- n 2)))))

(defn fib [n]
  (defn fib-iter [a b count]
    (if (= count 0)
      b
      (fib-iter (+ a b) a (dec count))))
  (fib-iter 1 0 n))

(def fibs(filter #(< % 4000000) (map fib (range 100))))
(def sum (apply + (filter even? fibs)))
(println sum)
