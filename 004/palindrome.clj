#!/usr/bin/env clojure
(defn palindrome? [n]
  (= (seq (str n)) (reverse (str n))))

(defn palindromes [limit]
  (filter palindrome? (for [a (range 100 1000) b (range a 1000)] (* a b))))

(println (reduce max (palindromes 1000)))
