#!/usr/bin/env clojure
; A palindromic number reads the same both ways. The largest palindrome
; made from the product of two 2-digit numbers is 9009 = 91  99.
;
; Find the largest palindrome made from the product of two 3-digit numbers.

(defn palindrome? [string]
  (= (seq string) (reverse string)))

(defn palindrome-number? [number]
  (palindrome? (str number)))

(defn combine [lst1 lst2]
  (mapcat (fn [x] (map #(list % x) lst1)) lst2))

(defn palindromes [limit]
  (filter palindrome-number? (map #(reduce * %) (combine (range limit) (range limit)))))

(println (last (sort (set (palindromes 1000)))))

