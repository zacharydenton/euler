#!/usr/bin/env clojure
(defn palindrome? [string]
  (= (seq string) (reverse string)))

(defn palindrome-number? [number]
  (palindrome? (str number)))

(defn combine [lst1 lst2]
  (mapcat (fn [x] (map #(list % x) lst1)) lst2))

(defn palindromes [limit]
  (filter palindrome-number? (map #(reduce * %) (combine (range limit) (range limit)))))

(println (last (sort (set (palindromes 1000)))))

