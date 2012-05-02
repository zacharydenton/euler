#!/usr/bin/env clojure
(println (reduce + (map #(- (int %) 48) (str (reduce * (range BigInteger/ONE 100))))))
