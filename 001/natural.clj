#!/usr/bin/env clojure
(defn multiple? [n]
  (or (= (rem n 3) 0) (= (rem n 5) 0)))

(def numbers (filter multiple? (range 1000)))
(def sum-numbers (apply + numbers))
(println sum-numbers)
