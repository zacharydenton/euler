#!/usr/bin/env clojure
(defn reversed [string]
  (apply str (reverse string)))

(defn palindrome? [string]
  (= string (reversed string)))

(defn palindrome-in-decimal-and-binary? [n]
  (and (palindrome? (Integer/toString n 2))
       (palindrome? (Integer/toString n))))

(println (reduce + (filter palindrome-in-decimal-and-binary? (range 1 1000000))))
