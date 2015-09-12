#!/usr/bin/env clojure
(def fibs (lazy-cat [0 1] (map + (rest fibs) fibs)))
(println (reduce + (filter even? (take-while #(< % 4000000) fibs))))

