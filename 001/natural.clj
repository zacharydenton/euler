#!/usr/bin/env clojure
(defn multiple? [n]
  (or (= (rem n 3) 0) (= (rem n 5) 0)))

(println (reduce + (filter multiple? (range 1000))))
